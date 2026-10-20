# transaction

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The latest transaction for the subscription group.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
let transaction: VerificationResult<Transaction>
```

## See Also

### Getting subscription status information
- [let state: Product.SubscriptionInfo.RenewalState](./state.md)
  The renewal state of the auto-renewable subscription.
- [let renewalInfo: VerificationResult<Product.SubscriptionInfo.RenewalInfo>](./renewalinfo.md)
  The signed renewal information for the auto-renewable subscription.
- [Product.SubscriptionInfo.RenewalInfo](../renewalinfo.md)
  The renewal information for an auto-renewable subscription.
- [Product.SubscriptionInfo.RenewalState](../renewalstate.md)
  The renewal states of auto-renewable subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/status-swift.struct/transaction)*