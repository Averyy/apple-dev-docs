# offerDiscountType

**Framework**: App Store Server Notifications  
**Kind**: typealias

The payment mode for a discount offer on an In-App Purchase.

**Availability**:
- App Store Server Notifications 2.9+

## Declaration

```swift
string offerDiscountType
```

## Mentions

- [App Store Server Notifications changelog](app-store-server-notifications-changelog.md)

#### Discussion

Offer discount types apply to auto-renewable subscriptions except for `ONE_TIME`, which applies to the consumable, non-consumable, and non-renewing subscription product types.

You set up offers and determine the payment mode when you configure subscriptions and offers in App Store Connect. For more information about the Free Trial, Pay As You Go, and Pay Up Front payment modes, see [`Pricing and availability`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/pricing-and-availability).

For more information on configuring offers, see: [`Set up introductory offers for auto-renewable subscriptions`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-introductory-offers-for-auto-renewable-subscriptions), [`Set up promotional offers for auto-renewable subscriptions`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-promotional-offers-for-auto-renewable-subscriptions), [`Set up offer codes`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-offer-codes), and [`Create offer codes for In-App Purchases`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-in-app-purchases/create-offer-codes-for-in-app-purchases).

## See Also

- [type eligibleWinBackOfferIds](eligiblewinbackofferids.md)
  An array of win-back offer identifiers that a customer is eligible to redeem, which sorts the identifiers to present the better offers first.
- [type offerIdentifier](offeridentifier.md)
  The string identifier of an offer that you create in App Store Connect.
- [type offerPeriod](offerperiod.md)
  The duration of the offer.
- [type offerType](offertype.md)
  The type of offer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/offerdiscounttype)*