# TN3185: Troubleshooting In-App Purchases availability in Xcode

**Framework**: Technotes

Inspect your active StoreKit configuration file for unexpected configurations.

#### Overview

When using [`Setting up StoreKit Testing in Xcode`](https://developer.apple.com/documentation/Xcode/setting-up-storekit-testing-in-xcode) to test your In-App Purchases, your app may not display its products. StoreKit Testing in Xcode is a local test environment for testing In-App Purchases without requiring a connection to App Store servers. To set up testing in this environment, add a local or synced StoreKit configuration file that contains In-App Purchases to your Xcode project. For more information, see [`Setting up StoreKit Testing in Xcode`](https://developer.apple.com/documentation/Xcode/setting-up-storekit-testing-in-xcode). When you [`Setting up StoreKit Testing in Xcode`](https://developer.apple.com/documentation/Xcode/setting-up-storekit-testing-in-xcode) in your Xcode project, this file becomes active. StoreKit uses data saved in the active configuration file when your app calls StoreKit APIs in the test environment. For more information, see [`Setting up StoreKit Testing in Xcode`](https://developer.apple.com/documentation/Xcode/setting-up-storekit-testing-in-xcode).

To offer In-App Purchases in your app, call [`products(for:)`](https://developer.apple.com/documentation/StoreKit/Product/products(for:)) with a list of [`product identifiers`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/in-app-purchase-information) (`Product ID`) matching these products in the test environment. `Product.products(for:)` returns an array that includes an instance of [`Product`](https://developer.apple.com/documentation/StoreKit/Product) for each of the In-App Purchases. Update your app’s UI with these returned instances, which contain all In-App Purchase information set up in the active configuration file for your app.

If `Product.products(for:)` fails to return a Product instance for your In-App Purchases, it may be due to the following reasons:

- Your In-App Purchases are missing or don’t exist in the active StoreKit configuration file.
- You set up the test environment to simulate a load products failure scenario.

> **Note**: If your app fails to display its products when testing In-App Purchases in the Apple sandbox environment, or when launching the app in the App Store, see [`TN3186: Troubleshooting In-App Purchases availability in the sandbox`](tn3186-troubleshooting-in-app-purchases-availability-in-the-sandbox.md) and [`TN3188: Troubleshooting In-App Purchases availability in the App Store`](tn3188-troubleshooting-in-app-purchases-availability-in-the-app-store.md), respectively.

#### Validate Your Product Identifier List

Inspect the active StoreKit configuration file in your Xcode project. Confirm each product identifier in your list matches the product identifier of an In-App Purchase configured in this file.

#### Disable the Simulated Storekit Load Products Failure Setting

A [`Setting up StoreKit Testing in Xcode`](https://developer.apple.com/documentation/Xcode/setting-up-storekit-testing-in-xcode) includes settings you can use to specify test conditions or scenarios for your In-App Purchases such as Load Products. When you enable Load Products, the test environment simulates the load product failure scenario you specified such as network error. Calling [`products(for:)`](https://developer.apple.com/documentation/StoreKit/Product/products(for:)) in your app throws a [`StoreKitError`](https://developer.apple.com/documentation/StoreKit/StoreKitError). When you disable this setting, the function returns all your In-App Purchases that exist in the active configuration file. For more information, see [`Testing in-app purchases with StoreKit transaction manager in Xcode`](https://developer.apple.com/documentation/Xcode/testing-in-app-purchases-with-storeKit-transaction-manager-in-code) in [`Testing in-app purchases with StoreKit transaction manager in Xcode`](https://developer.apple.com/documentation/Xcode/testing-in-app-purchases-with-storeKit-transaction-manager-in-code).

To prevent the test environment from simulating a load products failure scenario, perform these steps in your Xcode project:

1. In the Project navigator, select your active StoreKit configuration file.
2. Click Configuration Settings.
3. Scroll down to Simulated StoreKit Failures.
4. Disable the Load Products setting.

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

*[View on Apple Developer](https://developer.apple.com/documentation/Technotes/tn3185-troubleshooting-in-app-purchases-availability-in-xcode)*