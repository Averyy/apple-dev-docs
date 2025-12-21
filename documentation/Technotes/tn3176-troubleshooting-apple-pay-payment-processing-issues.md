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

- [TN3190: USB audio device design considerations](tn3190-usb-audio-device-design-considerations.md)
  Learn the best techniques for designing devices that conform to the USB Audio Device Class specifications.
- [TN3194: Handling account deletions and revoking tokens for Sign in with Apple](tn3194-handling-account-deletions-and-revoking-tokens-for-sign-in-with-apple.md)
  Learn the best techniques for managing Sign in with Apple user sessions and responding to account deletion requests.
- [TN3193: Managing the on-device foundation model’s context window](tn3193-managing-the-on-device-foundation-model-s-context-window.md)
  Learn how to budget for the context window limit of Apple’s on-device foundation model and handle the error when reaching the limit.
- [TN3115: Bluetooth State Restoration app relaunch rules](tn3115-bluetooth-state-restoration-app-relaunch-rules.md)
  Learn about the conditions under which an iOS app will be relaunched by Bluetooth State Restoration.
- [TN3192: Migrating your iPad app from the deprecated UIRequiresFullScreen key](tn3192-migrating-your-app-from-the-deprecated-uirequiresfullscreen-key.md)
  Support iPad multitasking and dynamic resizing while updating your app to remove the deprecated full-screen compatibility mode.
- [TN3151: Choosing the right networking API](tn3151-choosing-the-right-networking-api.md)
  Learn which networking API is best for you.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3191: IMAP extensions supported by Mail for iOS, iPadOS, and visionOS](tn3191-imap-extensions-supported-by-mail.md)
  Learn which extensions to the RFC 3501 IMAP protocol are supported by Mail for iOS, iPadOS, and visionOS.
- [TN3134: Network Extension provider deployment](tn3134-network-extension-provider-deployment.md)
  Explore the platforms, packaging, OS versions, and device configurations for Network Extension provider deployment.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3176-troubleshooting-apple-pay-payment-processing-issues)*