# Product.PromotionInfo

**Framework**: StoreKit  
**Kind**: struct

Information about a promoted In-App Purchase that customizes its order and visibility on the device.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+

## Declaration

```swift
struct PromotionInfo
```

## Mentions

- [Supporting promoted In-App Purchases in your app](supporting-promoted-in-app-purchases-in-your-app.md)

#### Overview

The `Product.PromotionInfo` structure represents promoted in-app purchases available in your app. You set up promoted in-app purchases using App Store Connect, including their default display order and visibility settings. Use this API to override and customize their order and visibility. Overrides are per device. They can take effect after the user launches the app at least once.

You don’t instantiate this structure. To get a list of `Product.PromotionInfo` objects, call the static method [`updateProductOrder(byID:)`](product/promotioninfo/updateproductorder(byid:).md) with a list of product identifiers that represent your promoted in-app purchases. Then call [`currentOrder`](product/promotioninfo/currentorder.md) to get the list of `Product.PromotionInfo` objects. To change their order, call [`updateAll(_:)`](product/promotioninfo/updateall(_:).md) with the promoted in-app purchases listed in the desired order. To change the order using product identifiers, call [`updateProductOrder(byID:)`](product/promotioninfo/updateproductorder(byid:).md).

To prevent a promoted in-app purchase from appearing in the App Store on the device, there are two options:

- Hide the product by setting the [`visibility`](product/promotioninfo/visibility-swift.property.md) value to [`Product.PromotionInfo.Visibility.hidden`](product/promotioninfo/visibility-swift.enum/hidden.md) and calling [`update()`](product/promotioninfo/update().md), or call [`updateProductVisibility(_:for:)`](product/promotioninfo/updateproductvisibility(_:for:).md).
- Remove the product from the list by excluding it when you call [`updateAll(_:)`](product/promotioninfo/updateall(_:).md) or [`updateProductOrder(byID:)`](product/promotioninfo/updateproductorder(byid:).md).

To cancel your overrides and return to the default order and visibility, call [`updateAll(_:)`](product/promotioninfo/updateall(_:).md) or [`updateProductOrder(byID:)`](product/promotioninfo/updateproductorder(byid:).md) with an empty array.

For more information about promoting in-app purchases, see [`Supporting promoted In-App Purchases in your app`](supporting-promoted-in-app-purchases-in-your-app.md).

## Topics

### Getting the product ID
- [let productID: Product.ID](product/promotioninfo/productid.md)
  The product identifier of the promoted in-app purchase.
### Managing promotion order
- [static func updateProductOrder(byID: some Collection<String>) async throws](product/promotioninfo/updateproductorder(byid:).md)
  Sets the display order of promoted in-app purchases in the App Store, using product identifiers.
### Getting overridden order
- [static var currentOrder: [Product.PromotionInfo]](product/promotioninfo/currentorder.md)
  Gets the customized order of the promotion info objects the represent promoted products.
### Managing promotion visibility
- [var visibility: Product.PromotionInfo.Visibility](product/promotioninfo/visibility-swift.property.md)
  A value that indicates whether the promoted in-app purchase is visible or hidden on the user’s device.
- [Product.PromotionInfo.Visibility](product/promotioninfo/visibility-swift.enum.md)
  The visibility states for product promotion information.
- [static func updateProductVisibility(Product.PromotionInfo.Visibility, for: Product.ID) async throws](product/promotioninfo/updateproductvisibility(_:for:).md)
  Updates a value that indicates whether a promoted in-app purchase appears in the App Store on the user’s device.
### Updating order and visibility
- [func update() async throws](product/promotioninfo/update.md)
  Saves your changes to the promoted product’s visibility.
- [static func updateAll(some Collection<Product.PromotionInfo>) async throws](product/promotioninfo/updateall(_:).md)
  Sets the order and visibility of all the promoted products and saves your changes.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [Supporting promoted In-App Purchases in your app](supporting-promoted-in-app-purchases-in-your-app.md)
  Display promoted In-App Purchases on your product page and handle purchases that users initiate on the App Store.
- [struct PurchaseIntent](purchaseintent.md)
  An instance that emits purchase intents, which indicate that the customer initiated a purchase outside of your app, for your app to complete.
- [Testing promoted In-App Purchases](testing-promoted-in-app-purchases.md)
  Test your In-App Purchases before making your app available in the App Store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/promotioninfo)*