# TransactionMultiSeatInfo

**Framework**: App Store Server Notifications  
**Kind**: dictionary  
**Role**: Object

Information about the seats in a transaction for a subscription that a customer buys as a multiseat purchase.

**Availability**:
- App Store Server Notifications 2.23+

## Declaration

```
object TransactionMultiSeatInfo
```

## Mentions

- [App Store Server Notifications changelog](./app-store-server-notifications-changelog.md)

## Discussion

The [`JWSTransactionDecodedPayload`](./jwstransactiondecodedpayload.md) contains a `multiSeatInfo` object for a subscription that a customer buys as a multiseat purchase. The transaction’s [`quantity`](./quantity.md) is the number of seats the transaction covers.

Each [`MultiSeatPriceTier`](./multiseatpricetier.md) in the `priceTiers` array contains a price per seat and the number of seats at that price. To calculate a total from the tiers, multiply the price of each tier by its quantity, and then add the results. For a multiseat purchase, the transaction’s [`price`](./price.md) is the average price per seat.

A seat-based refund revokes some of the seats in a transaction without revoking the transaction. The `revokedSeatQuantity` field reports the number of seats that the refund revoked, and the transaction remains valid for its remaining seats. The transaction’s revocation fields, such as [`revocationDate`](./revocationdate.md) and [`revocationType`](./revocationtype.md), appear only when every seat in the transaction is revoked, instead of `revokedSeatQuantity`. When a seat-based refund applies to a transaction, the App Store sends a `REFUND` [`notificationType`](./notificationtype.md) with a [`subtype`](./subtype.md) of `SEATS`.

## Topics

### Seat information
- [invitationManagement](./transactionmultiseatinfo/invitationmanagement.md)
- [object MultiSeatPriceTier](./multiseatpricetier.md)
  A price per seat, and the number of seats at that price, in a subscription that a customer buys as a multiseat purchase.
- [revokedSeatQuantity](./transactionmultiseatinfo/revokedseatquantity.md)

## Properties

- `invitationManagement` (invitationManagement): A value that indicates whether Apple or your app hosts the invitations to the seats of the purchase.
- `priceTiers` ([MultiSeatPriceTier]): An array of price tiers, each containing a price per seat and the number of seats in this transaction at that price.
- `revokedSeatQuantity` (revokedSeatQuantity): The number of seats in this transaction that a seat-based refund revoked.

## See Also

### Multiseat purchases
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
- [type revokedSeatQuantity](./revokedseatquantity.md)
  The number of seats in a transaction that a seat-based refund revoked.
- [object RenewalMultiSeatInfo](./renewalmultiseatinfo.md)
  Information about the seats in the next renewal of a subscription that renews as a multiseat purchase.
- [type renewalQuantity](./renewalquantity.md)
  The number of seats in the next renewal of an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/transactionmultiseatinfo)*