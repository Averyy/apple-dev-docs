# storefront

**Framework**: Advanced Commerce API  
**Kind**: typealias

A three-letter code that represents the country or region associated with the App Store storefront.

**Availability**:
- Advanced Commerce API 1.0+

## Declaration

```swift
string storefront
```

##### Discussion

Use an ISO 3166-1 Alpha-3 country code to represent the storefront.

To get storefront information in your app, use [`Storefront`](https://developer.apple.com/documentation/StoreKit/Storefront). Get the [`countryCode`](https://developer.apple.com/documentation/StoreKit/Storefront/countryCode) value of the [`current`](https://developer.apple.com/documentation/StoreKit/Storefront/current) storefront, and use that value for `storefront`. Use [`updates`](https://developer.apple.com/documentation/StoreKit/Storefront/updates) to listen for changes to the storefront.

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
- [type refundAmount](refundamount.md)
  A refund amount, in milliunits of the currency.
- [type refundReason](refundreason.md)
  A reason to request a refund.
- [type refundRiskingPreference](refundriskingpreference.md)
  A Boolean value that indicates whether the App Store asks you for consumption data to help inform the refund decision.
- [type SKU](sku.md)
  The product identifier of an in-app purchase product you manage in your own system.
- [type taxCode](taxcode.md)
  A tax code that applies to a SKU.
- [type targetProductId](targetproductid.md)
  A generic product identifier that represents all Advanced Commerce API products to App Store Connect, which you use when you migrate a product.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/storefront)*