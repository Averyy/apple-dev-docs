# TN3103: Apple Pay on the Web troubleshooting guide

**Framework**: Technotes  
**Role**: Technote

Diagnose and resolve common configuration, domain verification, merchant validation, and payment token decryption issues when implementing Apple Pay on the Web.

## Overview

Implementing Apple Pay on the Web involves coordinating client-side JavaScript, your backend application server, and Apple Pay servers to authenticate transactions and decrypt payment tokens securely. Because this flow spans multiple systems, misconfigurations in certificates, domains, or network security frequently disrupt checkout.

This technote guides you through troubleshooting each stage of an Apple Pay on the Web implementation. It covers:

- Registering merchant identifiers and configuring merchant assets
- Verifying your merchant domain and resolving common verification failures
- Constructing client-side payment requests with [Apple Pay JS](https://developer.apple.com/documentation/apple_pay_on_the_web/apple_pay_js_api)
- Completing server-to-server merchant validation and diagnosing validation errors
- Decrypting the payment token with your payment processing identity

> **Note**: This document focuses on direct integrations where your website connects to Apple Pay servers and passes payment tokens to a payment service provider (PSP). It does not cover third-party client libraries, software development kits (SDKs), or turnkey hosted checkouts. If you use a third-party checkout integration, contact your vendor directly for support.

For troubleshooting specific stages of the payment flow outside merchant identity and domain setup, consult these companion technotes:

- [TN3173: Troubleshooting issues with your Apple Pay merchant identifier configuration](./tn3173-troubleshooting-issues-with-your-apple-pay-merchant-id-configuration.md)
- [TN3174: Diagnosing issues with the Apple Pay payment sheet on your website](./tn3174-diagnosing-issues-with-the-apple-pay-payment-sheet-on-your-website.md)
- [TN3175: Diagnosing issues with displaying the Apple Pay button on your website](./tn3175-diagnosing-issues-with-displaying-the-apple-pay-button-on-your-website.md)
- [TN3176: Troubleshooting Apple Pay payment processing issues](./tn3176-troubleshooting-apple-pay-payment-processing-issues.md)
- [TN3206: Updating Apple Pay certificates](./tn3206-updating-apple-pay-certificates.md)

## Creating merchant assets

To register your business as a merchant, create a Merchant Identifier (Merchant ID) in your Apple Developer account under Certificates, Identifiers & Profiles. A Merchant ID is the unique identifier that binds your merchant domain, Merchant Identity Certificate, Payment Processing Certificate, and transaction assets. A Merchant ID uses reverse-DNS format, such as `merchant.com.testbed.applepay`.

> **Note**: If your PSP manages Apple Pay access on your behalf without requiring an individual Apple Developer account, your setup workflow differs. Contact your PSP for instructions on configuring your merchant assets.

After creating your Merchant ID, create a Payment Processing Certificate using a 256-bit elliptic curve cryptography (ECC) key pair. If your PSP provides this certificate or creates the certificate signing request (CSR) for you, proceed to Step 2 below.

### Create a payment processing identity

1. In Keychain Access on your Mac, create a [certificate signing request](https://developer.apple.com/help/account/certificates/create-a-certificate-signing-request) (CSR) using a 256-bit ECC key pair.
2. In Certificates, Identifiers & Profiles, select your Merchant ID, navigate to Payment Processing Certificate, and upload your CSR to generate the certificate.
3. Download the generated certificate and double-click it to install it into Keychain Access on the Mac where you created the initial CSR. Installing the certificate alongside the matching private key creates your Payment Processing Identity (a PKCS #12 file, or `.p12`). If you created the CSR outside macOS, store the certificate and private key together on that same system.

> ❗ **Important**: Store your payment processing private key securely and back it up. Your payment processor must have access to this identity to decrypt incoming payment tokens.

Alternatively, your PSP may generate the CSR on their servers and provide the CSR file for you to upload in Certificates, Identifiers & Profiles. In this workflow, your PSP already retains the private key, so you do not need to export the private key from your Mac.

### Create a merchant identity certificate

In Certificates, Identifiers & Profiles, navigate to your Merchant ID to create a [Merchant Identity Certificate](https://developer.apple.com/help/account/capabilities/configure-apple-pay-on-the-web#create-a-merchant-identity-certificate). This certificate authenticates your server when requesting a payment session from Apple Pay servers.

1. In Keychain Access on your Mac, create a [certificate signing request](https://developer.apple.com/help/account/certificates/create-a-certificate-signing-request) using a 2048-bit RSA key pair.
2. Upload the CSR to the Merchant ID configuration page to generate your Merchant Identity Certificate.
3. Download the generated certificate and install it into Keychain Access on the Mac where you created the CSR to create your Merchant Identity (`.p12`). If you generated the CSR outside macOS, store the certificate and private key on that host.

You can also generate a CSR and private key on Linux or server environments using OpenSSL. Creating a CSR always produces a corresponding private key. Store both the certificate and its private key securely so you can export a PKCS #12 (`.p12`) archive or stacked PEM (`.pem`) file containing both items. Your server-side application presents this digital identity during Transport Layer Security (TLS) client authentication when contacting Apple Pay validation endpoints. To learn more about creating Merchant ID Certificates, see [Identity certificates](./tn3206-updating-apple-pay-certificates.md#Identity-certificates).

### Registering a merchant domain

Register each web domain that will initiate Apple Pay transactions under your Merchant ID. For example, if you process payments on both `example.com` and `test.example.com`, register and verify each domain individually.

Always register the fully qualified domain name (FQDN). If your customers access your storefront at `www.example.com`, register `www.example.com` in addition to or instead of the apex domain `example.com`.

## Domain verification

After adding a domain in Certificates, Identifiers & Profiles, Apple prompts you to verify ownership using a domain association file named `apple-developer-merchantid-domain-association.txt`.

Download the file and host it at the standard `.well-known` path on your server:

```text
https://example.com/.well-known/apple-developer-merchantid-domain-association.txt
```

Serve this file over HTTPS from the root of the registered domain.

> ❗ **Important**: The domain association file expires 7 days after generation. If you do not complete verification within 7 days, generate and host a new file before attempting verification again.

In Certificates, Identifiers & Profiles, click Verify next to the registered domain. Once Apple verifies the file, the domain status changes to Verified. If verification fails, inspect the common network and TLS failure points described below.

## Common reasons domain verification fails

Domain verification issues typically stem from TLS misconfigurations, firewall restrictions, or intermediary proxies.

### TLS handshake cannot be established

Apple’s domain verification client establishes a strict TLS connection to your server to retrieve the association file. A handshake failure occurs if your server exhibits any of the following issues:

- The server does not support TLS 1.2 or later.
- The server does not negotiate an Apple Pay-supported cipher suite.
- The server presents an untrusted, expired, or malformed TLS certificate.

#### Supporting TLS 1.2 or later

Servers hosting the domain association file must support TLS 1.2 or later. The server must be publicly reachable over the internet and must not terminate client connections at an unauthenticated forward proxy.

#### Validating usage of a TLS cipher suite

Your web server must negotiate one of the supported cipher suites specified in [Setting up your server](https://developer.apple.com/documentation/apple_pay_on_the_web/setting_up_your_server).

To diagnose cipher suite negotiation issues, capture a packet trace of the verification request. Inspect the `Client Hello` packet sent by Apple’s verification client to view offered cipher suites, and verify that your server responds in the `Server Hello` packet with a supported cipher suite. If your server rejects all offered suites, the TLS handshake terminates immediately after the `Client Hello`.

#### Validating TLS certificates

Verify that your web server presents a valid leaf certificate issued by a trusted public certificate authority (CA), along with the necessary intermediate certificates to complete the chain of trust to a trusted root CA. The certificate must also comply with [Apple’s Certificate Transparency policy](https://support.apple.com/en-us/103214).

### The Apple Developer Portal cannot reach your server

If the developer portal reports a verification failure without specific TLS error details, examine your web server’s access and error logs:

1. Confirm whether the incoming verification request reaches your server. If the request does not appear in your access logs, network routing or firewall rules are blocking Apple’s verification client.
2. If the request reaches your server, check the returned HTTP status code. The file must return an HTTP `200 OK` response with the unmodified file contents. Redirects (such as HTTP `301` or `302`) and authentication challenges (HTTP `401` or `403`) cause verification to fail.

### Your domain sits behind a proxy or in a private network

Ensure your verification endpoint is directly reachable and properly routed:

- **Proxies:** Avoid placing your verification endpoint behind TLS-terminating proxies or deep-packet-inspection firewalls. Apple’s verification client examines your server’s leaf TLS certificate directly; an intermediate proxy presents its own certificate, which causes verification to fail.
- **Load balancers:** If your server sits behind a load balancer, confirm that its health checks and routing rules forward requests for `/.well-known/apple-developer-merchantid-domain-association.txt` to active backend nodes capable of serving the file.
- **Firewalls and private networks:** If your server restricts incoming traffic by IP address, allowlist Apple’s domain verification IP address ranges. See the official IP ranges listed in [Setting up your server](../ApplePayontheWeb/setting-up-your-server.md#Allow-Apple-IP-Addresses-for-Domain-Verification).

## Building your client application

Build client-side checkout flows using either [Apple Pay JS](https://developer.apple.com/documentation/apple_pay_on_the_web/apple_pay_js_api) or the [Payment Request API](https://developer.apple.com/documentation/apple_pay_on_the_web/payment_request_api). This guide illustrates workflows using Apple Pay JS.

Before displaying an Apple Pay button or requesting a transaction, confirm that the client browser and hardware support Apple Pay. For implementation details, see [Checking for Apple Pay availability](https://developer.apple.com/documentation/apple_pay_on_the_web/apple_pay_js_api/checking_for_apple_pay_availability). For a runnable end-to-step demonstration, see the [Apple Pay on the Web Interactive Demo](https://applepaydemo.apple.com).

### Creating a payment request

When constructing an `ApplePayPaymentRequest`, provide only the parameters required for your transaction:

```json
{
    "countryCode": "US",
    "currencyCode": "USD",
    "merchantCapabilities": [
        "supports3DS"
    ],
    "supportedNetworks": [
        "visa",
        "masterCard",
        "amex",
        "discover"
    ],
    "total": {
        "label": "Demo (Card is not charged)",
        "type": "final",
        "amount": "1.99"
    }
}
```

If you calculate shipping costs dynamically based on the customer’s address, specify `requiredShippingContactFields` in your payment request:

```json
"requiredShippingContactFields": [
    "postalAddress",
    "name",
    "phone",
    "email"
]
```

When the user selects or changes their shipping address, Apple Pay triggers the `onshippingcontactselected` delegate callback with redacted address information sufficient to calculate taxes and shipping methods:

```javascript
// Sample redacted contact information received in onshippingcontactselected
{
    "administrativeArea": "CA",
    "country": "United States",
    "countryCode": "US",
    "locality": "San Francisco",
    "postalCode": "94114"
}

// Return updated line items and total to complete contact selection
session.onshippingcontactselected = event => {
    const update = {
        newTotal: {
            label: "Demo Store",
            type: "final",
            amount: "2.49"
        },
        newLineItems: [
            {
                label: "Subtotal",
                amount: "1.99"
            },
            {
                label: "Standard Shipping",
                amount: "0.50"
            }
        ]
    };
    // Pass the populated update object to complete contact selection; do not pass an empty object
    session.completeShippingContactSelection(update);
};
```

After the user authorizes the payment with Face ID, Touch ID, or their passcode, the session returns the unredacted shipping and contact details.

## Merchant validation

Before presenting the payment sheet to authorize a charge, your application must complete [merchant validation](https://developer.apple.com/documentation/apple_pay_on_the_web/apple_pay_js_api/providing_merchant_validation) to verify that your website is authorized to process transactions under your Merchant ID. Upon successful validation, Apple’s servers return an opaque payment session object that your client passes to the `ApplePaySession`.

Merchant validation follows three sequential steps:

1. **Client receives validation URL:** When the payment sheet initializes, `ApplePaySession` invokes its `onvalidatemerchant` callback, supplying an Apple-hosted `validationURL`. Your client-side JavaScript sends this URL to your backend server in an HTTPS request.
2. **Server requests payment session:** Your backend server sends an HTTP POST request to the provided `validationURL`, presenting your Merchant Identity Certificate (`.p12` or `.pem`) to perform mutual TLS (mTLS) client authentication. Validate the hostname against Apple’s allowed domains specified in [Setting up your server](https://developer.apple.com/documentation/apple_pay_on_the_web/setting_up_your_server).
3. **Client completes validation:** Apple’s server validates your certificate and returns an encrypted merchant session payload. Your backend forwards this response to your client application, which passes it to `session.completeMerchantValidation(paymentSession)`.

> ❗ **Important**: Never send the merchant validation request directly from client-side JavaScript. Contacting the validation endpoint requires your Merchant Identity private key; initiating this request from a browser exposes your private key.

### Testing merchant validation with curl

To verify that your Merchant Identity Certificate and network routing are functioning independently of your backend application code, test the payment session request directly using `curl`.

Export your Merchant Identity Certificate and private key from Keychain Access as a `.p12` file, and convert it to a decrypted PEM file:

```zsh
openssl pkcs12 -in Certificates.p12 -out apple-pay-cert.pem -nodes -clcerts
```

Execute a POST request to the validation endpoint with your client certificate:

```zsh
curl -gv \
  --cert /path/to/pem/apple-pay-cert.pem \
  --data '{
    "merchantIdentifier": "merchant.com.testbed.applepay",
    "initiativeContext": "example.com",
    "initiative": "web",
    "displayName": "Apple Pay Testbed"
  }' \
  https://apple-pay-gateway.apple.com/paymentservices/paymentSession
```

Use the production gateway host (`apple-pay-gateway.apple.com`) for live merchant accounts. To test in the sandbox environment, send the request to the sandbox gateway host (`apple-pay-gateway.sandbox.apple.com`). Use sandbox hosts only for development and sandbox testing; never use them in production. For regional endpoints, including gateway hosts in China, see [Setting up your server](https://developer.apple.com/documentation/apple_pay_on_the_web/setting_up_your_server).

A successful validation returns an HTTP `200 OK` response containing a JSON merchant session object.

### Payment services exception

If the Apple Pay server returns an HTTP `400 Bad Request` with a `Payment Services Exception`, the Merchant ID in the request body does not match the merchant identity bound to your client certificate:

```json
{
  "statusMessage": "Payment Services Exception merchantId=bdb3ed0005c72b1e8c2a536bb65a0ec22de030578c08b45dde6cdc13cd925f03 unauthorized to process transactions on behalf of merchantId=12953b72a8db15cf4a079b49a87ddd5eed1b0ba2eb249c7907265a7b04cff6ce reason=\"12953b72a8db15cf4a079b49a87ddd5eed1b0ba2eb249c7907265a7b04cff6ce never authorized mass enablement transactions to occur via bdb3ed0005c72b1e8c2a536bb65a0ec22de030578c08b45dde6cdc13cd925f03\"",
  "statusCode": "400"
}
```

The error message contains the SHA-256 hashes of two Merchant IDs:

1. The first hash (`bdb3ed00...`) corresponds to the Merchant ID associated with the Merchant Identity Certificate used for TLS client authentication.
2. The second hash (`12953b72...`) corresponds to the string passed in the `merchantIdentifier` field of your JSON request payload.

To identify which Merchant ID generated a hash, compute the SHA-256 digest of your Merchant ID string in Terminal:

```zsh
echo -n "merchant.com.testbed.applepay" | shasum -a 256
# 12953b72a8db15cf4a079b49a87ddd5eed1b0ba2eb249c7907265a7b04cff6ce
```

If the two hashes differ, the client certificate you installed belongs to a different Merchant ID than the one specified in your JSON payload. Re-export the certificate created under the correct Merchant ID, or update the `merchantIdentifier` field in your payload to match.

### completeMerchantValidation fails

If passing the payment session into `completeMerchantValidation(_:)` fails on the client, investigate these potential causes:

1. **Sandbox and production environment mismatch:** Do not mix sandbox and production configurations. If you request a payment session from the sandbox gateway, test on a device signed into an active [Apple Pay Sandbox Tester Account](https://developer.apple.com/apple-pay/sandbox-testing/) with sandbox test cards.
2. **Domain mismatch in initiativeContext:** The `initiativeContext` value in your payment session request must exactly match the FQDN of the website hosting the checkout page. For example, if testing on `www.example.com`, do not pass `staging.example.com` or `example.com`.
3. **Invalid merchant session signature:** A merchant session contains a cryptographic signature generated by Apple Pay servers. If your Merchant Identity Certificate is expired, revoked, or untrusted, the client rejects the session.
4. **Biometric or device authorization:** Ensure the test device supports Apple Pay and can authenticate using Face ID, Touch ID, or Optic ID.

To inspect detailed merchant session validation errors on macOS Safari, stream log messages from `passd` and PassKit in Terminal:

```zsh
log stream --level debug --predicate 'process == "passd" || subsystem == "com.apple.passkit"'
```

Reproduce the validation failure in Safari. If the merchant session is invalid, the log output indicates the specific failure:

```log
com.apple.PassKit.PaymentAuthorizationUIExtension: (PassKitCore) [com.apple.passkit:Payment] 
Evaluating merchant session using PROD trust policy.

com.apple.PassKit.PaymentAuthorizationUIExtension: (PassKitCore) [com.apple.passkit:Payment] 
Application failed to provide a valid merchant session. We can't proceed to authorize the transaction.
```

## Decrypting the payment token

After the user authorizes the transaction, `ApplePaySession` returns an `ApplePayPayment` object containing the encrypted `ApplePayPaymentToken`. Send this token payload to your payment processor for decryption and settlement.

Your payment processor uses your Payment Processing Identity (the private key corresponding to the public key in your Payment Processing Certificate) to decrypt the payment token.

If token decryption fails or produces unparsable data rather than JSON, verify that your processor holds the correct private key:

- When Apple Pay encrypts the payment token, it uses the public key from the active Payment Processing Certificate associated with your Merchant ID.
- The private key used for decryption must match that public key. If you recently renewed or regenerated your Payment Processing Certificate, confirm that your payment processor updated their system with the new private key.
- To verify key consistency, extract the public key from the private key file and compute its SHA-256 hash. Compare this hash against the public key extracted from your Payment Processing Certificate. If the hashes differ, the private key does not match the certificate.

For detailed token schema definitions and cryptographic specifications, see [Payment Token Format Reference](https://developer.apple.com/library/archive/documentation/PassKit/Reference/PaymentTokenJSON/PaymentTokenJSON.html). To learn more about Payment Processing Certificates, see doc://tn3206-updating-apple-pay-certificates#Payment-processing-certificates.

## Revision History

- **2026-11-03** Added sandbox gateway hosts and made editorial changes.
- **2022-05-24** Made minor editorial changes.
- **2022-03-29** Made minor editorial changes.
- **2022-02-08** Republished as TN3103.
- **2021-09-13** First published as “Apple Pay on the Web Debugging Guide” on the Apple Developer Forums.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3103-apple-pay-on-the-web-troubleshooting-guide)*