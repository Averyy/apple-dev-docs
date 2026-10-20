# Product.PurchaseOption.SubscriptionRenewalBehavior.renewUntilNow

**Framework**: StoreKit  
**Kind**: case  
**Role**: Case

A subscription-renewal behavior in the testing environment that allows the subscription to renew continuously, up to the current date.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
case renewUntilNow
```

#### Discussion

Choose this option to create test cases that require an auto-renewable subscription that continues to renew. If you set the purchase date in [`purchaseDate(_:renewalBehavior:)`](../purchasedate%28_,renewalbehavior%29.md)to the past, the testing environment generates transactions for all the subscription renewals up to the current date.

## See Also

### Renewal behaviors in the testing environment
- [Product.PurchaseOption.SubscriptionRenewalBehavior.cancelImmediately](./cancelimmediately.md)
  A subscription-renewal behavior in the testing environment that cancels the subscription, resulting in only one subscription period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/purchaseoption/subscriptionrenewalbehavior/renewuntilnow)*