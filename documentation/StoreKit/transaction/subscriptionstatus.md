# subscriptionStatus

**Framework**: StoreKit  
**Kind**: property

An array that contains status information for a subscription group, including renewal and transaction information.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0)
var subscriptionStatus: Product.SubscriptionInfo.Status? { get async }
```

#### Discussion

This value is `nil` if the product in the transaction isn’t an auto-renewable subscription, specifically, if the [`productType`](transaction/producttype.md) is anything other than [`autoRenewable`](product/producttype/autorenewable.md).

The array can have more than one subscription status, for example, if your subscription supports Family Sharing. Provide the customer with service for the subscription based on the highest level of service where the subscription status is [`subscribed`](product/subscriptioninfo/renewalstate/subscribed.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/subscriptionstatus)*