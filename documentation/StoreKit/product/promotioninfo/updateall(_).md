# updateAll(_:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Type Method

Sets the order and visibility of all the promoted products and saves your changes.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
static func updateAll(_ promotions: some Collection<Product.PromotionInfo>) async throws
```

## Mentions

- [Supporting promoted Apple In-App Purchases in your app](../../supporting-promoted-in-app-purchases-in-your-app.md)

## Discussion

Call this static method to set the order of promoted Apple In-App Purchases for the user. Calling this method overrides any previous order and visibility that you set for this user.

To remove a promoted Apple In-App Purchase so it doesn’t display for a user, there are two options:

- Don’t include it in the `promotions` collection.
- Change its [`visibility`](./visibility-swift.property.md) value to [`Product.PromotionInfo.Visibility.hidden`](./visibility-swift.enum/hidden.md).

To set the order of promoted Apple In-App Purchases using product identifiers instead of [`Product.PromotionInfo`](../promotioninfo.md) objects, see [`updateProductOrder(byID:)`](./updateproductorder%28byid%29.md).

### Cancel overrides

To cancel the order and visibility changes you make, send an empty collection in `promotions`. All Apple In-App Purchases then display in the default order.

## Parameters

- `promotions`: A collection of [`Product.PromotionInfo`](../promotioninfo.md) objects that you list in the order they are to appear in the App Store on the user’s device. Use an empty collection to cancel previous changes.

## See Also

### Updating order and visibility
- [func update() async throws](./update%28%29.md)
  Saves your changes to the promoted product’s visibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/promotioninfo/updateall(_:))*