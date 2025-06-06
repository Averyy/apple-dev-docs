# currencyCode

**Framework**: Apple Pay on the Web  
**Kind**: property

The three-letter ISO 4217 currency code for the payment.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
required DOMString currencyCode;
```

#### Discussion

Set this property to the three-letter code for the currency used by this payment request. Apple Pay interprets the amounts provided in the summary items of this request as amounts in this currency.

The currency code is validated.

## See Also

- [countryCode](applepaypaymentrequest/countrycode.md)
  The merchant’s two-letter ISO 3166 country code.
- [merchantCapabilities](applepaypaymentrequest/merchantcapabilities.md)
  An array of the payment capabilities that the merchant supports, such as credit or debit.
- [shippingMethods](applepaypaymentrequest/shippingmethods.md)
  The list of shipping methods available for a payment request.
- [shippingType](applepaypaymentrequest/shippingtype.md)
  An optional value that indicates how to ship purchased items.
- [supportedCountries](applepaypaymentrequest/supportedcountries.md)
  A list of two-letter country codes for limiting payment to cards from specific countries or regions.
- [supportedNetworks](applepaypaymentrequest/supportednetworks.md)
  The payment networks the merchant supports.
- [ApplePayMerchantCapability](applepaymerchantcapability.md)
  The payment capabilities the merchant supports.
- [ApplePayShippingMethod](applepayshippingmethod.md)
  A dictionary that describes the shipping method for delivering physical goods.
- [ApplePayShippingType](applepayshippingtype.md)
  A type that indicates how to ship purchased items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymentrequest/currencycode)*