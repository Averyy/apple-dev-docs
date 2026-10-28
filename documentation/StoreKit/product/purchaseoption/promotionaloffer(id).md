# promotionalOffer(id:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Type Method

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

## Discussion

Use this purchase option when you test your app in Xcode using [StoreKit Test](../../../StoreKitTest/StoreKitTest.md) and call [`buyProduct(identifier:options:)`](../../../StoreKitTest/sktestsession/buyproduct%28identifier,options%29.md). This method makes it possible to test promotional offers without supplying a signature.

Set up the promotional offer identifiers that you use in this call in your StoreKit configuration file. For more information, see [Setting up StoreKit Testing in Xcode](../../../Xcode/setting-up-storekit-testing-in-xcode.md).

When you apply this option, the purchase transaction simulates a customer redeeming a promotional offer, and includes the promotional offer you specify.

## Parameters

- `identifier`: The identifier of the promotional offer to apply to the transaction. You need to set up identifiers in your StoreKit configuration file.

## See Also

### Setting options for StoreKit Testing in Xcode
- [static func purchaseDate(Date, renewalBehavior: Product.PurchaseOption.SubscriptionRenewalBehavior) -> Product.PurchaseOption](./purchasedate%28_,renewalbehavior%29.md)
  Sets the purchase date for the transaction in the testing environment, and indicates the renewal behavior for an auto-renewable subscription.
- [Product.PurchaseOption.SubscriptionRenewalBehavior](./subscriptionrenewalbehavior.md)
  Renewal options for auto-renewable subscriptions that you purchase in the testing environment.
- [static func codeOffer(referenceName: String) -> Product.PurchaseOption](./codeoffer%28referencename%29.md)
  Sets an offer code for the transaction in the testing environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/purchaseoption/promotionaloffer(id:))*