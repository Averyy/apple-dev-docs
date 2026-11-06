# tierPrice

**Framework**: App Store Server API  
**Kind**: typealias  
**Role**: Type

The price per seat, in milliunits, for a price tier of a subscription that a customer buys as a multiseat purchase.

**Availability**:
- App Store Server API 1.23+

## Declaration

```
int64 tierPrice
```

## Mentions

- [App Store Server API changelog](./app-store-server-api-changelog.md)

## Discussion

This value represents the price per seat, in milliunits of the [`currency`](./currency.md), for the seats in a [`MultiSeatPriceTier`](./multiseatpricetier.md). One unit of the currency equals 1000 milliunits. For examples, see [`price`](./price.md).

> ❗ **Important**:  Don’t use this value or the `currency` for revenue reconciliation or recognition. App Store Connect reporting is your source of record for financial and accounting purposes. For more information, see [Download financial reports](https://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports) and [Overview of reporting tools](https://developer.apple.com/help/app-store-connect/measure-app-performance/overview-of-reporting-tools).

## See Also

### Multiseat purchases
- [object TransactionMultiSeatInfo](./transactionmultiseatinfo.md)
  Information about the seats in a transaction for a subscription that a customer buys as a multiseat purchase.
- [type invitationManagement](./invitationmanagement.md)
  A value that indicates whether Apple or your app hosts the invitations to the seats of a multiseat purchase.
- [type additionalTransactionReason](./additionaltransactionreason.md)
  The reason that more than one transaction represents a subscription period.
- [object MultiSeatPriceTier](./multiseatpricetier.md)
  A price per seat, and the number of seats at that price, in a subscription that a customer buys as a multiseat purchase.
- [type tierQuantity](./tierquantity.md)
  The number of seats at the price of a price tier.
- [type revokedSeatQuantity](./revokedseatquantity.md)
  The number of seats in a transaction that a seat-based refund revoked.
- [object RenewalMultiSeatInfo](./renewalmultiseatinfo.md)
  Information about the seats in the next renewal of a subscription that renews as a multiseat purchase.
- [type renewalQuantity](./renewalquantity.md)
  The number of seats in the next renewal of an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/tierprice)*