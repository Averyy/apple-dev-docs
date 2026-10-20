# Product.SubscriptionInfo.RenewalInfo.ExpirationReason

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

The reasons for auto-renewable subscription expirations.

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
struct ExpirationReason
```

## Topics

### Getting the expiration reason
- [static let autoRenewDisabled: Product.SubscriptionInfo.RenewalInfo.ExpirationReason](./expirationreason-swift.struct/autorenewdisabled.md)
  The auto-renewable subscription expired because the customer voluntarily canceled their subscription.
- [static let billingError: Product.SubscriptionInfo.RenewalInfo.ExpirationReason](./expirationreason-swift.struct/billingerror.md)
  The auto-renewable subscription expired because of a billing error.
- [static let didNotConsentToPriceIncrease: Product.SubscriptionInfo.RenewalInfo.ExpirationReason](./expirationreason-swift.struct/didnotconsenttopriceincrease.md)
  The subscription expired because the customer didn’t consent to a price increase that requires customer consent.
- [static let productUnavailable: Product.SubscriptionInfo.RenewalInfo.ExpirationReason](./expirationreason-swift.struct/productunavailable.md)
  The auto-renewable subscription expired because the product was unavailable for purchase at the time of the renewal.
- [static let unknown: Product.SubscriptionInfo.RenewalInfo.ExpirationReason](./expirationreason-swift.struct/unknown.md)
  The auto-renewable subscription expired for an unknown reason.
### Getting a localized description
- [var localizedDescription: String](./expirationreason-swift.struct/localizeddescription.md)
  The localized text that describes the expiration reason.
### Type Properties
- [static var unbundled: Product.SubscriptionInfo.RenewalInfo.ExpirationReason](./expirationreason-swift.struct/unbundled.md)
  The subscription expired because the customer left the Subscription Bundle.

## Relationships

### Conforms To
- [Equatable](../../../../Swift/equatable.md)
- [Hashable](../../../../Swift/hashable.md)
- [RawRepresentable](../../../../Swift/rawrepresentable.md)
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)

## See Also

### Getting the renewal or expiration state
- [let state: Product.SubscriptionInfo.RenewalState](../status-swift.struct/state.md)
  The renewal state of the auto-renewable subscription.
- [let autoRenewPreference: String?](./autorenewpreference.md)
  The product ID of the auto-renewable subscription that will automatically renew.
- [let willAutoRenew: Bool](./willautorenew.md)
  A Boolean value that indicates whether the subscription automatically renews in the next period.
- [let expirationReason: Product.SubscriptionInfo.RenewalInfo.ExpirationReason?](./expirationreason-swift.property.md)
  The reason the auto-renewable subscription expired.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/expirationreason-swift.struct)*