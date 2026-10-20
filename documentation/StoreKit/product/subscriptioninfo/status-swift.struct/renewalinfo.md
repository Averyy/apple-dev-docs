# renewalInfo

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The signed renewal information for the auto-renewable subscription.

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
let renewalInfo: VerificationResult<Product.SubscriptionInfo.RenewalInfo>
```

## Mentions

- [Managing the life cycle of monthly subscriptions with a 12-month commitment](../../../managing-lifecycle-of-monthly-subscriptions-with-a-12-month-commitment.md)
- [Managing Price Increases for Auto-Renewable Subscriptions](../../../managing-price-increases-for-auto-renewable-subscriptions.md)
- [Testing Apple In-App Purchases in Xcode](../../../testing-in-app-purchases-in-xcode.md)

## See Also

### Getting subscription status information
- [let state: Product.SubscriptionInfo.RenewalState](./state.md)
  The renewal state of the auto-renewable subscription.
- [let transaction: VerificationResult<Transaction>](./transaction.md)
  The latest transaction for the subscription group.
- [Product.SubscriptionInfo.RenewalInfo](../renewalinfo.md)
  The renewal information for an auto-renewable subscription.
- [Product.SubscriptionInfo.RenewalState](../renewalstate.md)
  The renewal states of auto-renewable subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/status-swift.struct/renewalinfo)*