# TN3185: Troubleshooting In-App Purchases availability in Xcode

**Framework**: Technotes  
**Role**: Technote

Inspect your active StoreKit configuration file for unexpected configurations.

#### Overview

When using [StoreKit Testing in Xcode](../Xcode/setting-up-storekit-testing-in-xcode.md) to test your In-App Purchases, your app may not display its products. StoreKit Testing in Xcode is a local test environment for testing In-App Purchases without requiring a connection to App Store servers. To set up testing in this environment, add a local or synced StoreKit configuration file that contains In-App Purchases to your Xcode project. For more information, see [Create a StoreKit configuration file](../Xcode/setting-up-storekit-testing-in-xcode.md). When you [enable a configuration file](../Xcode/setting-up-storekit-testing-in-xcode.md) in your Xcode project, this file becomes active. StoreKit uses data saved in the active configuration file when your app calls StoreKit APIs in the test environment. For more information, see [Setting up StoreKit Testing in Xcode](../Xcode/setting-up-storekit-testing-in-xcode.md).

To offer In-App Purchases in your app, call [`Product.products(for:)`](../StoreKit/product/products%28for%29.md) with a list of [product identifiers](https://developer.apple.com/help/app-store-connect/reference/in-app-purchase-information) (`Product ID`) matching these products in the test environment. `Product.products(for:)` returns an array that includes an instance of [`Product`](../StoreKit/product.md) for each of the In-App Purchases. Update your app’s UI with these returned instances, which contain all In-App Purchase information set up in the active configuration file for your app.

If `Product.products(for:)` fails to return a Product instance for your In-App Purchases, it may be due to the following reasons:

- Your In-App Purchases are missing or don’t exist in the active StoreKit configuration file.
- You set up the test environment to simulate a load products failure scenario.

> **Note**: If your app fails to display its products when testing In-App Purchases in the Apple sandbox environment, or when launching the app in the App Store, see [TN3186: Troubleshooting In-App Purchases availability in the sandbox](./tn3186-troubleshooting-in-app-purchases-availability-in-the-sandbox.md) and [TN3188: Troubleshooting In-App Purchases availability in the App Store](./tn3188-troubleshooting-in-app-purchases-availability-in-the-app-store.md), respectively.

#### Validate your product identifier list

Inspect the active StoreKit configuration file in your Xcode project. Confirm each product identifier in your list matches the product identifier of an In-App Purchase configured in this file.

#### Disable the Simulated StoreKit Load Products failure setting

A [StoreKit configuration file](../Xcode/setting-up-storekit-testing-in-xcode.md) includes settings you can use to specify test conditions or scenarios for your In-App Purchases such as Load Products. When you enable Load Products, the test environment simulates the load product failure scenario you specified such as network error. Calling [`Product.products(for:)`](../StoreKit/product/products%28for%29.md) in your app throws a [StoreKit error](../StoreKit/storekiterror.md). When you disable this setting, the function returns all your In-App Purchases that exist in the active configuration file. For more information, see [Change settings and initiate test conditions](../Xcode/testing-in-app-purchases-with-storekit-transaction-manager-in-code.md) in [Testing in-app purchases with StoreKit transaction manager in Xcode](../Xcode/testing-in-app-purchases-with-storekit-transaction-manager-in-code.md).

To prevent the test environment from simulating a load products failure scenario, perform these steps in your Xcode project:

1. In the Project navigator, select your active StoreKit configuration file.
2. Click Configuration Settings.
3. Scroll down to Simulated StoreKit Failures.
4. Disable the Load Products setting.

#### Revision History

- **2025-04-29** First published.

## See Also

### Related Documentation
- [TN3186: Troubleshooting In-App Purchases availability in the sandbox](./tn3186-troubleshooting-in-app-purchases-availability-in-the-sandbox.md)
  Identify common configurations that make your In-App Purchases unavailable in the sandbox environment.
- [TN3188: Troubleshooting In-App Purchases availability in the App Store](./tn3188-troubleshooting-in-app-purchases-availability-in-the-app-store.md)
  Verify your In-App Purchases are approved and available for sale in the App Store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3185-troubleshooting-in-app-purchases-availability-in-xcode)*