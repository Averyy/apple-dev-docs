# dependentSKU

**Framework**: Advanced Commerce API  
**Kind**: typealias  
**Role**: Type

The product identifier of a dependent SKU in a subscription price change.

**Availability**:
- Advanced Commerce API 1.0+

## Declaration

```
string dependentSKU
```



**Maximum Length**: `128`

### Discussion

A dependent SKU is a product identifier that represents an item that depends on another SKU in the context of subscription price changes. Dependent SKUs cannot be chained or shared between multiple parent SKUs.

The dependentSKU value is a string with a maximum length of 128 characters.

## See Also

### Data types
- [type currency](./currency.md)
  The three-letter ISO 4217 currency code for the price of a product.
- [type description](./description.md)
  A string you provide that describes a SKU.
- [type displayName](./displayname.md)
  A string with a product name that you can localize and is suitable for display to customers.
- [type effective](./effective.md)
  A string value that indicates when a requested change to an auto-renewable subscription goes into effect.
- [type finalQuantity](./finalquantity.md)
  The total number of seats for a subscription item that a customer buys as a multiseat purchase.
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

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/dependentsku)*