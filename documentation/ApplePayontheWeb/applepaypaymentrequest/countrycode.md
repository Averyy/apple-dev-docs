# countryCode

**Framework**: Apple Pay on the Web  
**Kind**: property

The merchant’s two-letter ISO 3166 country code.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
required DOMString countryCode;
```

#### Discussion

Set this property to the two-letter ISO 3166 code for the country or region of the merchant’s principle place of business. This is often the location for settling the payment. Consult with your payment service provider (PSP) to determine the appropriate country code.

Apple Pay may use the `countryCode` to generate payment data that complies with local regulations. For more information on regional compliance, see [`Complying with regional regulations`](https://developer.apple.com/documentation/PassKit/complying-with-regional-regulations).

## See Also

- [currencyCode](applepaypaymentrequest/currencycode.md)
  The three-letter ISO 4217 currency code for the payment.
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

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymentrequest/countrycode)*