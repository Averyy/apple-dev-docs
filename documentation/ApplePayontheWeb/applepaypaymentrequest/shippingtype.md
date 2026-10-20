# shippingType

**Framework**: Apple Pay on the Web  
**Kind**: property  
**Role**: Instance Property

An optional value that indicates how to ship purchased items.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```
ApplePayShippingType shippingType;
```

#### Discussion

The shipping type is optional. If it is specified, it must be one or more of these values:

- `shipping`
- `delivery`
- `storePickup`
- `servicePickup`

The default value is `shipping`.

## See Also

### Working with transaction information
- [countryCode](./countrycode.md)
  The merchant’s two-letter ISO 3166 country code.
- [currencyCode](./currencycode.md)
  The three-letter ISO 4217 currency code for the payment.
- [merchantCapabilities](./merchantcapabilities.md)
  An array of the payment capabilities that the merchant supports, such as credit or debit.
- [shippingMethods](./shippingmethods.md)
  The list of shipping methods available for a payment request.
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

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymentrequest/shippingtype)*