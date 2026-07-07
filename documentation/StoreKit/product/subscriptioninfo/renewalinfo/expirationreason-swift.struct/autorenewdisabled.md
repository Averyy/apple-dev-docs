# autoRenewDisabled

**Framework**: StoreKit  
**Kind**: property

The auto-renewable subscription expired because the customer voluntarily canceled their subscription.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static let autoRenewDisabled: Product.SubscriptionInfo.RenewalInfo.ExpirationReason
```

## Mentions

- [Managing Price Increases for Auto-Renewable Subscriptions](managing-price-increases-for-auto-renewable-subscriptions.md)

## See Also

- [static let billingError: Product.SubscriptionInfo.RenewalInfo.ExpirationReason](product/subscriptioninfo/renewalinfo/expirationreason-swift.struct/billingerror.md)
  The auto-renewable subscription expired because of a billing error.
- [static let didNotConsentToPriceIncrease: Product.SubscriptionInfo.RenewalInfo.ExpirationReason](product/subscriptioninfo/renewalinfo/expirationreason-swift.struct/didnotconsenttopriceincrease.md)
  The subscription expired because the customer didn’t consent to a price increase that requires customer consent.
- [static let productUnavailable: Product.SubscriptionInfo.RenewalInfo.ExpirationReason](product/subscriptioninfo/renewalinfo/expirationreason-swift.struct/productunavailable.md)
  The auto-renewable subscription expired because the product was unavailable for purchase at the time of the renewal.
- [static let unknown: Product.SubscriptionInfo.RenewalInfo.ExpirationReason](product/subscriptioninfo/renewalinfo/expirationreason-swift.struct/unknown.md)
  The auto-renewable subscription expired for an unknown reason.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/expirationreason-swift.struct/autorenewdisabled)*