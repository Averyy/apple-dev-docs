# updateAll(_:)

**Framework**: StoreKit  
**Kind**: method

Sets the order and visibility of all the promoted products and saves your changes.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+

## Declaration

```swift
static func updateAll(_ promotions: some Collection<Product.PromotionInfo>) async throws
```

## Mentions

- [Supporting promoted In-App Purchases in your app](supporting-promoted-in-app-purchases-in-your-app.md)

#### Discussion

Call this static method to set the order of promoted in-app purchases for the user. Calling this method overrides any previous order and visibility that you set for this user.

To remove a promoted in-app purchase so it doesn’t display for a user, there are two options:

- Don’t include it in the `promotions` collection.
- Change its [`visibility`](product/promotioninfo/visibility-swift.property.md) value to [`Product.PromotionInfo.Visibility.hidden`](product/promotioninfo/visibility-swift.enum/hidden.md).

To set the order of promoted in-app purchases using product identifiers instead of [`Product.PromotionInfo`](product/promotioninfo.md) objects, see [`updateProductOrder(byID:)`](product/promotioninfo/updateproductorder(byid:).md).

##### Cancel Overrides

To cancel the order and visibility changes you make, send an empty collection in `promotions`. All in-app purchases then display in the default order.

## Parameters

- `promotions`: A collection of   objects that you list in the order they are to appear in the App Store on the user’s device. Use an empty collection to cancel previous changes.

## See Also

- [func update() async throws](product/promotioninfo/update.md)
  Saves your changes to the promoted product’s visibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/promotioninfo/updateall(_:))*