# Storefront

**Framework**: StoreKit  
**Kind**: struct

The region and unique identifier of the App Store storefront for the device.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct Storefront
```

## Mentions

- [Testing In-App Purchases with sandbox](testing-in-app-purchases-with-sandbox.md)

#### Overview

In-app products you create through App Store Connect are available for sale in each region with an App Store. You can use the storefront information to determine the customer’s region, and offer in-app products suitable for that region.

You need to maintain your own list of product identifiers and the storefronts where you want to make them available.

> **Note**:  Don’t save the storefront information with your customer information because storefront information can change at any time. Get the storefront identifier immediately before you display product information or availability in your app. Don’t use storefront information to develop or enhance a customer profile, or to track customers for advertising or marketing purposes.

##### Change the App Store Country or Region in the Sandbox Environment

When you change the App Store Country or Region in App Store Connect for a Sandbox Apple Account, it changes the storefront in your app. Change the region to test In-App Purchases for different regions in your app. For more information about changing the App Store Country or Region in App Store Connect, see [`Test in-app purchases`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/test-in-app-purchases/manage-sandbox-apple-account-settings/).

> ❗ **Important**:  To successfully activate a storefront after you change the region in App Store Connect, sign out of the Sandbox Apple Account on the device and sign back in.

## Topics

### Identifying the storefront
- [static var current: Storefront?](storefront/current.md)
  The current App Store storefront for product purchases.
- [let countryCode: String](storefront/countrycode.md)
  The three-letter code that represents the country or region associated with the App Store storefront.
- [let id: String](storefront/id.md)
  An Apple-defined value that uniquely identifies an App Store storefront.
### Listening for storefront changes
- [static var updates: Storefront.Storefronts](storefront/updates.md)
  The asynchronous sequence that emits storefront information when the system updates the storefront.
- [Storefront.Storefronts](storefront/storefronts.md)
  An asynchronous sequence that listens for changes to the storefront.
### Getting the currency for the storefront
- [var currency: Locale.Currency?](storefront/currency.md)
  The currency that the storefront uses.

## Relationships

### Conforms To
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static var current: Storefront?](storefront/current.md)
  The current App Store storefront for product purchases.
- [static var updates: Storefront.Storefronts](storefront/updates.md)
  The asynchronous sequence that emits storefront information when the system updates the storefront.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/storefront)*