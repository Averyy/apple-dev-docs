# Product.PromotionInfo.Visibility

**Framework**: StoreKit  
**Kind**: enum

The visibility states for product promotion information.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+

## Declaration

```swift
enum Visibility
```

#### Overview

Use the visibility states to set the [`visibility`](product/promotioninfo/visibility-swift.property.md) of a promoted in-app purchase. Call [`update()`](product/promotioninfo/update().md) to save your changes.

The visibility states have the following effects on the user’s device:

- [`Product.PromotionInfo.Visibility.visible`](product/promotioninfo/visibility-swift.enum/visible.md) makes the promoted in-app purchase visible in the App Store.
- [`Product.PromotionInfo.Visibility.hidden`](product/promotioninfo/visibility-swift.enum/hidden.md) hides the promoted in-app purchase in the App Store.
- [`Product.PromotionInfo.Visibility.appStoreConnectDefault`](product/promotioninfo/visibility-swift.enum/appstoreconnectdefault.md) let’s you control the visibility using settings in App Store Connect. For more information, see [`Promote in-app purchases`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/promote-in-app-purchases).

## Topics

### Getting visibility states
- [Product.PromotionInfo.Visibility.appStoreConnectDefault](product/promotioninfo/visibility-swift.enum/appstoreconnectdefault.md)
  A visibility value for a promoted in-app purchase that uses the visibility setting from App Store Connect.
- [Product.PromotionInfo.Visibility.hidden](product/promotioninfo/visibility-swift.enum/hidden.md)
  A visibility value that hides a promoted in-app purchase on the App Store on a user’s device.
- [Product.PromotionInfo.Visibility.visible](product/promotioninfo/visibility-swift.enum/visible.md)
  A visibility value that makes a promoted in-app purchase visible on the App Store on a user’s device.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

## See Also

- [var visibility: Product.PromotionInfo.Visibility](product/promotioninfo/visibility-swift.property.md)
  A value that indicates whether the promoted in-app purchase is visible or hidden on the user’s device.
- [static func updateProductVisibility(Product.PromotionInfo.Visibility, for: Product.ID) async throws](product/promotioninfo/updateproductvisibility(_:for:).md)
  Updates a value that indicates whether a promoted in-app purchase appears in the App Store on the user’s device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/promotioninfo/visibility-swift.enum)*