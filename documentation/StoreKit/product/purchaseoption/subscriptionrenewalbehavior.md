# Product.PurchaseOption.SubscriptionRenewalBehavior

**Framework**: StoreKit  
**Kind**: enum

Renewal options for auto-renewable subscriptions that you purchase in the testing environment.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
enum SubscriptionRenewalBehavior
```

#### Overview

Use the subscription renewal behavior values when you use the [`purchaseDate`](https://developer.apple.com/documentation/StoreKitTest/SKTestTransaction/purchaseDate) option to test your app in Xcode using [`StoreKit Test`](https://developer.apple.com/documentation/StoreKitTest).

## Topics

### Renewal behaviors in the testing environment
- [Product.PurchaseOption.SubscriptionRenewalBehavior.cancelImmediately](product/purchaseoption/subscriptionrenewalbehavior/cancelimmediately.md)
  A subscription-renewal behavior in the testing environment that cancels the subscription, resulting in only one subscription period.
- [Product.PurchaseOption.SubscriptionRenewalBehavior.renewUntilNow](product/purchaseoption/subscriptionrenewalbehavior/renewuntilnow.md)
  A subscription-renewal behavior in the testing environment that allows the subscription to renew continuously, up to the current date.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static func purchaseDate(Date, renewalBehavior: Product.PurchaseOption.SubscriptionRenewalBehavior) -> Product.PurchaseOption](product/purchaseoption/purchasedate(_:renewalbehavior:).md)
  Sets the purchase date for the transaction in the testing environment, and indicates the renewal behavior for an auto-renewable subscription.
- [static func codeOffer(referenceName: String) -> Product.PurchaseOption](product/purchaseoption/codeoffer(referencename:).md)
  Sets an offer code for the transaction in the testing environment.
- [static func promotionalOffer(id: String) -> Product.PurchaseOption](product/purchaseoption/promotionaloffer(id:).md)
  Sets a promotional offer for the transaction in the testing environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/purchaseoption/subscriptionrenewalbehavior)*