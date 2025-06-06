# offerPeriod

**Framework**: App Store Server API  
**Kind**: typealias

The duration of the offer.

**Availability**:
- App Store Server API 1.15+

## Declaration

```swift
string offerPeriod
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

This field is in ISO 8601 duration format.

The following table shows examples of offer period values.

| Single period length | Period count | Offer period value |
| --- | --- | --- |
| 1 month | 1 | `P1M` |
| 1 month | 2 | `P2M` |
| 3 days | 1 | `P3D` |

## See Also

- [type eligibleWinBackOfferIds](eligiblewinbackofferids.md)
  An array of win-back offer identifiers that a customer is eligible to redeem, which sorts the identifiers with the best offers first.
- [type offerIdentifier](offeridentifier.md)
  The string identifier of a subscription offer that you create in App Store Connect.
- [type offerType](offertype.md)
  The type of subscription offer.
- [type offerDiscountType](offerdiscounttype.md)
  The payment mode for subscription offers on an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/offerperiod)*