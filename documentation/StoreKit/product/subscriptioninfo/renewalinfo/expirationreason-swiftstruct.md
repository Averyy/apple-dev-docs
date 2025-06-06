# Product.SubscriptionInfo.RenewalInfo.ExpirationReason

**Framework**: StoreKit  
**Kind**: struct

The reasons for auto-renewable subscription expirations.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct ExpirationReason
```

## Topics

### Getting the expiration reason
- [static let autoRenewDisabled: Product.SubscriptionInfo.RenewalInfo.ExpirationReason](product/subscriptioninfo/renewalinfo/expirationreason-swift.struct/autorenewdisabled.md)
  The auto-renewable subscription expired because the customer voluntarily canceled their subscription.
- [static let billingError: Product.SubscriptionInfo.RenewalInfo.ExpirationReason](product/subscriptioninfo/renewalinfo/expirationreason-swift.struct/billingerror.md)
  The auto-renewable subscription expired because of a billing error.
- [static let didNotConsentToPriceIncrease: Product.SubscriptionInfo.RenewalInfo.ExpirationReason](product/subscriptioninfo/renewalinfo/expirationreason-swift.struct/didnotconsenttopriceincrease.md)
  The subscription expired because the customer didn’t consent to an auto-renewable subscription price increase that requires customer consent.
- [static let productUnavailable: Product.SubscriptionInfo.RenewalInfo.ExpirationReason](product/subscriptioninfo/renewalinfo/expirationreason-swift.struct/productunavailable.md)
  The auto-renewable subscription expired because the product was unavailable for purchase at the time of the renewal.
- [static let unknown: Product.SubscriptionInfo.RenewalInfo.ExpirationReason](product/subscriptioninfo/renewalinfo/expirationreason-swift.struct/unknown.md)
  The auto-renewable subscription expired for an unknown reason.
### Getting a localized description
- [var localizedDescription: String](product/subscriptioninfo/renewalinfo/expirationreason-swift.struct/localizeddescription.md)
  The localized text that describes the expiration reason.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [let state: Product.SubscriptionInfo.RenewalState](product/subscriptioninfo/status-swift.struct/state.md)
  The renewal state of the auto-renewable subscription.
- [let autoRenewPreference: String?](product/subscriptioninfo/renewalinfo/autorenewpreference.md)
  The product ID of the auto-renewable subscription that will automatically renew.
- [let willAutoRenew: Bool](product/subscriptioninfo/renewalinfo/willautorenew.md)
  A Boolean value that indicates whether the subscription automatically renews in the next period.
- [let expirationReason: Product.SubscriptionInfo.RenewalInfo.ExpirationReason?](product/subscriptioninfo/renewalinfo/expirationreason-swift.property.md)
  The reason the auto-renewable subscription expired.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/expirationreason-swift.struct)*