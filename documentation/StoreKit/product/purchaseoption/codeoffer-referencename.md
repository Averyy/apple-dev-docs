# codeOffer(referenceName:)

**Framework**: StoreKit  
**Kind**: method

Sets an offer code for the transaction in the testing environment.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static func codeOffer(referenceName: String) -> Product.PurchaseOption
```

#### Discussion

Use this purchase option when you test your app in Xcode using [`StoreKit Test`](https://developer.apple.com/documentation/StoreKitTest) and call [`buyProduct(identifier:options:)`](https://developer.apple.com/documentation/StoreKitTest/SKTestSession/buyProduct(identifier:options:)).

Set up the offer codes to use in this call in your StoreKit configuration file. For more information, see [`Setting up StoreKit Testing in Xcode`](https://developer.apple.com/documentation/Xcode/setting-up-storekit-testing-in-xcode).

When you apply this option, the purchase transaction simulates a customer redeeming an offer code and includes the offer code you specify.

## Parameters

- `referenceName`: The reference name of the offer code to apply to the transaction. You need to set up offer codes in your StoreKit configuration file.

## See Also

- [static func purchaseDate(Date, renewalBehavior: Product.PurchaseOption.SubscriptionRenewalBehavior) -> Product.PurchaseOption](product/purchaseoption/purchasedate(_:renewalbehavior:).md)
  Sets the purchase date for the transaction in the testing environment, and indicates the renewal behavior for an auto-renewable subscription.
- [Product.PurchaseOption.SubscriptionRenewalBehavior](product/purchaseoption/subscriptionrenewalbehavior.md)
  Renewal options for auto-renewable subscriptions that you purchase in the testing environment.
- [static func promotionalOffer(id: String) -> Product.PurchaseOption](product/purchaseoption/promotionaloffer(id:).md)
  Sets a promotional offer for the transaction in the testing environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/purchaseoption/codeoffer(referencename:))*