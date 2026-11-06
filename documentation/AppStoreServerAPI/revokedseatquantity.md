# revokedSeatQuantity

**Framework**: App Store Server API  
**Kind**: typealias  
**Role**: Type

The number of seats in a transaction that a seat-based refund revoked.

**Availability**:
- App Store Server API 1.23+

## Declaration

```
int32 revokedSeatQuantity
```

## Mentions

- [App Store Server API changelog](./app-store-server-api-changelog.md)

## Discussion

A seat-based refund revokes some of the seats in a subscription that a customer buys as a multiseat purchase, without revoking the transaction. The transaction remains valid for its remaining seats. When a seat-based refund applies to a transaction, the App Store sends a `REFUND` notification with a `subtype` of `SEATS`. For more information, see [`subtype`](../AppStoreServerNotifications/subtype.md).

Only the group purchaser’s transaction contains `revokedSeatQuantity`. Don’t revoke the group purchaser’s access because of this value. Revoke it only when every transaction in the period contains revocation fields, such as [`revocationDate`](./revocationdate.md).

- For a subscription with an [`invitationManagement`](./invitationmanagement.md) value of `APPLE`, you don’t need to act on this value; the App Store reduces the number of seats the group purchaser can assign.
- For a subscription with a value of `DEVELOPER`, use this value to update your record of the number of seats, or call the [`Get Seat Info`](./get-seat-info.md) endpoint to get the current [`totalSeatCount`](./totalseatcount.md).

The [`TransactionMultiSeatInfo`](./transactionmultiseatinfo.md) object contains this value when a seat-based refund applies to the transaction. If a refund covers seats from more than one transaction in the period, each of those transactions reports its own `revokedSeatQuantity`, and you receive a notification for each one. If every seat in the transaction is revoked, the transaction contains revocation fields, such as [`revocationDate`](./revocationdate.md), instead of `revokedSeatQuantity`.

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
- [type tierPrice](./tierprice.md)
  The price per seat, in milliunits, for a price tier of a subscription that a customer buys as a multiseat purchase.
- [type tierQuantity](./tierquantity.md)
  The number of seats at the price of a price tier.
- [object RenewalMultiSeatInfo](./renewalmultiseatinfo.md)
  Information about the seats in the next renewal of a subscription that renews as a multiseat purchase.
- [type renewalQuantity](./renewalquantity.md)
  The number of seats in the next renewal of an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/revokedseatquantity)*