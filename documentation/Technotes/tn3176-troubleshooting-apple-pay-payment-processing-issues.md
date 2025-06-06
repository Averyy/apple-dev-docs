# TN3176: Troubleshooting Apple Pay payment processing issues

**Framework**: Technotes

Diagnose errors that occur when processing Apple Pay payments, identify common causes, and explore potential solutions.

#### Overview

This technote covers debugging common Apple Pay payment processing issues. When an Apple Pay payment is requested by your app or website, Apple sends an encrypted payment token to you to verify its signature, decrypt its payment data, and validate the transaction. Often, these payment processing issues are caused by an invalid [`payment processing certificate`](https://developer.apple.comhttps://developer.apple.com/help/account/configure-app-capabilities/configure-apple-pay#create-a-payment-processing-certificate), or by mishandling payment data by you or your payment service provider (PSP).

#### Possible Reasons for Payment Service Provider Errors While Handling the Apple Pay Payment Token

Payment token validation that fail for your PSP are often due to an issue with your payment processing certificate or the format of your token. In either case, your PSP may be able to provide additional insight.

Please confirm the following with your PSP:

- The merchant ID value used throughout Apple Pay must be identical to the one you created in your Apple Developer account. If it is different, Apple will not be able to to decrypt the payment data.
- The merchant ID is associated with the correct payment processing certificate.
- The payment processing certificate is in an active state in your Apple Developer account.
- The [`merchantCapabilities`](https://developer.apple.comhttps://developer.apple.com/documentation/apple_pay_on_the_web/applepaypaymentrequest/1916123-merchantcapabilities) array of the `ApplePayPaymentRequest`
contains only `supports3DS`.
- Your PSP is sending the authorization message in the format required by each payment network.

For more information about configuring your merchant identifier (ID) and certificates required for Apple Pay, see [`Configuring Your Environment`](https://developer.apple.comhttps://developer.apple.com/documentation/apple_pay_on_the_web/configuring_your_environment).

#### Possible Reasons for Payment Token Decryption Errors

You validate a transaction by verifying the signature, decrypting the payment data, and verifying additional transaction details. A payment token’s payment data is encrypted using either elliptic curve cryptography (ECC) or RSA encryption. The encryption algorith used is based on the merchant capabilities of the initial payment request. The payment token can be decrypted by the merchant with the certificate private key or by the PSP on behalf of the merchant. For China mainland, decrypt via RSA; otherwise decrypt via ECC.

If you experience payment token-related decryption issues, please confirm the following:

- The PSP routes the payment to the correct payment network.
- The tokenization of the payment data doesn’t take too long or hasn’t timed out.
- The decrypted data is a valid JSON object.
- You receive a parseable JSON output when you attempt to decrypt a payment token, indicating a possible a key mismatch.
- No payment with the same `transactionId` shows as processed, indicating a transaction you’ve already credited.
- The merchant ID that you share with PSP is identical to the one you created in your Apple Developer account.

For more information, see [`Payment token format reference`](https://developer.apple.comhttps://developer.apple.com/documentation/passkit_apple_pay_and_wallet/apple_pay/payment_token_format_reference).

#### Possible Reasons for Payment Token Processing Errors

Once decrypted, the payment token is passed to the PSP for processing. If you experience payment token-related processing issues, please confirm the following:

- The cryptogram format is valid. For example, the `merchantCapabilities` property includes `supports3DS` (as well as `supportsEMV`, if you support China Union Pay transactions).
- Your PSP has assigned the correct Electronic Commerce Indicator (ECI) values for the transcation.
- Your certificate signing request (CSR) Apple uses to encrypt the payment token was generated for the correct environment (sandbox or production). and not mismatched.
- You aren’t reusing a previously processed payment token. Cryptograms are single-use and cannot be used over multiple transactions.

#### Revision History

-  First published.

## See Also

- [TN3189: Managing Mail background traffic load](tn3189-managing-mail-background-traffic-load.md)
  Identify iOS Mail background traffic and manage its impact on your IMAP server.
- [TN3187: Migrating to the UIKit scene-based life cycle](tn3187-migrating-to-the-uikit-scene-based-life-cycle.md)
  Update your app to receive scene-based life-cycle events and manage your user interface using scene objects and methods.
- [TN3188: Troubleshooting In-App Purchases availability in the App Store](tn3188-troubleshooting-in-app-purchases-availability-in-the-app-store.md)
  Verify your In-App Purchases are approved and available for sale in the App Store.
- [TN3186: Troubleshooting In-App Purchases availability in the sandbox](tn3186-troubleshooting-in-app-purchases-availability-in-the-sandbox.md)
  Identify common configurations that make your In-App Purchases unavailable in the sandbox environment.
- [TN3185: Troubleshooting In-App Purchases availability in Xcode](tn3185-troubleshooting-in-app-purchases-availability-in-xcode.md)
  Inspect your active StoreKit configuration file for unexpected configurations.
- [TN3182: Adding privacy tracking keys to your privacy manifest](tn3182-adding-privacy-tracking-keys-to-your-privacy-manifest.md)
  Declare the tracking domains you use in your app or third-party SDK in a privacy manifest.
- [TN3183: Adding required reason API entries to your privacy manifest](tn3183-adding-required-reason-api-entries-to-your-privacy-manifest.md)
  Declare the APIs that can potentially fingerprint devices in your app or third-party SDK in a privacy manifest.
- [TN3184: Adding data collection details to your privacy manifest](tn3184-adding-data-collection-details-to-your-privacy-manifest.md)
  Declare the data your app or third-party SDK collects in a privacy manifest.
- [TN3181: Debugging an invalid privacy manifest](tn3181-debugging-invalid-privacy-manifest.md)
  Identify common configurations that cause unsuccessful privacy manifest validation with the App Store.
- [TN3180: Reverting to App Store Server Notifications V1](tn3180-reverting-app-store-server-notifications-v1.md)
  Migrate from version 2 to version 1 of App Store Server Notifications using the Modify an App endpoint.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
- [TN3178: Checking for and resolving build UUID problems](tn3178-checking-for-and-resolving-build-uuid-problems.md)
  Ensure that every Mach-O image has a UUID, and that every distinct Mach-O image has its own unique UUID.
- [TN3177: Understanding alternate audio track groups in movie files](tn3177-understanding-alternate-audio-track-groups-in-movie-files.md)
  Learn how alternate groups collect audio tracks, and how to choose which audio track to use in your app.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3175: Diagnosing issues with displaying the Apple Pay button on your website](tn3175-diagnosing-issues-with-displaying-the-apple-pay-button-on-your-website.md)
  Diagnose common errors received while displaying the Apple Pay button on your website by identifying the underlying causes, and explore potential solutions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3176-troubleshooting-apple-pay-payment-processing-issues)*