# didNotConsentToPriceIncrease

**Framework**: StoreKit  
**Kind**: property

The subscription expired because the customer didn’t consent to a price increase that requires customer consent.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static let didNotConsentToPriceIncrease: Product.SubscriptionInfo.RenewalInfo.ExpirationReason
```

## Mentions

- [Managing Price Increases for Auto-Renewable Subscriptions](managing-price-increases-for-auto-renewable-subscriptions.md)

#### Discussion

The customer didn’t consent to an auto-renewable subscription price increase that requires their consent, or to a subscription offer conversion that requires their consent, so the subscription expired.

For more information about subscription price increases that require customer consent, see [`Auto-renewable subscription price increase thresholds`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/auto-renewable-subscription-price-increase-thresholds). For more information about offer conversions that require customer consent, see [`Consent for subscription offer conversions`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/consent-for-subscription-offer-conversions).

## See Also

- [static let autoRenewDisabled: Product.SubscriptionInfo.RenewalInfo.ExpirationReason](product/subscriptioninfo/renewalinfo/expirationreason-swift.struct/autorenewdisabled.md)
  The auto-renewable subscription expired because the customer voluntarily canceled their subscription.
- [static let billingError: Product.SubscriptionInfo.RenewalInfo.ExpirationReason](product/subscriptioninfo/renewalinfo/expirationreason-swift.struct/billingerror.md)
  The auto-renewable subscription expired because of a billing error.
- [static let productUnavailable: Product.SubscriptionInfo.RenewalInfo.ExpirationReason](product/subscriptioninfo/renewalinfo/expirationreason-swift.struct/productunavailable.md)
  The auto-renewable subscription expired because the product was unavailable for purchase at the time of the renewal.
- [static let unknown: Product.SubscriptionInfo.RenewalInfo.ExpirationReason](product/subscriptioninfo/renewalinfo/expirationreason-swift.struct/unknown.md)
  The auto-renewable subscription expired for an unknown reason.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/expirationreason-swift.struct/didnotconsenttopriceincrease)*