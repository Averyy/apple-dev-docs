# update()

**Framework**: StoreKit  
**Kind**: method

Saves your changes to the promoted product’s visibility.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+

## Declaration

```swift
func update() async throws
```

## Mentions

- [Supporting promoted In-App Purchases in your app](supporting-promoted-in-app-purchases-in-your-app.md)

#### Discussion

If you change the [`visibility`](product/promotioninfo/visibility-swift.property.md) value by setting it directly, call [`update()`](product/promotioninfo/update().md) to save your changes to the App Store server. Changes take effect after you call [`update()`](product/promotioninfo/update().md) or [`updateAll(_:)`](product/promotioninfo/updateall(_:).md).

## See Also

- [static func updateAll(some Collection<Product.PromotionInfo>) async throws](product/promotioninfo/updateall(_:).md)
  Sets the order and visibility of all the promoted products and saves your changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/promotioninfo/update())*