# refundAmount

**Framework**: Advanced Commerce API  
**Kind**: typealias

A refund amount, in milliunits of the currency.

**Availability**:
- Advanced Commerce API 1.1+

## Declaration

```swift
integer refundAmount
```

#### Discussion

When you supply a requested refund amount, include the tax for all regions, except for Canada and the United States.

## See Also

- [type currency](currency.md)
  The three-letter ISO 4217 currency code for the price of a product.
- [type description](description.md)
  A string you provide that describes a SKU.
- [type dependentSKU](dependentsku.md)
  The product identifier of a dependent SKU in a subscription price change.
- [type displayName](displayname.md)
  A string with a product name that you can localize and is suitable for display to customers.
- [type effective](effective.md)
  A string value that indicates when a requested change to an auto-renewable subscription goes into effect.
- [type period](period.md)
  The duration of a single cycle of an auto-renewable subscription.
- [type price](price.md)
  A price, in milliunits of a currency, for an Advanced Commerce API SKU.
- [type proratedPrice](proratedprice.md)
  A prorated price, in milliunits of a currency, for an Advanced Commerce API SKU.
- [type retainBillingCycle](retainbillingcycle.md)
  A Boolean value that determines whether to keep the existing billing cycle with the change you request.
- [type refundReason](refundreason.md)
  A reason to request a refund.
- [type refundRiskingPreference](refundriskingpreference.md)
  A Boolean value that indicates whether the App Store asks you for consumption data to help inform the refund decision.
- [type SKU](sku.md)
  The product identifier of an in-app purchase product you manage in your own system.
- [type storefront](storefront.md)
  A three-letter code that represents the country or region associated with the App Store storefront.
- [type taxCode](taxcode.md)
  A tax code that applies to a SKU.
- [type targetProductId](targetproductid.md)
  A generic product identifier that represents all Advanced Commerce API products to App Store Connect, which you use when you migrate a product.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/refundamount)*