# TN3174: Diagnosing issues with the Apple Pay payment sheet on your website

**Framework**: Technotes

Diagnose errors received while presenting the Apple Pay payment sheet on your website by identifying the underlying causes of common errors and explore their potential solutions.

#### Overview

When the Apple Pay payment sheet is presented, a number of JavaScript events are triggered before the payment sheet is activated and ready for the customer to authenticate. Additionally, some events are triggered when the customer interacts with the payment sheet, such as changing their selected payment card with [`onpaymentmethodselected`](https://developer.apple.comhttps://developer.apple.com/documentation/apple_pay_on_the_web/applepaysession/1778013-onpaymentmethodselected), or authorizing the transaction via user authentication with [`onpaymentauthorized`](https://developer.apple.comhttps://developer.apple.com/documentation/apple_pay_on_the_web/applepaysession/1778020-onpaymentauthorized).

The sequence of events depends on the configuration of the Apple Pay payment request. For example, including [`requiredShippingContactFields`](https://developer.apple.comhttps://developer.apple.com/documentation/apple_pay_on_the_web/applepaypaymentrequest/2216121-requiredshippingcontactfields) values may invoke the [`onshippingcontactselected`](https://developer.apple.comhttps://developer.apple.com/documentation/apple_pay_on_the_web/applepaysession/1778009-onshippingcontactselected) event. For more information, see [`Getting started with Apple Pay on the Web`](https://developer.apple.comhttps://developer.apple.com/videos/play/tech-talks/111381/).

For payments, the [`onvalidatemerchant`](https://developer.apple.comhttps://developer.apple.com/documentation/apple_pay_on_the_web/applepaysession/1778021-onvalidatemerchant), `onpaymentmethodselected`, and `onpaymentauthorized` event handlers are always invoked, so you must implement these methods and complete the events successfully with [`completeMerchantValidation`](https://developer.apple.comhttps://developer.apple.com/documentation/apple_pay_on_the_web/applepaysession/1778015-completemerchantvalidation), [`completePaymentMethodSelection`](https://developer.apple.comhttps://developer.apple.com/documentation/apple_pay_on_the_web/applepaysession/1777995-completepaymentmethodselection) and [`completePayment`](https://developer.apple.comhttps://developer.apple.com/documentation/apple_pay_on_the_web/applepaysession/1778012-completepayment), respectively. However, most other events are optional and may be implemented as needed.

Some common payment sheet-related issues that you may encounter during your Apple Pay implementation include:

- “Apple Pay not available for this website” errors
- “Payment Failed” errors
- Payment sheet is unexpectedly dismissed

> ❗ **Important**:  Starting October 1, 2026, cross-environment sessions are no longer be supported. If you experience payment issues after this date, see [`Possible reasons why the payment sheet dismisses after customer authentication`](tn3174-diagnosing-issues-with-the-apple-pay-payment-sheet-on-your-website#Possible-reasons-why-the-payment-sheet-dismisses-after-customer-authentication.md) for further information.

#### Possible Reasons for Apple Pay Not Available for This Website Errors

An “Apple Pay not available for this website” error can occur while presenting the payment sheet, most commonly for an invalid [`merchantIdentifier`](https://developer.apple.comhttps://developer.apple.com/documentation/apple_pay_on_the_web/applepayrequest/2951611-merchantidentifier). To ensure your developer account is configured correctly, please go to [`Certificates, Identifiers & Profiles`](https://developer.apple.comhttps://developer.apple.com/account/resources) and confirm the following:

- The `merchantIdentifier` provided to your payment session request matches an existing Merchant ID [`registered`](https://developer.apple.comhttps://developer.apple.com/help/account/configure-app-capabilities/configure-apple-pay#create-a-merchant-identifier) to your developer account.
- The `merchantIdentifier` also has an active [`payment processing certificate`](https://developer.apple.comhttps://developer.apple.com/help/account/configure-app-capabilities/configure-apple-pay#create-a-payment-processing-certificate) and [`merchant identity certificate`](https://developer.apple.comhttps://developer.apple.com/help/account/configure-app-capabilities/configure-apple-pay-on-the-web#create-a-merchant-identity-certificate).
- The domain provided to the payload of the `/startSession` or `/paymentSession` endpoints match the domain shown in your web browser’s address bar.

> **Note**: The `/startSession` endpoint is being phased out and replaced by `/paymentSession`. See [`Requesting an Apple Pay Payment Session`](https://developer.apple.comhttps://developer.apple.com/documentation/apple_pay_on_the_web/apple_pay_js_api/requesting_an_apple_pay_payment_session) for more information.

#### Possible Reasons for Payment Failed Errors

A “Payment Failed” error can occur while presenting the payment sheet, the most common reasons include:

- Invalid server configurations
- Invalid payment session request formatting
- Merchant validation issues

##### Troubleshooting Invalid Server Configurations

An invalid server configuration can cause several issues with your Apple Pay implementation, mostly due to the lack of security, trust and verification of your server’s authenticity via a mutual TLS connection. The most common issues with your server include:

- TLS handshake can’t be established.
- The server doesn’t support TLS 1.2 or later.
- The server uses unsupported TLS cipher suites.
- The server uses invalid or untrusted TLS certificates.

###### Issue Tls Handshake Cant Be Established

A TLS handshake can fail during the domain verification process. For example, your server may be misconfigured in the following ways:

- The server does not support TLS 1.2 or later.
- The server does not support one of the specified cipher suites for Apple Pay.
- The server is using invalid or untrusted TLS certificates.

###### Issue Your Server Doesnt Support Tls 12 or Later

Servers supporting Apple Pay on the Web need to use TLS 1.2 or later. Servers also need to be accessible by the Apple Pay merchant verification server and can’t be proxied or redirected. For additional guidance on using a strict allow list for Apple Pay IP addresses and merchant validation domains, see [`Setting up your Server`](https://developer.apple.comhttps://developer.apple.com/documentation/apple_pay_on_the_web/setting_up_your_server).

###### Issue Use of Unsupported Tls Cipher Suites

Servers negotiating TLS connections for Apple Pay on the Web must use one of the supported cipher suites described in [`Setting up your Server`](https://developer.apple.comhttps://developer.apple.com/documentation/apple_pay_on_the_web/setting_up_your_server). To debug which cipher suites are being negotiated between Apple’s domain verification client and your server, [`record a packet trace`](https://developer.apple.comhttps://developer.apple.com/documentation/network/recording_a_packet_trace) and review the cipher suites being offered by Apple’s domain verification server in the Client Hello packet. If a supported cipher suite is selected by your server, confirm this by reviewing the Server Hello packet sent back to the client. If there is an issue in the cipher suite negotiation then there will typically be a failure after the Client Hello packet.

###### Issue Use of Invalid or Untrusted Tls Certificates

Ensure you are using a valid TLS certificate. For example, make sure that this certificate is set up with a proper chain of trust and also adheres to Apple’s Certificate Transparency policy for Safari. You can double check this with a packet trace. Make sure the leaf certificate being used on your domain follows a valid chain of trust through the intermediate certificates to the root certificate. For additional guidance, see [`Requesting an Apple Pay Payment Session`](https://developer.apple.comhttps://developer.apple.com/documentation/apple_pay_on_the_web/apple_pay_js_api/requesting_an_apple_pay_payment_session).

##### Troubleshooting Payment Session Request Formatting Issues

The following topics provide guidance on resolving issues when requesting a payment session from Apple’s servers. When you experience an error, check the contents of the response body as it may contain a status message to determine where the issue occurred.

###### Issue Unable to Establish a Secure Connection or Ssl Handshake Failure

This error typically indicates a merchant identity certificate issue. To resolve this error, please confirm the following:

- The payment session request: - Uses the `POST` method, not `GET`.
- Values don’t contain accidental whitespace or spelling mistakes.
- Uses the URL provided by the `validationURL` attribute.
- The `validationURL` attribute uses the `https://` scheme.
- The certificate is configured correctly.
- The correct certificate is used for the payment session, especially when managing multiple certificates.
- The correct private key is associated to the certificate.
- Your server is correctly configured. See [`Troubleshooting invalid server configurations`](tn3174-diagnosing-issues-with-the-apple-pay-payment-sheet-on-your-website#Troubleshooting-invalid-server-configurations.md).

To learn more about configuring a merchant identity certificate, see [`Configuring Your Environment`](https://developer.apple.comhttps://developer.apple.com/documentation/apple_pay_on_the_web/configuring_your_environment). Additionally, see [`Setting up your Server`](https://developer.apple.comhttps://developer.apple.com/documentation/apple_pay_on_the_web/setting_up_your_server) to verify your server configuration is valid.

###### Issue Received a Payment Session Response Error

**Error: 400 – Bad Request.** This error typically indicates a formatting issue. Review your request to ensure the request body isn’t empty and contains all required parameters.

**Error: 404 – Not Found.** When you begin the Apple Pay session, Apple responds with an `onvalidatemerchant` callback that includes a `validationURL`. This `validationURL` is the endpoint your server must use to validate itself and obtain a merchant session object. If you receive this error, make sure you are sending the payload to the exact URL provided in the `validationURL` field. Use a strict allow list for the merchant validation URLs. Send the payment session request from your server; never request the session from the client.

**Error: 417 – Expectation Failed.** The merchant ID is either not registered for Apple Pay service or not registered for the domain. If you receive this error, navigate to your Apple Developer account and confirm the following:

- You are passing the correct merchant ID, which is associated to the merchant identity certificate, within the request.
- There are both: - A fully configured payment processing certificate; and
- A merchant identity certificate associated with the merchant ID.
- Your domain is registered and completed merchant domain verification successfully.
- The `initiativeContext` value is identical to the domain registered for your Apple Developer account.

Ensure the value provided in the `initiativeContext` request parameter is identical to the merchant ID registered for your Apple Developer account. If you have multiple merchant IDs, ensure the domain is registered to the same merchant ID associated with the merchant identity certificate used to secure the request.

The `initiativeContext` value should include subdomains, but shouldn’t contain the URL scheme (e.g. `https://`) or any paths. For example:

- **Valid:** `"secure.example.com"`
- **Invalid:** `"https://secure.example.com/request-session"`

If you plan to process payments on a root domain and subdomain—for example, `example.com` and `test.example.com`—register and verify each domain.

> **Note**: Apple considers `www.` a subdomain, so if you plan to process payments for `example.com`, but customers can access your site at `www.example.com`, you may need to ensure you register and verify both domains.

**Error 500 – Internal Server Error.** This error indicates the request couldn’t be processed, or the request body is malformed or invalid. Please ensure your request body is a valid JSON.

##### Troubleshooting Merchant Validation Issues

The following topics provide guidance on resolving issues when debugging Apple Pay merchant validation. The most common merchant validation issues occur during your payment session, including:

- Mishandling of payment session merchant validation events.
- Requesting a payment session with invalid certificates or values.
- Failure to complete merchant validation on a payment session.

To learn more about validating sessions and your merchant payment requests, see [`Requesting an Apple Pay Payment Session`](https://developer.apple.comhttps://developer.apple.com/documentation/apple_pay_on_the_web/apple_pay_js_api/requesting_an_apple_pay_payment_session) for more information.

###### Issue Mishandling of Payment Session Merchant Validation Events

When the `onvalidatemerchant` event is triggered, your client-side code should ask your server to request an Apple Pay payment session from Apple over an mTLS connection.

The most common issues while handling merchant validation events occur when:

- You request an Apple Pay payment session from Apple.
- You invoke `completeMerchantValidation` after successfully receiving a payment session from Apple.

Please ensure your implementation is following the expected flows for these merchant validation events. For more information, see [`Providing Merchant Validation`](https://developer.apple.comhttps://developer.apple.com/documentation/apple_pay_on_the_web/apple_pay_js_api/providing_merchant_validation).

###### Issue Requesting a Payment Session with Invalid Certificates or Values

You should create a new Apple Pay payment session for each transaction for your merchant. Your server posts a request using a mutual TLS (mTLS) connection by calling the Apple Pay server’s `/paymentSession` endpoint. Please confirm the following are true for your payment session request:

- The merchant identity certificate — a TLS certificate associated with your merchant ID — is used to authenticate your requests.
- The `merchantIdentifier` request parameter matches the same merchant ID value.
- For Apple Pay on the Web, use `"web"` for the `initiative` parameter. For the `initiativeContext` parameter, provide your fully qualified domain name associated with your Merchant Identity Certificate.

In response to the `POST` request, your server receives an opaque Apple Pay session object. The session expires after five (5) minutes. For Apple Pay on the Web, you pass the session object to the completion method, `completeMerchantValidation`.

###### Issue Failure to Complete Merchant Validation

If you are able to successfully generate a payment session but encounter issues when you pass this session into `completeMerchantValidation`, this suggests one of a few potential issues:

- **The session data is not formatted as a JSON Object.** The `completeMerchantValidation` method does not support this data in string format; the data must be parsed as a JSON object before it can be successfully passed to the completion method.
- **The session data is incomplete or has been modified.** You should treat the payment session data you receive as *opaque* and should not modify or change any of its contents. The contents or format of this data can change periodically, so it’s better to mapping this data to a strongly-typed object while it is in transit through your server and passed to your client-side code.
- **The `initiativeContext` for the session does not match the browser domain or is not correctly formatted.** The value provided as the `initiativeContext` in the payment session request should exactly match the domain shown in the browser’s address bar. The `initiativeContext` value should include subdomains but should not contain the URL scheme (e.g. `https://`) or any paths.
- **You are mixing environments.** Ensure you are using the correct `merchantIdentifier` and `initiativeContext` for the environment you are requesting a payment session from (Sandbox or Production).

#### Possible Reasons Why the Payment Sheet Dismisses After Initial Presentation

When the Apple Pay payment sheet is presented but dismisses within a few seconds — for example, after the customer has clicked or tapped the Apple Pay button — typically one of the following issues has occurred:

- Merchant validation failed.
- At least one of the payment sheet event handler methods is implemented, but the equivalent completion method isn’t properly configured.

To determine if this payment sheet dismissal is due to a merchant validation failure, use [`Safari Web Inspector`](https://developer.apple.comhttps://webkit.org/web-inspector/enabling-web-inspector/) to log errors and objects when debugging merchant validation. Otherwise, please ensure the object passed to the event’s completion method is well-formed, contains valid data, and all required parameters.

For Apple Pay, each event handler has a thirty (30) second timeout. If the related completion method is not invoked within 30 seconds from the start of the event, the payment sheet will dismiss with an error. When the customer changes or updates fields on the payment sheet, their selections are shared through event handlers, allowing your website to respond to user input.

For example, for any of the customer-selected payment methods on the W3C `PaymentRequest` object — such as `shippingaddresschange` — when the browser calls one of these event handlers, you have 30 seconds to process the event and invoke the equivalent `updateWith` callback. Ensure any server requests to validate the shipping address occur within this 30-second period. For more information about using the W3C Payment Request API, see [`Setting up the payment request API to accept Apple Pay`](https://developer.apple.comhttps://developer.apple.com/documentation/apple_pay_on_the_web/payment_request_api/setting_up_the_payment_request_api_to_accept_apple_pay).

> ❗ **Important**:  For the `onpaymentauthorized` event, if your system takes longer than 30 seconds to process the payment, the customer may see the payment sheet dismiss with an error, even though you may eventually process the payment successfully.

If the payment sheet dismisses without user interaction, please confirm the following:

- Your event handler implementations invoke the equivalent completion method. Do not stub out any of these event handler or completion methods.
- Your event handler implementations don’t take longer than 30 seconds to execute. Check for any long-running operations in your client or server code that may prevent the completion methods from returning in a timely manner.
- Your event handler implementations aren’t triggering an exception, breakpoint, or error, preventing the equivalent completion methods invocation.
- The object provided to the completion handler is a well-formed and valid JSON object. Validate the structure outlined in the documentation for each event’s completion method. Additionally, ensure all required parameters are populated correctly.

Use Safari Web Inspector to identify which event handler completion method is related to an issue and then diagnose the underlying cause of the issue for that specific event, including both the event handler and completion method.

#### Possible Reasons Why the Payment Sheet Dismisses After Customer Authentication

The payment sheet presents and responds to user interaction successfully, but fails to display a successful payment confirmation (the “Done” checkmark) after customer authentication.

###### Issue the Payment Sheet Dismisses Before the Onpaymentauthorized Event Triggers

This typically indicates an issue generating the Apple Pay payment token. The most common cause is an environment mismatch, where you request an Apple Pay merchant session from one environment but complete it in a different environment.

When requesting a merchant session, use the [`validationURL`](https://developer.apple.comhttps://developer.apple.com/documentation/applepayontheweb/applepayvalidatemerchantevent/validationurl) parameter in the [`ApplePayValidateMerchantEvent`](https://developer.apple.comhttps://developer.apple.com/documentation/applepayontheweb/applepayvalidatemerchantevent) object that the `onvalidatemerchant` event provides, or set the endpoint manually. If you set the endpoint manually, you must ensure it matches the user’s device configuration to avoid an environment mismatch:

- **Sandbox environment:** If the user’s device is signed in with a [`Sandbox tester account`](https://developer.apple.comhttps://developer.apple.com/apple-pay/sandbox-testing/), request the session using the Sandbox merchant validation URL. Developers typically use Sandbox-configured devices only in the integration phase with non-production merchant environments.
- **Production environment:** If the device is signed in with a standard Apple Account, request the session using the Production [`merchant validation URL`](https://developer.apple.comhttps://developer.apple.com/documentation/applepayontheweb/requesting-an-apple-pay-payment-session). Most consumer devices use this configuration.

In almost all cases, your production website must use the production Apple Pay endpoint. If you manually set the endpoint and encounter payment failures after customer authentication, ensure you didn’t carry over your Apple Pay configuration from lower environments when deploying changes to your production environment.

See [`Requesting an Apple Pay Payment Session`](https://developer.apple.comhttps://developer.apple.com/documentation/apple_pay_on_the_web/apple_pay_js_api/requesting_an_apple_pay_payment_session) for information on merchant validation URLs.

###### Issue the Payment Sheet Dismisses After the Onpaymentauthorized Event Triggers

When the sheet dismisses after the `onpaymentauthorized` event fires, the issue usually relates to the completion method. Verify the following:

- **Timeout:** Ensure your code calls `completePayment` within the allotted 30-second period. If your server takes too long to process the payment, the payment sheet times out and dismisses, even though the transaction itself might eventually complete successfully.
- **Malformed response object:** Confirm the [`ApplePayPaymentAuthorizationResult`](https://developer.apple.comhttps://developer.apple.com/documentation/applepayontheweb/applepaypaymentauthorizationresult) dictionary you provide to `completePayment` is properly formatted and contains valid data.

#### Revision History

- **2026-07-10** Expanded possible reasons why the payment sheet dismisses after customer authentication.
- **2024-06-25** First published.

## See Also

- [TN3173: Troubleshooting issues with your Apple Pay merchant identifier configuration](tn3173-troubleshooting-issues-with-your-apple-pay-merchant-id-configuration.md)
  Diagnose errors due to invalid Apple Pay merchant identifier configurations by identifying the underlying causes of common errors and explore their potential solutions.
- [TN3175: Diagnosing issues with displaying the Apple Pay button on your website](tn3175-diagnosing-issues-with-displaying-the-apple-pay-button-on-your-website.md)
  Diagnose common errors received while displaying the Apple Pay button on your website by identifying the underlying causes, and explore potential solutions.
- [TN3176: Troubleshooting Apple Pay payment processing issues](tn3176-troubleshooting-apple-pay-payment-processing-issues.md)
  Diagnose errors that occur when processing Apple Pay payments, identify common causes, and explore potential solutions.
- [TN3206: Updating Apple Pay certificates](tn3206-updating-apple-pay-certificates.md)
  Learn how to create, manage, and rotate Apple Pay certificates to maintain uninterrupted payment processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3174-diagnosing-issues-with-the-apple-pay-payment-sheet-on-your-website)*