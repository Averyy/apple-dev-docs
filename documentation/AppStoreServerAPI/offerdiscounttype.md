# offerDiscountType

**Framework**: App Store Server API  
**Kind**: typealias

The payment mode for subscription offers on an auto-renewable subscription.

**Availability**:
- App Store Server API 1.10+

## Declaration

```swift
string offerDiscountType
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

You set up subscription offers and determine the payment mode when you configure subscriptions in App Store Connect. For more information about the free trial, pay as you go, and pay up front payment modes, see [`Pricing and availability`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/pricing-and-availability).

For more information on subscription offers, see [`Providing subscription offers`](https://developer.apple.comhttps://developer.apple.com/app-store/subscriptions/#providing-subscription-offers).

## See Also

- [type eligibleWinBackOfferIds](eligiblewinbackofferids.md)
  An array of win-back offer identifiers that a customer is eligible to redeem, which sorts the identifiers with the best offers first.
- [type offerIdentifier](offeridentifier.md)
  The string identifier of a subscription offer that you create in App Store Connect.
- [type offerPeriod](offerperiod.md)
  The duration of the offer.
- [type offerType](offertype.md)
  The type of subscription offer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/offerdiscounttype)*