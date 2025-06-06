# expirationReason

**Framework**: StoreKit  
**Kind**: property

The reason the auto-renewable subscription expired.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
let expirationReason: Product.SubscriptionInfo.RenewalInfo.ExpirationReason?
```

## Mentions

- [Managing Price Increases for Auto-Renewable Subscriptions](managing-price-increases-for-auto-renewable-subscriptions.md)

#### Discussion

This optional value is `nil` if the auto-renewable subscription is active and hasn’t expired.

## See Also

- [let state: Product.SubscriptionInfo.RenewalState](product/subscriptioninfo/status-swift.struct/state.md)
  The renewal state of the auto-renewable subscription.
- [let autoRenewPreference: String?](product/subscriptioninfo/renewalinfo/autorenewpreference.md)
  The product ID of the auto-renewable subscription that will automatically renew.
- [let willAutoRenew: Bool](product/subscriptioninfo/renewalinfo/willautorenew.md)
  A Boolean value that indicates whether the subscription automatically renews in the next period.
- [Product.SubscriptionInfo.RenewalInfo.ExpirationReason](product/subscriptioninfo/renewalinfo/expirationreason-swift.struct.md)
  The reasons for auto-renewable subscription expirations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/expirationreason-swift.property)*