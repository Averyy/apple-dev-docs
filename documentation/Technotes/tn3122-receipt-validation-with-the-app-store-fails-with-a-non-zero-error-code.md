# TN3122: Receipt validation with the App Store fails with a non-zero error code

**Framework**: Technotes

Identify common configurations that cause unsuccessful receipt validation with the App Store.

#### Overview

Receipt validation with the App Store requires that you send a JSON object with the `receipt-data` and `password` keys, and optionally the `exclude-old-transactions` key as detailed in [`requestBody`](https://developer.apple.comhttps://developer.apple.com/documentation/appstorereceipts/requestbody). The App Store responds with a value of `0` if validation was successful, and a [`status code`](https://developer.apple.comhttps://developer.apple.com/documentation/appstorereceipts/status) if validation failed. This document lists reasons for unsuccessful validations.

#### Encoding of the Receipt Data Failed

Validating the receipt with the App Store requires encoding the receipt data using Base64 in your app before sending it to your server. Use [`Data.base64EncodedString(options:)`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/data/2142853-base64encodedstring/) as detailed in [`Fetch the Receipt Data`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/original_api_for_in-app_purchase/validating_receipts_with_the_app_store) or a Base64 algorithm of your choosing to encode the receipt data. if you use a different Base64 algorithm, confirm that it successfully covers and encodes all possible characters in a receipt.

#### Shared Secret Is Invalid

In App Store Connect, you can generate or regenerate a primary shared secret for all of your apps, or an app-specific shared secret for each of your apps. When you regenerate the primary shared secret, you invalidate the previous shared secret for all of your apps that use it. Confirm that the `password` key is set to the latest value of the primary shared secret for all of your apps that use it. See [`Generate a shared secret`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/devf341c0f01) for details.

When you generate an app-specific shared secret for an app, that app can no longer use the primary shared secret. Confirm that `password` is set to the
latest value of the app-specific shared secret for this app. The app-specific shared secret becomes invalid for the app when you regenerate it.

#### Object Posted to the App Store Is Invalid

On your server, create and format an object as JSON. This JSON object is a dictionary that contains the `receipt-data` and `password` keys. Each key pair in the dictionary is separated by a comma.

```json
{
    "receipt-data": "your_Base64_encoded_receipt_data",
    "password": "your_shared_secret",
}
```

For receipts that contain auto-renewable subscriptions, optionally add `exclude-old-transactions` to the JSON object. The [`latest_receipt_info`](https://developer.apple.comhttps://developer.apple.com/documentation/appstorereceipts/responsebody/latest_receipt_info) key contains the most recent entry for any subscriptions when `exclude-old-transactions` is set to `true` and all renewal entries, otherwise.

```json
{
    "receipt-data": "your_Base64_encoded_receipt_data",
    "password": "your_shared_secret",
    "exclude-old-transactions": true
}
```

If `exclude-old-transactions` is absent in the JSON object, then the default value is `false`.

> ❗ **Important**: On your server, be sure to send your JSON object as the payload of an HTTP POST request for receipt validation with the App Store.

#### Validation Request Was Posted to the Incorrect Url

Use the sandbox URL to verify receipts when testing in the sandbox and while your app is in review:

```None
https://sandbox.itunes.apple.com/verifyReceipt
```

Use the production URL to verify receipts when your app is live in the App Store:

```None
https://buy.itunes.apple.com/verifyReceipt
```

First, verify your receipt with the production URL. If you receive a `21007` status code, as outlined in [`verifyReceipt`](https://developer.apple.comhttps://developer.apple.com/documentation/appstorereceipts/verifyreceipt), verify with the sandbox URL instead.

> **Note**: TestFlight uses the sandbox environment for in-app purchases. See [`Testing at All Stages of Development with Xcode and Sandbox`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/in-app_purchase/testing_at_all_stages_of_development_with_xcode_and_sandbox) for details.

#### Validate the Receipt Locally

Consider validating your receipt locally with the App Store to ensure your implementation works as designed. Use the `curl` command to test your JSON object.

To validate your receipt in the sandbox environment, run:

```json
% curl -d 
'{
    "receipt-data": "your_Base64_encoded_receipt_data",
    "password": "your_shared_secret"
 }' 
 https://sandbox.itunes.apple.com/verifyReceipt
```

To validate your receipt in the production environment, run:

```json
% curl -d 
'{
    "receipt-data": "your_Base64_encoded_receipt_data",
    "password": "your_shared_secret"
 }' 
 https://buy.itunes.apple.com/verifyReceipt
```

To validate your receipt in the production environment and limit the content of the `latest_receipt_info` key to only the most recent entry, run:

```json
% curl -d 
'{
    "receipt-data": "your_Base64_encoded_receipt_data",
    "password": "your_shared_secret",
    "exclude-old-transactions": true
 }' 
 https://buy.itunes.apple.com/verifyReceipt
```

#### Revision History

-  Made minor editorial changes.
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
- [TN3176: Troubleshooting Apple Pay payment processing issues](tn3176-troubleshooting-apple-pay-payment-processing-issues.md)
  Diagnose errors that occur when processing Apple Pay payments, identify common causes, and explore potential solutions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Technotes/tn3122-receipt-validation-with-the-app-store-fails-with-a-non-zero-error-code)*