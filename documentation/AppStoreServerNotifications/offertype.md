# offerType

**Framework**: App Store Server Notifications  
**Kind**: typealias

The type of offer.

**Availability**:
- App Store Server Notifications 2.0+

## Declaration

```swift
int32 offerType
```

## Mentions

- [App Store Server Notifications changelog](app-store-server-notifications-changelog.md)

#### Discussion

All offer types, except offer type `1`, have an [`offerIdentifier`](offeridentifier.md).

You set up offers in App Store Connect. For more information on subscription offers, see [`Set up introductory offers for auto-renewable subscriptions`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-introductory-offers-for-auto-renewable-subscriptions), [`Set up promotional offers for auto-renewable subscriptions`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-promotional-offers-for-auto-renewable-subscriptions), [`Set up offer codes`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-offer-codes), and [`Set up win-back offers`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-win-back-offers). For more information on offer codes, see [`Create offer codes for In-App Purchases`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-in-app-purchases/create-offer-codes-for-in-app-purchases).

## See Also

- [type eligibleWinBackOfferIds](eligiblewinbackofferids.md)
  An array of win-back offer identifiers that a customer is eligible to redeem, which sorts the identifiers to present the better offers first.
- [type offerIdentifier](offeridentifier.md)
  The string identifier of an offer that you create in App Store Connect.
- [type offerPeriod](offerperiod.md)
  The duration of the offer.
- [type offerDiscountType](offerdiscounttype.md)
  The payment mode for a discount offer on an In-App Purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/offertype)*