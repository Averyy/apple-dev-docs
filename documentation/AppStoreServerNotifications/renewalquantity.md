# renewalQuantity

**Framework**: App Store Server Notifications  
**Kind**: typealias  
**Role**: Type

The number of seats in the next renewal of an auto-renewable subscription.

**Availability**:
- App Store Server Notifications 2.23+

## Declaration

```
int32 renewalQuantity
```

## Mentions

- [App Store Server Notifications changelog](./app-store-server-notifications-changelog.md)

## Discussion

The group purchaser chooses the number of seats that renew. Seats that the group purchaser adds take effect immediately, and the subscription renews with the new number of seats. When the group purchaser reduces the number of seats, or undoes all or part of an earlier reduction, the change takes effect at the next renewal date.

For information about the notifications the App Store sends when the number of seats changes, see the `INCREASE_QUANTITY` and `DECREASE_QUANTITY` values of [`subtype`](./subtype.md).

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
- [type revokedSeatQuantity](./revokedseatquantity.md)
  The number of seats in a transaction that a seat-based refund revoked.
- [object RenewalMultiSeatInfo](./renewalmultiseatinfo.md)
  Information about the seats in the next renewal of a subscription that renews as a multiseat purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/renewalquantity)*