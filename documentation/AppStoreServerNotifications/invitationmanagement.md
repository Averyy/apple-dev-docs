# invitationManagement

**Framework**: App Store Server Notifications  
**Kind**: typealias  
**Role**: Type

A value that indicates whether Apple or your app hosts the invitations to the seats of a multiseat purchase.

**Availability**:
- App Store Server Notifications 2.23+

## Declaration

```
string invitationManagement
```

## Possible Values

- `APPLE`: The subscription uses invitations that Apple hosts.
- `DEVELOPER`: The subscription uses invitations that your app hosts.

## Mentions

- [App Store Server Notifications changelog](./app-store-server-notifications-changelog.md)

## Discussion

When a customer buys your subscription through Group Purchases, the group purchaser invites others to join the group. In App Store Connect, you choose whether Apple or your app hosts these invitations. The `invitationManagement` value of a subscription transaction reflects the setting at the time of purchase. If you change the setting, the change applies to new subscriptions and resubscribes only; existing active subscriptions keep the value they have.

The value determines how members get access:

- For a subscription with a value of `APPLE`, Apple hosts the invitations and manages the group’s membership. Each member receives their own transaction, with an [`inAppOwnershipType`](./inappownershiptype.md) of `ASSIGNED`.
- For a subscription with a value of `DEVELOPER`, your app hosts the invitations and manages the group’s membership. The purchaser is the only member who receives a transaction, so your server keeps the record of other members who have access. Use the [`Get Seat Info`](../AppStoreServerAPI/get-seat-info.md), [`Claim Seat`](../AppStoreServerAPI/claim-seat.md), [`Unclaim Seat`](../AppStoreServerAPI/unclaim-seat.md), and [`Associate Seat`](../AppStoreServerAPI/associate-seat.md) endpoints to report and look up which seats are occupied.

## See Also

### Multiseat purchases
- [object TransactionMultiSeatInfo](./transactionmultiseatinfo.md)
  Information about the seats in a transaction for a subscription that a customer buys as a multiseat purchase.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/invitationmanagement)*