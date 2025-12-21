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

1. In your Xcode project, [`Preparing your app for distribution`](https://developer.apple.com/documentation/Xcode/preparing-your-app-for-distribution#Set-the-bundle-ID) your app’s [`CFBundleIdentifier`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleIdentifier).
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
- [TN3186: Troubleshooting In-App Purchases availability in the sandbox](tn3186-troubleshooting-in-app-purchases-availability-in-the-sandbox.md)
  Identify common configurations that make your In-App Purchases unavailable in the sandbox environment.
- [TN3185: Troubleshooting In-App Purchases availability in Xcode](tn3185-troubleshooting-in-app-purchases-availability-in-xcode.md)
  Inspect your active StoreKit configuration file for unexpected configurations.
- [TN3182: Adding privacy tracking keys to your privacy manifest](tn3182-adding-privacy-tracking-keys-to-your-privacy-manifest.md)
  Declare the tracking domains you use in your app or third-party SDK in a privacy manifest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3188-troubleshooting-in-app-purchases-availability-in-the-app-store)*