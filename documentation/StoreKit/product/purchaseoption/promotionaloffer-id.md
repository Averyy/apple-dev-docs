# promotionalOffer(id:)

**Framework**: StoreKit  
**Kind**: method

Sets a promotional offer for the transaction in the testing environment.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static func promotionalOffer(id identifier: String) -> Product.PurchaseOption
```

#### Discussion

Use this purchase option when you test your app in Xcode using [`StoreKit Test`](https://developer.apple.com/documentation/StoreKitTest) and call [`buyProduct(identifier:options:)`](https://developer.apple.com/documentation/StoreKitTest/SKTestSession/buyProduct(identifier:options:)). This method makes it possible to test promotional offers without supplying a signature.

Set up the promotional offer identifiers that you use in this call in your StoreKit configuration file. For more information, see [`Setting up StoreKit Testing in Xcode`](https://developer.apple.com/documentation/Xcode/setting-up-storekit-testing-in-xcode).

When you apply this option, the purchase transaction simulates a customer redeeming a promotional offer, and includes the promotional offer you specify.

## Parameters

- `identifier`: The identifier of the promotional offer to apply to the transaction. You need to set up identifiers in your StoreKit configuration file.

## See Also

- [static func purchaseDate(Date, renewalBehavior: Product.PurchaseOption.SubscriptionRenewalBehavior) -> Product.PurchaseOption](product/purchaseoption/purchasedate(_:renewalbehavior:).md)
  Sets the purchase date for the transaction in the testing environment, and indicates the renewal behavior for an auto-renewable subscription.
- [Product.PurchaseOption.SubscriptionRenewalBehavior](product/purchaseoption/subscriptionrenewalbehavior.md)
  Renewal options for auto-renewable subscriptions that you purchase in the testing environment.
- [static func codeOffer(referenceName: String) -> Product.PurchaseOption](product/purchaseoption/codeoffer(referencename:).md)
  Sets an offer code for the transaction in the testing environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/purchaseoption/promotionaloffer(id:))*