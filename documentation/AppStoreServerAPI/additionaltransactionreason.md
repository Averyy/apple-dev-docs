# additionalTransactionReason

**Framework**: App Store Server API  
**Kind**: typealias  
**Role**: Type

The reason that more than one transaction represents a subscription period.

**Availability**:
- App Store Server API 1.23+

## Declaration

```
string additionalTransactionReason
```

## Possible Values

- `SEAT_ADDITION`: The group purchaser added seats to the subscription during the period.

## Mentions

- [App Store Server API changelog](./app-store-server-api-changelog.md)

## Discussion

When a group purchaser adds seats to a subscription during a subscription period, the App Store creates an additional transaction for the added seats. The additional transaction doesn’t replace the existing one. Every transaction that represents the period contains an `additionalTransactionReason`, including the transaction that existed before the group purchaser added seats. This field is absent when a single transaction represents the period.

To determine the number of seats for the period, add the [`quantity`](./quantity.md) of each transaction in the period, excluding any seats that a refund revoked. For more information about revoked seats, see [`revokedSeatQuantity`](./revokedseatquantity.md). To get the transactions for the period, use [App Store Server Notifications](../AppStoreServerNotifications/AppStoreServerNotifications.md) or call the [`Get Transaction History`](./get-transaction-history.md) endpoint. For an active subscription with developer-hosted invitations, you can also call the [`Get Seat Info`](./get-seat-info.md) endpoint. Its [`totalSeatCount`](./totalseatcount.md) is the number of seats in the current period. The group purchaser keeps access unless every transaction in the period is revoked.

## See Also

### Multiseat purchases
- [object TransactionMultiSeatInfo](./transactionmultiseatinfo.md)
  Information about the seats in a transaction for a subscription that a customer buys as a multiseat purchase.
- [type invitationManagement](./invitationmanagement.md)
  A value that indicates whether Apple or your app hosts the invitations to the seats of a multiseat purchase.
- [object MultiSeatPriceTier](./multiseatpricetier.md)
  A price per seat, and the number of seats at that price, in a subscription that a customer buys as a multiseat purchase.
- [type tierPrice](./tierprice.md)
  The price per seat, in milliunits, for a price tier of a subscription that a customer buys as a multiseat purchase.
- [type tierQuantity](./tierquantity.md)
  The number of seats at the price of a price tier.
- [type revokedSeatQuantity](./revokedseatquantity.md)
  The number of seats in a transaction that a seat-based refund revoked.
- [object RenewalMultiSeatInfo](./renewalmultiseatinfo.md)
  Information about the seats in the next renewal of a subscription that renews as a multiseat purchase.
- [type renewalQuantity](./renewalquantity.md)
  The number of seats in the next renewal of an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/additionaltransactionreason)*