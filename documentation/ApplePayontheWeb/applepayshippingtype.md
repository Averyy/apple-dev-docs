# ApplePayShippingType

**Framework**: Apple Pay on the Web  
**Kind**: enum

A type that indicates how to ship purchased items.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
enum ApplePayShippingType
```

#### Overview

Shipping types values are:

- `"shipping"`
- `"delivery"`
- `"storePickup"`
- `"servicePickup"`

## Topics

### Enumeration Cases
- [delivery](applepayshippingtype/delivery.md)
- [servicePickup](applepayshippingtype/servicepickup.md)
- [shipping](applepayshippingtype/shipping.md)
- [storePickup](applepayshippingtype/storepickup.md)

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
- [ApplePayMerchantCapability](applepaymerchantcapability.md)
  The payment capabilities the merchant supports.
- [ApplePayShippingMethod](applepayshippingmethod.md)
  A dictionary that describes the shipping method for delivering physical goods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepayshippingtype)*