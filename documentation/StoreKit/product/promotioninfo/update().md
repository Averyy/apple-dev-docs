# update()

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

Saves your changes to the promoted product’s visibility.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
func update() async throws
```

## Mentions

- [Supporting promoted Apple In-App Purchases in your app](../../supporting-promoted-in-app-purchases-in-your-app.md)

#### Discussion

If you change the [`visibility`](./visibility-swift.property.md) value by setting it directly, call [`update()`](./update%28%29.md) to save your changes to the App Store server. Changes take effect after you call [`update()`](./update%28%29.md) or [`updateAll(_:)`](./updateall%28_%29.md).

## See Also

### Updating order and visibility
- [static func updateAll(some Collection<Product.PromotionInfo>) async throws](./updateall%28_%29.md)
  Sets the order and visibility of all the promoted products and saves your changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/promotioninfo/update())*