# subscribed

**Framework**: StoreKit  
**Kind**: property  
**Role**: Type Property

The customer is currently subscribed.

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
static let subscribed: Product.SubscriptionInfo.RenewalState
```

## Discussion

An auto-renewable subscription in this state is entitled to service.

## See Also

### Getting the renewal state
- [static let expired: Product.SubscriptionInfo.RenewalState](./expired.md)
  The subscription expired.
- [static let inBillingRetryPeriod: Product.SubscriptionInfo.RenewalState](./inbillingretryperiod.md)
  The subscription is in a billing retry period.
- [static let inGracePeriod: Product.SubscriptionInfo.RenewalState](./ingraceperiod.md)
  The subscription is in a billing grace period state.
- [static let revoked: Product.SubscriptionInfo.RenewalState](./revoked.md)
  The App Store has revoked the customer’s access to the subscription group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalstate/subscribed)*