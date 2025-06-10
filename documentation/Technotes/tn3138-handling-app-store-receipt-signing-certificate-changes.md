# TN3138: Handling App Store receipt signing certificate changes

**Framework**: Technotes

Ensure that your app’s local receipt validation is compatible with intermediate certificates that require using the SHA-256 algorithm.

#### Overview

As part of ongoing efforts to improve security and privacy on Apple platforms, Apple is updating the App Store receipt signing intermediate certificate with one that uses the SHA-256 algorithm. This change affects the sandbox, TestFlight, and App Store environments, on the dates shown below:

| Date | Sandbox | TestFlight | App Store |
| --- | --- | --- | --- |
| January 24, 2025 | Uses SHA-256 certificate; SHA-1 certificate expires | Uses SHA-256 certificate; SHA-1 certificate expires | Uses SHA-256 certificate; SHA-1 certificate expires |
| August 16, 2023 |  | Uses SHA-256 certificate | Uses SHA-256 certificate |
| June 20, 2023 | Uses SHA-256 certificate |  |  |

The App Store receipt signing intermediate certificate is in the certificate chain that Apple uses to sign App Store receipts, which are the proof-of-purchase for apps and in-app purchases.

> ❗ **Important**: If your app verifies App Store receipts on the device, follow the instructions outlined in this document to ensure that your receipt validation code is compatible with this change.

If your app performs on-device receipt validation, it needs to support SHA-256 algorithm to correctly verify Apple’s certificate chain. For more information, see [`Validating receipts on the device`](https://developer.apple.comhttps://developer.apple.com/documentation/appstorereceipts/validating_receipts_on_the_device).

Starting January 24, 2025, apps that perform on-device receipt validation and don’t support a SHA-256 algorithm will fail their on-device receipt validation when the App Store updates the receipt. If your app prevents customers from accessing the app or premium content when receipt validation fails, your customers may lose access to their content.

Update your app to support certificates that use the SHA-256 algorithm if your app performs on-device receipt validation.

#### Determine If Your App Is Affected

Apps that are affected by Apple’s certificate update to SHA-256 include those that do the following:

- Perform on-device receipt validation, as described in [`Validating receipts on the device`](https://developer.apple.comhttps://developer.apple.com/documentation/appstorereceipts/validating_receipts_on_the_device), and
- Use code to verify the chain of trust that doesn’t support the SHA-256 algorithm or relies on an expectation that the certificate encryption uses only SHA-1.

The certificate update does not affect any of the following transaction or receipt validation methods:

- Validating app and in-app purchase transactions using [`AppTransaction`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/apptransaction) and [`Transaction`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction).
- Server-to-server receipt verification using the [`verifyReceipt`](https://developer.apple.comhttps://developer.apple.com/documentation/appstorereceipts/verifyreceipt/) endpoint. For more information, see [`Validating receipts with the App Store`](https://developer.apple.comhttps://developer.apple.com/documentation/appstorereceipts/validating_receipts_with_the_app_store).

> **Note**: The [`verifyReceipt`](https://developer.apple.comhttps://developer.apple.com/documentation/appstorereceipts/verifyreceipt/) endpoint is deprecated. To validate receipts on your server, follow the steps in [`Validating receipts on the device`](https://developer.apple.comhttps://developer.apple.com/documentation/appstorereceipts/validating_receipts_on_the_device) on your server.

#### Update Your App to Support Sha 256 Certificates

Follow these guidelines to update your app to support certificates that use the SHA-256 algorithm for on-device receipt validation:

1. If your app follows the instructions in [`Validating receipts on the device`](https://developer.apple.comhttps://developer.apple.com/documentation/appstorereceipts/validating_receipts_on_the_device), the new certificate affects step 2, which involves verifying the certificate chain. Be sure your app uses the latest certificates from [`Apple PKI`](https://developer.apple.comhttps://www.apple.com/certificateauthority).
2. Use cryptography code that supports SHA-256 algorithm. If you wrote your own code to verify receipts, update that code to use the SHA-256 algorithm. If your app uses a cryptography library, update the library to the latest version that supports SHA-256 algorithm.
3. Test your app in the sandbox environment to ensure that your on-device receipt validation succeeds.

#### Test Your App Receipt Validation in the Sandbox Environment

Starting June 20, 2023, the sandbox environment produces app receipts that are signed using the SHA-256 intermediate certificate for apps running in iOS 16.6, tvOS 16.6, watchOS 9.6, and macOS 13.5. Follow these steps to test how your app handles the receipts:

1. On a test device, sign in to the App Store with your Sandbox Apple ID.
2. Launch the app.
3. Perform one or more actions that cause the App Store to send an updated receipt to your app, such as the following: - Make an in-app purchase
- Call [`SKReceiptRefreshRequest`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/skreceiptrefreshrequest)
- Call [`restoreCompletedTransactions()`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/skpaymentqueue/1506123-restorecompletedtransactions) or [`restoreCompletedTransactions(withApplicationUsername:)`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/skpaymentqueue/1505992-restorecompletedtransactions).
4. Verify that Apple signed the receipt with a SHA-256 certificate. Decode your app receipt as a PKCS #7 container, then confirm that the `Receipt Creation Date` string, identified as [`ASN.1 Field Type 12`](https://developer.apple.comhttps://developer.apple.com/library/archive/releasenotes/General/ValidateAppStoreReceipt/Chapters/ReceiptFields.html#//apple_ref/doc/uid/TP40010573-CH106-SW22), is set to June 20, 2023 or later in the sandbox environment. (In the production environment, that date is August 16, 2023 or later.)
5. Ensure that your app calls its on-device receipt validation code with the new receipt.
6. Check that your on-device receipt validation succeeds.

If your app successfully verifies the receipt and you’ve confirmed that the new receipt uses the updated certificate in its certificate chain, your app is ready for Apple’s SHA-256 intermediate certificate update.

> **Note**: The receipt field [`SHA-1 Hash ASN.1 Field Type 5`](https://developer.apple.comhttps://developer.apple.com/library/archive/releasenotes/General/ValidateAppStoreReceipt/Chapters/ReceiptFields.html#//apple_ref/doc/uid/TP40010573-CH106-SW7) is not affected by the certificate update. Use that field as described in step 5 of [`Validate the receipt`](https://developer.apple.comhttps://developer.apple.com/documentation/appstorereceipts/validating_receipts_on_the_device#3744732).

#### Revision History

-  Added the SHA-1 expiry date. Noted that the `verifyReceipt` endpoint is now deprecated. Made other minor editorial changes.
-  Updated date timeline.
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

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3138-handling-app-store-receipt-signing-certificate-changes)*