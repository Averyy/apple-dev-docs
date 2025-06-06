# willAutoRenew

**Framework**: StoreKit  
**Kind**: property

A Boolean value that indicates whether the subscription automatically renews in the next period.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
let willAutoRenew: Bool
```

## Mentions

- [Supporting win-back offers in your app](supporting-win-back-offers-in-your-app.md)

## See Also

- [let state: Product.SubscriptionInfo.RenewalState](product/subscriptioninfo/status-swift.struct/state.md)
  The renewal state of the auto-renewable subscription.
- [let autoRenewPreference: String?](product/subscriptioninfo/renewalinfo/autorenewpreference.md)
  The product ID of the auto-renewable subscription that will automatically renew.
- [let expirationReason: Product.SubscriptionInfo.RenewalInfo.ExpirationReason?](product/subscriptioninfo/renewalinfo/expirationreason-swift.property.md)
  The reason the auto-renewable subscription expired.
- [Product.SubscriptionInfo.RenewalInfo.ExpirationReason](product/subscriptioninfo/renewalinfo/expirationreason-swift.struct.md)
  The reasons for auto-renewable subscription expirations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/willautorenew)*