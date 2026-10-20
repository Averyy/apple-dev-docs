# merchantCapabilities

**Framework**: Apple Pay on the Web  
**Kind**: property  
**Role**: Instance Property

An array of the payment capabilities that the merchant supports, such as credit or debit.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```
required sequence <ApplePayMerchantCapability> merchantCapabilities;
```

#### Discussion

The supported values for `merchantCapabilities` are:

- `supports3DS` - Required. This value must be supplied.
- `supportsCredit` - Optional. If present,  only transactions that are categorized as credit cards are allowed.
- `supportsDebit` - Optional. If present, only transactions that are categorized as debit cards are allowed.
- `supportsEMV` - Include this value only if you support China Union Pay transactions.

If both or neither `supportsCredit` and `supportsDebit` values are supplied, the transaction allows both credit and debit cards.

## See Also

### Working with transaction information
- [countryCode](./countrycode.md)
  The merchant’s two-letter ISO 3166 country code.
- [currencyCode](./currencycode.md)
  The three-letter ISO 4217 currency code for the payment.
- [shippingMethods](./shippingmethods.md)
  The list of shipping methods available for a payment request.
- [shippingType](./shippingtype.md)
  An optional value that indicates how to ship purchased items.
- [supportedCountries](./supportedcountries.md)
  A list of two-letter country codes for limiting payment to cards from specific countries or regions.
- [supportedNetworks](./supportednetworks.md)
  The payment networks the merchant supports.
- [ApplePayMerchantCapability](../applepaymerchantcapability.md)
  The payment capabilities the merchant supports.
- [ApplePayShippingMethod](../applepayshippingmethod.md)
  A dictionary that describes the shipping method for delivering physical goods.
- [ApplePayShippingType](../applepayshippingtype.md)
  A type that indicates how to ship purchased items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymentrequest/merchantcapabilities)*