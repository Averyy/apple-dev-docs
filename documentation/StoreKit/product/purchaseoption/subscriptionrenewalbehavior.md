# Product.PurchaseOption.SubscriptionRenewalBehavior

**Framework**: StoreKit  
**Kind**: enum  
**Role**: Enumeration

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

Use the subscription renewal behavior values when you use the [`purchaseDate`](../../../StoreKitTest/sktesttransaction/purchasedate.md) option to test your app in Xcode using [StoreKit Test](../../../StoreKitTest/StoreKitTest.md).

## Topics

### Renewal behaviors in the testing environment
- [Product.PurchaseOption.SubscriptionRenewalBehavior.cancelImmediately](./subscriptionrenewalbehavior/cancelimmediately.md)
  A subscription-renewal behavior in the testing environment that cancels the subscription, resulting in only one subscription period.
- [Product.PurchaseOption.SubscriptionRenewalBehavior.renewUntilNow](./subscriptionrenewalbehavior/renewuntilnow.md)
  A subscription-renewal behavior in the testing environment that allows the subscription to renew continuously, up to the current date.

## Relationships

### Conforms To
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Setting options for StoreKit Testing in Xcode
- [static func purchaseDate(Date, renewalBehavior: Product.PurchaseOption.SubscriptionRenewalBehavior) -> Product.PurchaseOption](./purchasedate%28_,renewalbehavior%29.md)
  Sets the purchase date for the transaction in the testing environment, and indicates the renewal behavior for an auto-renewable subscription.
- [static func codeOffer(referenceName: String) -> Product.PurchaseOption](./codeoffer%28referencename%29.md)
  Sets an offer code for the transaction in the testing environment.
- [static func promotionalOffer(id: String) -> Product.PurchaseOption](./promotionaloffer%28id%29.md)
  Sets a promotional offer for the transaction in the testing environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/purchaseoption/subscriptionrenewalbehavior)*