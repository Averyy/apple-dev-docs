# isFamilyShareable

**Framework**: StoreKit  
**Kind**: property

A Boolean value that indicates whether the product is available for Family Sharing in App Store Connect.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var isFamilyShareable: Bool { get }
```

## Mentions

- [Supporting Family Sharing in your app](supporting-family-sharing-in-your-app.md)

#### Discussion

Check the value of [`isFamilyShareable`](skproduct/isfamilyshareable.md) to learn whether an in-app purchase is sharable with the family group.

```swift
// Determine whether an in-app purchase supports Family Sharing.
let myProduct: SKProduct = getProductWithId(id: "com.example.product_identifier")
if myProduct.isFamilyShareable {
    print("Product can be shared with family group.")
}
```

When displaying in-app purchases in your app, indicate whether the product includes Family Sharing to help customers make a selection that best fits their needs.

Configure your in-app purchases to allow Family Sharing in App Store Connect. For more information about setting up Family Sharing, see [`Turn-on Family Sharing for in-app purchases`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/turn-on-family-sharing-for-in-app-purchases).

## See Also

- [Supporting Family Sharing in your app](supporting-family-sharing-in-your-app.md)
  Provide service to share subscriptions and non-consumable products to family members.
- [func paymentQueue(SKPaymentQueue, didRevokeEntitlementsForProductIdentifiers: [String])](skpaymenttransactionobserver/paymentqueue(_:didrevokeentitlementsforproductidentifiers:).md)
  Tells an observer that the customer is no longer entitled to one or more Family Sharing purchases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproduct/isfamilyshareable)*