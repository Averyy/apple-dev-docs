# TN3188: Troubleshooting In-App Purchases availability in the App Store

**Framework**: Technotes  
**Role**: Technote

Verify your In-App Purchases are approved and available for sale in the App Store.

## Overview

When launching your app in the App Store, the app may not display your In-App Purchases. To offer In-App Purchases in your app, call [`Product.products(for:)`](../StoreKit/product/products%28for%29.md) with a list of [product identifiers](https://developer.apple.com/help/app-store-connect/reference/in-app-purchase-information) (`Product ID`) matching these products in App Store Connect. `Product.products(for:)` returns an array that includes an instance of [`Product`](../StoreKit/product.md) for each of the In-App Purchases. Update your app’s UI with these returned instances, which contain all In-App Purchase data configured in App Store Connect for your app.

If `Product.products(for:)` fails to return a `Product` instance for your In-App Purchases, it may be due to the following reasons:

- Your In-App Purchases are missing or don’t exist in the App Store.
- Your In-App Purchases exist in the App Store, but they are unapproved and unavailable.

> **Note**: If your app fails to display its products when testing In-App Purchases in Xcode or the Apple sandbox environment, see [TN3185: Troubleshooting In-App Purchases availability in Xcode](./tn3185-troubleshooting-in-app-purchases-availability-in-xcode.md) and [TN3186: Troubleshooting In-App Purchases availability in the sandbox](./tn3186-troubleshooting-in-app-purchases-availability-in-the-sandbox.md), respectively.

## Validate your product identifier list

To verify your product identifier list, perform these steps:

1. In your Xcode project, [locate](../Xcode/preparing-your-app-for-distribution.md) your app’s [bundle ID](../BundleResources/information-property-list/cfbundleidentifier.md).
2. In App Store Connect, find the app that matches your app’s bundle ID.
3. Verify each product identifier in your list matches the product identifier (`Product ID`) of an In-App Purchase created for the app in App Store Connect.

## Review the status of your In-App Purchases

In App Store Connect, submit your In-App Purchases for review. To submit an In-App Purchase for review, the In-App Purchase must have the [Ready to Submit](https://developer.apple.com/help/app-store-connect/reference/in-app-purchase-statuses) status. If the In-App Purchase doesn’t have this status, [complete any missing information](https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/view-and-edit-in-app-purchase-information) such as price or localization for the subscription group display name. For more information about submitting In-App Purchases, see [Submit for review](https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-for-review).

After Apple completes review of your In-App Purchases, confirm that the status of each In-App Purchase you submitted is [`Approved`](https://developer.apple.com/help/app-store-connect/reference/in-app-purchase-statuses). If App Store Connect shows [`Developer Action Needed`](https://developer.apple.com/help/app-store-connect/reference/in-app-purchase-statuses) or [`Developer Removed from Sale`](https://developer.apple.com/help/app-store-connect/reference/in-app-purchase-statuses) for an In-App Purchase, handle the status as described in the following table:

| Status | Perform action |
| --- | --- |
| Developer Action Needed | Update the In-App Purchase information. For more information, see [View and edit in-app purchase information](https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/view-and-edit-in-app-purchase-information). |
| Developer Removed from Sale | Select the countries or regions where you want to sell the In-App Purchase. For more information, see [Set availability for in-app purchases](https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/set-availability-for-in-app-purchases). |

## Review the availability of your In-App Purchases

A customer’s [Apple Account](https://developer.apple.com/help/glossary/apple-account) country or region determines the App Store country or region where they can purchase content. For example, an account set to Canada can only purchase In-App Purchases from the App Store in Canada. If your In-App Purchase is available in all countries or regions of the App Store except Canada, [`Product.products(for:)`](../StoreKit/product/products%28for%29.md) won’t return a `Product` instance for your In-App Purchase on a device with an Apple Account set to Canada. In App Store Connect, you can select or deselect the countries or regions where your In-App Purchases are available on the App Store. For more information, see [Set availability for in-app purchases](https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/set-availability-for-in-app-purchases).

After you confirm the status of your In-App Purchases is [`Approved`](https://developer.apple.com/help/app-store-connect/reference/in-app-purchase-statuses), review their availability in App Store Connect. Confirm you select all the countries or regions where you want to sell the In-App Purchases. For instance, select all the countries and regions supported by the App Store to make your In-App Purchases available for sale in every App Store.

## Retry your product request later

After Apple approves your In-App Purchases, it may take some time for the In-App Purchases to be available in all the countries or regions you select in App Store Connect.

## Revision History

- **2025-04-29** First published.

## See Also

### Related Documentation
- [TN3185: Troubleshooting In-App Purchases availability in Xcode](./tn3185-troubleshooting-in-app-purchases-availability-in-xcode.md)
  Inspect your active StoreKit configuration file for unexpected configurations.
- [TN3186: Troubleshooting In-App Purchases availability in the sandbox](./tn3186-troubleshooting-in-app-purchases-availability-in-the-sandbox.md)
  Identify common configurations that make your In-App Purchases unavailable in the sandbox environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3188-troubleshooting-in-app-purchases-availability-in-the-app-store)*