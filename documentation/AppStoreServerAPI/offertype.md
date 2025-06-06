# offerType

**Framework**: App Store Server API  
**Kind**: typealias

The type of subscription offer.

**Availability**:
- App Store Server API 1.0+

## Declaration

```swift
int32 offerType
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

All offer types, except offer type `1`, have an [`offerIdentifier`](offeridentifier.md).

You set up subscription offers in App Store Connect. For more information about introductory offers, see [`Implementing introductory offers in your app`](https://developer.apple.com/documentation/StoreKit/implementing-introductory-offers-in-your-app). For more information about promotional offers, see [`Set up promotional offers for auto-renewable subscriptions`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/dev16dfca448). For more information about promo codes, see [`Promo codes overview`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/dev50869de4a).

## See Also

- [type eligibleWinBackOfferIds](eligiblewinbackofferids.md)
  An array of win-back offer identifiers that a customer is eligible to redeem, which sorts the identifiers with the best offers first.
- [type offerIdentifier](offeridentifier.md)
  The string identifier of a subscription offer that you create in App Store Connect.
- [type offerPeriod](offerperiod.md)
  The duration of the offer.
- [type offerDiscountType](offerdiscounttype.md)
  The payment mode for subscription offers on an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/offertype)*