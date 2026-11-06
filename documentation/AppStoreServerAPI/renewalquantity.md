# renewalQuantity

**Framework**: App Store Server API  
**Kind**: typealias  
**Role**: Type

The number of seats in the next renewal of an auto-renewable subscription.

**Availability**:
- App Store Server API 1.23+

## Declaration

```
int32 renewalQuantity
```

## Mentions

- [App Store Server API changelog](./app-store-server-api-changelog.md)

## Discussion

The group purchaser manages the number of seats. Seats they add take effect immediately, and a reduction takes effect at the next renewal date. The group purchaser can change the number of seats that renew more than once before the subscription renews, so read `renewalQuantity` from the latest renewal information, for example by calling the [`Get All Subscription Statuses`](./get-all-subscription-statuses.md) endpoint, rather than tracking the changes yourself.

For the notifications the App Store sends when the number of seats changes, see the `INCREASE_QUANTITY` and `DECREASE_QUANTITY` values of [`subtype`](../AppStoreServerNotifications/subtype.md).

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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/renewalquantity)*