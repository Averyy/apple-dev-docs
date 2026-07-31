# TN3206: Updating Apple Pay certificates

**Framework**: Technotes

Learn how to create, manage, and rotate Apple Pay certificates to maintain uninterrupted payment processing.

#### Overview

When you configure Apple Pay, you create a payment processing certificate to securely encrypt payment data. If you integrate Apple Pay on the Web, you also create an identity certificate to authenticate communication with Apple Pay servers. To get started with Apple Pay configuration, see [`Setting up Apple Pay`](https://developer.apple.com/documentation/PassKit/setting-up-apple-pay).

Both certificates are valid for 25 months and must be renewed before they expire to avoid disruptions to payment processing in your apps and websites. This document explains how to update—also referred to as rolling or rotating—your Apple Pay certificates with minimal disruption.

#### Apple Pay Credentials

| Credential | Description | Expiration |
| --- | --- | --- |
| Merchant Identifier | A unique identifier representing a merchant within Apple Pay. Can be associated with multiple apps and websites. See [`Create a merchant identifier`](https://developer.apple.comhttps://developer.apple.com/help/account/capabilities/configure-apple-pay#create-a-merchant-identifier) for the setup steps. | No |
| Payment Platform Integrator Identifier | A unique identifier representing a payment platform within Apple Pay. Used with [`Apple Pay Web Merchant Registration API`](https://developer.apple.com/documentation/ApplePayWebMerchantRegistrationAPI). | No |
| Payment Processing Certificate | Encrypts payment data. Apple Pay servers use the certificate’s public key to encrypt payment data; the corresponding private key is used to decrypt it. See [`Create a payment processing certificate`](https://developer.apple.com#Create-a-payment-processing-certificate) for the setup steps. | Yes; 25 months |
| Identity Certificate | A TLS certificate that authenticates requests with Apple Pay servers. Required for Apple Pay on the Web. Can be linked to either a Merchant Identifier or a Payment Platform Integrator Identifier. See [`Create an identity certificate`](https://developer.apple.com#Create-an-identity-certificate) for the setup steps. | Yes; 25 months |

#### Payment Processing Certificates

Merchant identifiers and payment platform integrator identifiers support one active payment processing certificate at a time. When you activate a new payment processing certificate, Apple Pay servers begin using it to encrypt transactions. Whilst the newly created payment processing certificate is propagated across Apple Pay servers, some transactions may temporarily still be encrypted with the previous certificate’s public key.

To handle this transition correctly, always check the `publicKeyHash` value in the payment token to determine which public key was used for encryption, then retrieve the corresponding private key from your keychain or keystore to decrypt the payment data. When the transition is complete, only the new public key will be used. For more information, see [`Payment token format reference`](https://developer.apple.com/documentation/PassKit/payment-token-format-reference).

> **Note**: If your Payment Service Provider (PSP) performs decryption on your behalf, follow your PSP’s guidance on the process required to coordinate successful certificate rolling in their platform.

**To update your payment processing certificate, follow the sections below:**

- Create a payment processing certificate
- Activate a payment processing certificate
- Use the public key’s hash to identify the correct private key
- Monitor and rotate your certificates

##### Create a Payment Processing Certificate

A payment processing certificate is associated with your merchant identifier or payment platform integrator identifier and encrypts payment information for Apple Pay. Decryption can be handled by the merchant directly or delegated to their PSP.

The decrypting party is responsible for generating the new keys and certificate signing request (CSR). They may also need the downloaded certificate after the enrollment process is complete.

To create a payment processing certificate, use the following resources:

- **Apple Developer Portal:** Use [`Certificates, Identifiers & Profiles`](https://developer.apple.comhttps://developer.apple.com/account/resources/identifiers/list).
- **App Store Connect API:** Use [`Create a certificate`](https://developer.apple.com/documentation/AppStoreConnectAPI/POST-v1-certificates) to create a certificate. For more information, see [`Managing merchant IDs and Payment Processing certificates`](https://developer.apple.com/documentation/AppStoreConnectAPI/managing-payment-processing-certificates).

When generating the CSR for payment processing, use the appropriate key type for your region:

| Region | Key Type |
| --- | --- |
| Global | 256-bit ECC key pair |
| China mainland | 2048-bit RSA key pair |

**To manually create and download a new payment processing certificate:**

1. In [`Certificates, Identifiers & Profiles`](https://developer.apple.comhttps://developer.apple.com/account/resources/identifiers/list), click Identifiers.
2. Under Identifiers, select Merchant IDs or Payment Platform Integrator IDs using the filter on the top right.
3. On the right, select your merchant identifier or payment platform integrator identifier. - ***Note:*** If a banner appears at the top of the page saying that you need to accept an agreement, click the Review Agreement button and follow the instructions before continuing.
4. Under Apple Pay Payment Processing Certificate, click Create Certificate.
5. The decrypting party should [`create a CSR`](https://developer.apple.comhttps://developer.apple.com/help/account/certificates/create-a-certificate-signing-request/). This can be done on a Mac using Keychain Access, or use a command-line tool such as OpenSSL or Java keytool.
6. Click Choose File.
7. In the dialog that appears, select your CSR file (`*.certSigningRequest`), then click Choose.
8. Click Continue.
9. Click Download to save the certificate file (`*.cer`).

##### Activate a Payment Processing Certificate

Apple Pay payment decryption can be handled by the merchant directly or delegated to a PSP. If your PSP handles decryption, coordinate with them before activing a new payment processing certificate. Both parties must be fully prepared to use the updated credentials before you proceed—activating prematurely can interrupt payment processing in your apps and websites.

**To manually activate a payment processing certificate:**

1. In [`Certificates, Identifiers & Profiles`](https://developer.apple.comhttps://developer.apple.com/account/resources/identifiers/list), navigate to your merchant identifier or payment platform integrator identifier.
2. Under Apple Pay Payment Processing Certificate, locate the new certificate.
3. Click Activate.

Once activated, Apple Pay servers immediately begin using the new certificate to encrypt transactions.

> ❗ **Important**: Payment processing certificate activation is irreversible. Once you activate a new certificate, the previous certificate is immediately invalidated and cannot be restored.

##### Use the Public Keys Hash to Identify the Correct Private Key

During the transition period after activation, Apple Pay servers may use either the previous or new public key to encrypt transactions as the update propagates. Use the `publicKeyHash` value in the payment token’s header to determine which private key to use for decryption.

Once you stop receiving the `publicKeyHash` value associated with the previous certificate, it’s safe to delete the previous private key from your keychain or keystore.

For more information on payment token structure and decryption, see [`Payment token format reference`](https://developer.apple.com/documentation/PassKit/payment-token-format-reference).

#### Identity Certificates

Merchant identifiers and payment platform integrator identifiers support up to three active identity certificates simultaneously. This allows you to create and validate a new certificate before revoking the previous one, ensuring uninterrupted connectivity with Apple Pay servers.

**To update your identity certificate, follow the sections below:**

- Create an identity certificate
- Monitor and rotate your certificates
- Revoke an identity certificate

##### Create an Identity Certificate

Identity certificates require a CSR generated using an RSA 2048-bit key pair.

**To manually create and download a new identity certificate:**

1. In [`Certificates, Identifiers & Profiles`](https://developer.apple.comhttps://developer.apple.com/account/resources/identifiers/list), click Identifiers.
2. Under Identifiers, select Merchant IDs or Payment Platform Integrator IDs using the filter on the top right.
3. On the right, select your merchant identifier or payment platform integrator identifier. - ***Note:*** If a banner appears at the top of the page saying that you need to accept an agreement, click the Review Agreement button and follow the instructions before continuing.
4. Under the identity certificate section, click Create Certificate. - ***Note:*** If the Create Certificate button is disabled, consider choosing an older, inactive certificate to revoke. Revoking an active certificate will immediately cause Apple Pay requests to fail.
5. [`create a CSR`](https://developer.apple.comhttps://developer.apple.com/help/account/certificates/create-a-certificate-signing-request/) on a Mac using Keychain Access, or use a command-line tool such as OpenSSL or Java keytool.
6. Click Choose File.
7. In the dialog that appears, select your CSR file (`*.certSigningRequest`), then click Choose.
8. Click Continue.
9. Click Download to save the certificate file (`*.cer`).

Once downloaded, add the new certificate to your keychain or keystore. It can be used immediately to secure connections to Apple Pay servers. After you’ve confirmed the new certificate works as expected in your environment, revoke and delete the previous certificate from both the [`Certificates, Identifiers & Profiles`](https://developer.apple.comhttps://developer.apple.com/account/resources/identifiers/list) and your keychain or keystore.

#### Monitor and Rotate Your Certificates

To view the status and expiration date of each certificate, use the following resources:

- **Apple Developer Portal:** Use [`Certificates, Identifiers & Profiles`](https://developer.apple.comhttps://developer.apple.com/account/resources/identifiers/list).
- **App Store Connect API:** Use [`List and download certificates`](https://developer.apple.com/documentation/AppStoreConnectAPI/GET-v1-certificates) to find and list certificates, or [`Read and download certificate information`](https://developer.apple.com/documentation/AppStoreConnectAPI/GET-v1-certificates-_id_) to retrieve details about a specific certificate.

> 💡 **Tip**: Proactively renew certificates at least 30 days before expiration. Apple sends expiration reminder notifications to Account Holder and Admin [`roles`](https://developer.apple.comhttps://developer.apple.com/help/account/access/roles/) 30, 15, and 7 days before a certificate expires. To ensure you receive all notifications, maintain up to date and accurate contact details for these roles.

Certificates can be rotated manually in the [`Certificates, Identifiers & Profiles`](https://developer.apple.comhttps://developer.apple.com/account/resources/identifiers/list) or programmatically using the [`Certificates`](https://developer.apple.com/documentation/AppStoreConnectAPI/certificates). To learn more about programmatically rotating payment processing certificates, see [`Managing merchant IDs and Payment Processing certificates`](https://developer.apple.com/documentation/AppStoreConnectAPI/managing-payment-processing-certificates).

##### Revoke an Identity Certificate

You can revoke certificates in the following resources:

- **Apple Developer Portal:** Use [`Certificates, Identifiers & Profiles`](https://developer.apple.comhttps://developer.apple.com/account/resources/identifiers/list).
- **App Store Connect API:** Use [`Revoke a certificate`](https://developer.apple.com/documentation/AppStoreConnectAPI/DELETE-v1-certificates-_id_) to revoke a specific certificate.

**To manually revoke an identity certificate:**

1. In [`Certificates, Identifiers & Profiles`](https://developer.apple.comhttps://developer.apple.com/account/resources/identifiers/list), click Identifiers.
2. Under Identifiers, select Merchant IDs or Payment Platform Integrator IDs using the filter on the top right.
3. On the right, select your merchant identifier or payment platform integrator identifier. - ***Note:*** If a banner appears at the top of the page saying that you need to accept an agreement, click the Review Agreement button and follow the instructions before continuing.
4. Under the identity certificate section, locate a certificate (preferably an inactive certificate) and click Revoke.

#### Frequently Asked Questions

**Does updating certificates affect my merchant domain verification?**

No. Merchant domain verification is unrelated to the certificate update process.

**If my PSP handles decryption, can certificate updates cause payment failures?**

Yes, if updates aren’t coordinated in advance. Before updating your payment processing certificate, follow your PSP’s guidance on the process required to coordinate successful certificate rolling in their platform. Your PSP must provide you with a CSR to generate the new certificate, which confirms they hold the correct private key to perform decryption.

**Do merchant identifiers or payment platform integrator identifiers expire?**

No. Merchant identifiers and payment platform integrator identifiers don’t expire. Only their associated certificates expire and require renewal every 25 months.

**When should I activate a new payment processing certificate?**

Click the Activate button in the [`Certificates, Identifiers & Profiles`](https://developer.apple.comhttps://developer.apple.com/account/resources/identifiers/list) when both you and your PSP have confirmed you’re ready to accept payments with the new credentials, and decrypt payloads using the updated private keys. Activation is immediate and irreversible.

**Can I revert to a previous payment processing certificate after activation?**

No. Activating a new certificate immediately invalidates the previous one. It cannot be reactivated or restored.

**What if my certificate expires during a scheduled code freeze?**

Renew your certificate before the code freeze begins so the new expiration date falls outside that time period. This ensures uninterrupted payment processing without requiring code changes during the scheduled code freeze.

**How far in advance should I renew my certificates?**

Renew your certificates at least 30 days before expiration to allow sufficient time for coordination with your PSP and validation in your environment before activation.

#### Revision History

- **2026-03-12** First published.

## See Also

- [TN3173: Troubleshooting issues with your Apple Pay merchant identifier configuration](tn3173-troubleshooting-issues-with-your-apple-pay-merchant-id-configuration.md)
  Diagnose errors due to invalid Apple Pay merchant identifier configurations by identifying the underlying causes of common errors and explore their potential solutions.
- [TN3174: Diagnosing issues with the Apple Pay payment sheet on your website](tn3174-diagnosing-issues-with-the-apple-pay-payment-sheet-on-your-website.md)
  Diagnose errors received while presenting the Apple Pay payment sheet on your website by identifying the underlying causes of common errors and explore their potential solutions.
- [TN3175: Diagnosing issues with displaying the Apple Pay button on your website](tn3175-diagnosing-issues-with-displaying-the-apple-pay-button-on-your-website.md)
  Diagnose common errors received while displaying the Apple Pay button on your website by identifying the underlying causes, and explore potential solutions.
- [TN3176: Troubleshooting Apple Pay payment processing issues](tn3176-troubleshooting-apple-pay-payment-processing-issues.md)
  Diagnose errors that occur when processing Apple Pay payments, identify common causes, and explore potential solutions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3206-updating-apple-pay-certificates)*