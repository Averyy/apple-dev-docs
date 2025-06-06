# offerDiscountType

**Framework**: App Store Server Notifications  
**Kind**: typealias

The payment mode for a subscription offer for an auto-renewable subscription.

**Availability**:
- App Store Server Notifications 2.9+

## Declaration

```swift
string offerDiscountType
```

## Mentions

- [App Store Server Notifications changelog](app-store-server-notifications-changelog.md)

#### Discussion

You set up subscription offers and determine the payment mode when you configure subscriptions in App Store Connect. For more information about the Free Trial, Pay As You Go, and Pay Up Front payment modes, see [`Pricing and availability`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/pricing-and-availability).

For more information about configuring subscription offers, see: [`Set up introductory offers for auto-renewable subscriptions`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-introductory-offers-for-auto-renewable-subscriptions), [`Set up promotional offers for auto-renewable subscriptions`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-promotional-offers-for-auto-renewable-subscriptions), and [`Set up offer codes`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-offer-codes).

## See Also

- [type eligibleWinBackOfferIds](eligiblewinbackofferids.md)
  An array of win-back offer identifiers that a customer is eligible to redeem, which sorts the identifiers to present the better offers first.
- [type offerIdentifier](offeridentifier.md)
  The string identifier of a subscription offer that you create in App Store Connect.
- [type offerPeriod](offerperiod.md)
  The duration of the offer.
- [type offerType](offertype.md)
  The type of subscription offer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/offerdiscounttype)*