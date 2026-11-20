# finalQuantity

**Framework**: Advanced Commerce API  
**Kind**: typealias  
**Role**: Type

The total number of seats for a subscription item that a customer buys as a multiseat purchase.

**Availability**:
- Advanced Commerce API 1.3+

## Declaration

```
int32 finalQuantity
```

## Mentions

- [Creating multiseat purchases](./creating-multiseat-purchases.md)
- [Advanced Commerce API changelog](./changelog.md)



**Minimum**: `1`

## Discussion

> ❗ **Important**: Multiseat purchases are only available in the sandbox environment.

In a [`SubscriptionCreateItem`](./subscriptioncreateitem.md) or [`SubscriptionModifyChangeItem`](./subscriptionmodifychangeitem.md), provide `finalQuantity` together with `seatPriceTiers`; an item that includes one must include the other. Don’t provide `finalQuantity` for an item that has a `price`.

The value is the total number of seats the item has after the request, not the number of seats to add. For example, to add 4 seats to an item that has 8, provide `12`. In a [`SubscriptionModifyChangeItem`](./subscriptionmodifychangeitem.md), the value can’t be lower than the item’s current number of seats.

A price change doesn’t change the number of seats, so [`SubscriptionPriceChangeItem`](./subscriptionpricechangeitem.md) doesn’t include `finalQuantity`.

## See Also

### Data types
- [type currency](./currency.md)
  The three-letter ISO 4217 currency code for the price of a product.
- [type description](./description.md)
  A string you provide that describes a SKU.
- [type dependentSKU](./dependentsku.md)
  The product identifier of a dependent SKU in a subscription price change.
- [type displayName](./displayname.md)
  A string with a product name that you can localize and is suitable for display to customers.
- [type effective](./effective.md)
  A string value that indicates when a requested change to an auto-renewable subscription goes into effect.
- [type period](./period.md)
  The duration of a single cycle of an auto-renewable subscription.
- [type price](./price.md)
  A price, in milliunits of a currency, for an Advanced Commerce API SKU.
- [type proratedPrice](./proratedprice.md)
  A prorated price, in milliunits of a currency, for an Advanced Commerce API SKU.
- [type retainBillingCycle](./retainbillingcycle.md)
  A Boolean value that determines whether to keep the existing billing cycle with the change you request.
- [type revokeSeatQuantity](./revokeseatquantity.md)
  The number of unclaimed seats to revoke from a subscription that a customer buys as a multiseat purchase.
- [type refundAmount](./refundamount.md)
  A refund amount, in milliunits of the currency.
- [type refundReason](./refundreason.md)
  A reason to request a refund.
- [type refundRiskingPreference](./refundriskingpreference.md)
  A Boolean value that indicates whether the App Store asks you for consumption data to help inform the refund decision.
- [type SKU](./sku.md)
  The product identifier of an Apple In-App Purchase product you manage in your own system.
- [type storefront](./storefront.md)
  A three-letter code that represents the country or region associated with the App Store storefront.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/finalquantity)*