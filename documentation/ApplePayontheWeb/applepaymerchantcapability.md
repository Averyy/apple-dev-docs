# ApplePayMerchantCapability

**Framework**: Apple Pay on the Web  
**Kind**: enum

The payment capabilities the merchant supports.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
enum ApplePayMerchantCapability
```

#### Overview

Values for merchant capability are:

| `"supports3DS"` | Required. This value must be supplied. |
| --- | --- |
| `"supportsEMV"` | Include this value only if you support China Union Pay transactions. |
| `"supportsCredit"` | Optional. If present,  only transactions that are categorized as credit cards are allowed. |
| `"supportsDebit"` | Optional. If present, only transactions that are categorized as debit cards are allowed. |

## Topics

### Enumeration Cases
- [supports](applepaymerchantcapability/supports.md)
- [supportsCredit](applepaymerchantcapability/supportscredit.md)
- [supportsDebit](applepaymerchantcapability/supportsdebit.md)
- [supportsEMV](applepaymerchantcapability/supportsemv.md)

## See Also

- [countryCode](applepaypaymentrequest/countrycode.md)
  The merchant’s two-letter ISO 3166 country code.
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
- [ApplePayShippingMethod](applepayshippingmethod.md)
  A dictionary that describes the shipping method for delivering physical goods.
- [ApplePayShippingType](applepayshippingtype.md)
  A type that indicates how to ship purchased items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaymerchantcapability)*