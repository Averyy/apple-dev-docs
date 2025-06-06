# offerIdentifier

**Framework**: App Store Server Notifications  
**Kind**: typealias

The string identifier of a subscription offer that you create in App Store Connect.

**Availability**:
- App Store Server Notifications 2.0+

## Declaration

```swift
string offerIdentifier
```

#### Discussion

The `offerIdentifier` is a string that you provide in App Store Connect when you set up a subscription offer. All offer types ([`offerType`](offertype.md)) have offer identifiers, except for introductory offers.

For more information on offer codes, see [`Supporting subscription offer codes in your app`](https://developer.apple.com/documentation/StoreKit/supporting-subscription-offer-codes-in-your-app) and [`Set up offer codes`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/dev6a098e4b1). For more information on promotional offers, see [`Set up promotional offers for auto-renewable subscriptions`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/dev16dfca448).

## See Also

- [type eligibleWinBackOfferIds](eligiblewinbackofferids.md)
  An array of win-back offer identifiers that a customer is eligible to redeem, which sorts the identifiers to present the better offers first.
- [type offerPeriod](offerperiod.md)
  The duration of the offer.
- [type offerType](offertype.md)
  The type of subscription offer.
- [type offerDiscountType](offerdiscounttype.md)
  The payment mode for a subscription offer for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/offeridentifier)*