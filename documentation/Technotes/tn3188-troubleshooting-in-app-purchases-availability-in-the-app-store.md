# TN3188: Troubleshooting In-App Purchases availability in the App Store

**Framework**: Technotes

Verify your In-App Purchases are approved and available for sale in the App Store.

#### Overview

When launching your app in the App Store, the app may not display your In-App Purchases. To offer In-App Purchases in your app, call [`products(for:)`](https://developer.apple.com/documentation/StoreKit/Product/products(for:)) with a list of [`product identifiers`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/in-app-purchase-information) (`Product ID`) matching these products in App Store Connect. `Product.products(for:)` returns an array that includes an instance of [`Product`](https://developer.apple.com/documentation/StoreKit/Product) for each of the In-App Purchases. Update your app’s UI with these returned instances, which contain all In-App Purchase data configured in App Store Connect for your app.

If `Product.products(for:)` fails to return a `Product` instance for your In-App Purchases, it may be due to the following reasons:

- Your In-App Purchases are missing or don’t exist in the App Store.
- Your In-App Purchases exist in the App Store, but they are unapproved and unavailable.

> **Note**: If your app fails to display its products when testing In-App Purchases in Xcode or the Apple sandbox environment, see [`TN3185: Troubleshooting In-App Purchases availability in Xcode`](tn3185-troubleshooting-in-app-purchases-availability-in-xcode.md) and [`TN3186: Troubleshooting In-App Purchases availability in the sandbox`](tn3186-troubleshooting-in-app-purchases-availability-in-the-sandbox.md), respectively.

#### Validate Your Product Identifier List

To verify your product identifier list, perform these steps:

1. In your Xcode project, [`Preparing your app for distribution`](https://developer.apple.com/documentation/Xcode/preparing-your-app-for-distribution) your app’s [`CFBundleIdentifier`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleIdentifier).
2. In App Store Connect, find the app that matches your app’s bundle ID.
3. Verify each product identifier in your list matches the product identifier (`Product ID`) of an In-App Purchase created for the app in App Store Connect.

#### Review the Status of Your in App Purchases

In App Store Connect, submit your In-App Purchases for review. To submit an In-App Purchase for review, the In-App Purchase must have the [`Ready to Submit`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/in-app-purchase-statuses) status. If the In-App Purchase doesn’t have this status, [`complete any missing information`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-in-app-purchases/view-and-edit-in-app-purchase-information) such as price or localization for the subscription group display name. For more information about submitting In-App Purchases, see [`Submit for review`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-for-review).

After Apple completes review of your In-App Purchases, confirm that the status of each In-App Purchase you submitted is [`Ready to Submit`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/in-app-purchase-statuses). If App Store Connect shows [`Ready to Submit`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/in-app-purchase-statuses) or [`Ready to Submit`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/in-app-purchase-statuses) for an In-App Purchase, handle the status as described in the following table:

| Status | Perform action |
| --- | --- |
| Developer Action Needed | Update the In-App Purchase information. For more information, see [`complete any missing information`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-in-app-purchases/view-and-edit-in-app-purchase-information). |
| Developer Removed from Sale | Select the countries or regions where you want to sell the In-App Purchase. For more information, see [`Set availability for in-app purchases`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-in-app-purchases/set-availability-for-in-app-purchases). |

#### Review the Availability of Your in App Purchases

A customer’s [`Apple Account`](https://developer.apple.comhttps://developer.apple.com/help/glossary/apple-account) country or region determines the App Store country or region where they can purchase content. For example, an account set to Canada can only purchase In-App Purchases from the App Store in Canada. If your In-App Purchase is available in all countries or regions of the App Store except Canada, [`products(for:)`](https://developer.apple.com/documentation/StoreKit/Product/products(for:)) won’t return a `Product` instance for your In-App Purchase on a device with an Apple Account set to Canada. In App Store Connect, you can select or deselect the countries or regions where your In-App Purchases are available on the App Store. For more information, see [`Set availability for in-app purchases`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-in-app-purchases/set-availability-for-in-app-purchases).

After you confirm the status of your In-App Purchases is [`Ready to Submit`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/in-app-purchase-statuses), review their availability in App Store Connect. Confirm you select all the countries or regions where you want to sell the In-App Purchases. For instance, select all the countries and regions supported by the App Store to make your In-App Purchases available for sale in every App Store.

#### Retry Your Product Request Later

After Apple approves your In-App Purchases, it may take some time for the In-App Purchases to be available in all the countries or regions you select in App Store Connect.

#### Revision History

-  First published.

## See Also

- [TN3189: Managing Mail background traffic load](tn3189-managing-mail-background-traffic-load.md)
  Identify iOS Mail background traffic and manage its impact on your IMAP server.
- [TN3187: Migrating to the UIKit scene-based life cycle](tn3187-migrating-to-the-uikit-scene-based-life-cycle.md)
  Update your app to receive scene-based life-cycle events and manage your user interface using scene objects and methods.
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
- [TN3175: Diagnosing issues with displaying the Apple Pay button on your website](tn3175-diagnosing-issues-with-displaying-the-apple-pay-button-on-your-website.md)
  Diagnose common errors received while displaying the Apple Pay button on your website by identifying the underlying causes, and explore potential solutions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3188-troubleshooting-in-app-purchases-availability-in-the-app-store)*