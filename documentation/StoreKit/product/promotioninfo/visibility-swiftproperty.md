# visibility

**Framework**: StoreKit  
**Kind**: property

A value that indicates whether the promoted in-app purchase is visible or hidden on the user’s device.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+

## Declaration

```swift
var visibility: Product.PromotionInfo.Visibility
```

## Mentions

- [Supporting promoted In-App Purchases in your app](supporting-promoted-in-app-purchases-in-your-app.md)

#### Discussion

To override the visibility of a promoted in-app purchase, set the [`visibility`](product/promotioninfo/visibility-swift.property.md) value and then call [`update()`](product/promotioninfo/update().md) to save the change. You can also call [`updateProductVisibility(_:for:)`](product/promotioninfo/updateproductvisibility(_:for:).md) to set the visibility.

The default value is [`Product.PromotionInfo.Visibility.appStoreConnectDefault`](product/promotioninfo/visibility-swift.enum/appstoreconnectdefault.md).

## See Also

- [Product.PromotionInfo.Visibility](product/promotioninfo/visibility-swift.enum.md)
  The visibility states for product promotion information.
- [static func updateProductVisibility(Product.PromotionInfo.Visibility, for: Product.ID) async throws](product/promotioninfo/updateproductvisibility(_:for:).md)
  Updates a value that indicates whether a promoted in-app purchase appears in the App Store on the user’s device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/promotioninfo/visibility-swift.property)*