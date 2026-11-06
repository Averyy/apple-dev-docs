# MultiSeatPriceTier

**Framework**: App Store Server API  
**Kind**: dictionary  
**Role**: Object

A price per seat, and the number of seats at that price, in a subscription that a customer buys as a multiseat purchase.

**Availability**:
- App Store Server API 1.23+

## Declaration

```
object MultiSeatPriceTier
```

## Mentions

- [App Store Server API changelog](./app-store-server-api-changelog.md)

## Discussion

A subscription with volume discount pricing charges a lower price per seat as the number of seats increases. Each `MultiSeatPriceTier` describes the seats at a given price tier.

The `priceTiers` array of [`TransactionMultiSeatInfo`](./transactionmultiseatinfo.md) and the `renewalPriceTiers` array of [`RenewalMultiSeatInfo`](./renewalmultiseatinfo.md) contain these tiers. Each `price` uses the [`currency`](./currency.md) of the transaction or renewal information that contains the tier.

## Topics

### Tier information
- [type tierPrice](./tierprice.md)
  The price per seat, in milliunits, for a price tier of a subscription that a customer buys as a multiseat purchase.
- [type tierQuantity](./tierquantity.md)
  The number of seats at the price of a price tier.

## Properties

- `price` (tierPrice): The price per seat, in milliunits of the currency, for this tier.
- `quantity` (tierQuantity): The number of seats at this tier’s price.

## See Also

### Multiseat purchases
- [object TransactionMultiSeatInfo](./transactionmultiseatinfo.md)
  Information about the seats in a transaction for a subscription that a customer buys as a multiseat purchase.
- [type invitationManagement](./invitationmanagement.md)
  A value that indicates whether Apple or your app hosts the invitations to the seats of a multiseat purchase.
- [type additionalTransactionReason](./additionaltransactionreason.md)
  The reason that more than one transaction represents a subscription period.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/multiseatpricetier)*