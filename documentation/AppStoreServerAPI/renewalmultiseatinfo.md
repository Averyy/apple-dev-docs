# RenewalMultiSeatInfo

**Framework**: App Store Server API  
**Kind**: dictionary  
**Role**: Object

Information about the seats in the next renewal of a subscription that renews as a multiseat purchase.

**Availability**:
- App Store Server API 1.23+

## Declaration

```
object RenewalMultiSeatInfo
```

## Mentions

- [App Store Server API changelog](./app-store-server-api-changelog.md)

## Discussion

The [`JWSRenewalInfoDecodedPayload`](./jwsrenewalinfodecodedpayload.md) contains a `multiSeatInfo` object only if the subscription renews as a multiseat purchase. The [`renewalQuantity`](./renewalquantity.md) field in the same payload contains the number of seats that renew.

Each [`MultiSeatPriceTier`](./multiseatpricetier.md) in the `renewalPriceTiers` array contains a price per seat and the number of seats at that price. To calculate a total from the tiers, multiply the price of each tier by its quantity, and then add the results. For a multiseat purchase, [`renewalPrice`](./renewalprice.md) is the average price per seat.

## Topics

### Seat information
- [object MultiSeatPriceTier](./multiseatpricetier.md)
  A price per seat, and the number of seats at that price, in a subscription that a customer buys as a multiseat purchase.
- [type renewalQuantity](./renewalquantity.md)
  The number of seats in the next renewal of an auto-renewable subscription.

## Properties

- `renewalPriceTiers` ([MultiSeatPriceTier]): An array of price tiers, each containing a price per seat and the number of seats at that price for the next renewal.

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
- [type renewalQuantity](./renewalquantity.md)
  The number of seats in the next renewal of an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/renewalmultiseatinfo)*