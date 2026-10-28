# isFamilyShareable

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the product is available for Family Sharing in App Store Connect.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS 14.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 7.0+ - Deprecated in 11.0

> **Deprecated**: Use Product.isFamilyShareable.

## Declaration

```swift
var isFamilyShareable: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL isFamilyShareable;
```

## Mentions

- [Supporting Family Sharing in your app](../supporting-family-sharing-in-your-app.md)

## Discussion

Check the value of [`isFamilyShareable`](./isfamilyshareable.md) to learn whether an Apple In-App Purchase is sharable with the family group.

```swift
// Determine whether an in-app purchase supports Family Sharing.
let myProduct: SKProduct = getProductWithId(id: "com.example.product_identifier")
if myProduct.isFamilyShareable {
    print("Product can be shared with family group.")
}
```

When displaying Apple In-App Purchases in your app, indicate whether the product includes Family Sharing to help customers make a selection that best fits their needs.

Configure your Apple In-App Purchases to allow Family Sharing in App Store Connect. For more information about setting up Family Sharing, see [Turn-on Family Sharing for Apple In-App Purchases](https://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/turn-on-family-sharing-for-in-app-purchases).

## See Also

### Family Sharing
- [Supporting Family Sharing in your app](../supporting-family-sharing-in-your-app.md)
  Provide service to share subscriptions and non-consumable products to family members.
- [func paymentQueue(SKPaymentQueue, didRevokeEntitlementsForProductIdentifiers: [String])](../skpaymenttransactionobserver/paymentqueue%28_,didrevokeentitlementsforproductidentifiers%29.md)
  Tells an observer that the customer is no longer entitled to one or more Family Sharing purchases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproduct/isfamilyshareable)*