# Product.PurchaseOption.SubscriptionRenewalBehavior.cancelImmediately

**Framework**: StoreKit  
**Kind**: case  
**Role**: Case

A subscription-renewal behavior in the testing environment that cancels the subscription, resulting in only one subscription period.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
case cancelImmediately
```

## Discussion

Choose this option for test cases that require an auto-renewable subscription that won’t renew.

## See Also

### Renewal behaviors in the testing environment
- [Product.PurchaseOption.SubscriptionRenewalBehavior.renewUntilNow](./renewuntilnow.md)
  A subscription-renewal behavior in the testing environment that allows the subscription to renew continuously, up to the current date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/purchaseoption/subscriptionrenewalbehavior/cancelimmediately)*