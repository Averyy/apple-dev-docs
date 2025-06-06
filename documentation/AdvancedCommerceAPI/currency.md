# currency

**Framework**: Advanced Commerce API  
**Kind**: typealias

The three-letter ISO 4217 currency code for the price of a product.

**Availability**:
- Advanced Commerce API 1.0+

## Declaration

```swift
string currency
```

## Mentions

- [Creating SKUs for your In-App Purchases](creating-your-purchases.md)
- [Specifying prices for Advanced Commerce SKUs](prices.md)

#### Discussion

The currency property contains an ISO 4217 alpha-3 string that represents the currency of the price of a SKU. You provide a currency value each time you create or modify a purchase transaction.

To get the current storefront’s currency in your app:

- In iOS 15 through iOS 17, check the `Product.priceFormatStyle.currencyCode` of the generic product ID that represents your Advanced Commerce product. For more information, see [`priceFormatStyle`](https://developer.apple.com/documentation/StoreKit/Product/priceFormatStyle).
- In iOS 17 and later, get the currency value using `Storefront.current.currency`.

For a list of regions and currencies that the App Store supports, see [`Financial reports regions and currencies`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/financial-report-regions-and-currencies).

## See Also

- [type description](description.md)
  A string you provide that describes a SKU.
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
- [type refundAmount](refundamount.md)
  A refund amount, in milliunits of the currency.
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
- [type transactionId](transactionid.md)
  A unique identifier that the App Store generates for a transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/currency)*