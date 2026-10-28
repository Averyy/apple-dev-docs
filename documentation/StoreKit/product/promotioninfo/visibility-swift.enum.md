# Product.PromotionInfo.Visibility

**Framework**: StoreKit  
**Kind**: enum  
**Role**: Enumeration

The visibility states for product promotion information.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
enum Visibility
```

## Overview

Use the visibility states to set the [`visibility`](./visibility-swift.property.md) of a promoted in-app purchase. Call [`update()`](./update%28%29.md) to save your changes.

The visibility states have the following effects on the user’s device:

- [`Product.PromotionInfo.Visibility.visible`](./visibility-swift.enum/visible.md) makes the promoted Apple In-App Purchase visible in the App Store.
- [`Product.PromotionInfo.Visibility.hidden`](./visibility-swift.enum/hidden.md) hides the promoted Apple In-App Purchase in the App Store.
- [`Product.PromotionInfo.Visibility.appStoreConnectDefault`](./visibility-swift.enum/appstoreconnectdefault.md) let’s you control the visibility using settings in App Store Connect. For more information, see [Promote Apple In-App Purchases](https://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/promote-in-app-purchases).

## Topics

### Getting visibility states
- [Product.PromotionInfo.Visibility.appStoreConnectDefault](./visibility-swift.enum/appstoreconnectdefault.md)
  A visibility value for a promoted Apple In-App Purchase that uses the visibility setting from App Store Connect.
- [Product.PromotionInfo.Visibility.hidden](./visibility-swift.enum/hidden.md)
  A visibility value that hides a promoted Apple In-App Purchase on the App Store on a user’s device.
- [Product.PromotionInfo.Visibility.visible](./visibility-swift.enum/visible.md)
  A visibility value that makes a promoted Apple In-App Purchase visible on the App Store on a user’s device.

## Relationships

### Conforms To
- [Copyable](../../../Swift/copyable.md)
- [Equatable](../../../Swift/equatable.md)
- [Escapable](../../../Swift/escapable.md)
- [Hashable](../../../Swift/hashable.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)

## See Also

### Managing promotion visibility
- [var visibility: Product.PromotionInfo.Visibility](./visibility-swift.property.md)
  A value that indicates whether the promoted Apple In-App Purchase is visible or hidden on the user’s device.
- [static func updateProductVisibility(Product.PromotionInfo.Visibility, for: Product.ID) async throws](./updateproductvisibility%28_,for%29.md)
  Updates a value that indicates whether a promoted Apple In-App Purchase appears in the App Store on the user’s device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/promotioninfo/visibility-swift.enum)*