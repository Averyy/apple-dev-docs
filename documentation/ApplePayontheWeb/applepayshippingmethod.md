# ApplePayShippingMethod

**Framework**: Apple Pay on the Web  
**Kind**: struct

A dictionary that describes the shipping method for delivering physical goods.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
dictionary ApplePayShippingMethod {
	required DOMString label;
	required DOMString detail;
	required DOMString amount;
	required DOMString identifier;
	ApplePayDateComponentsRange dateComponentsRange;
};
```

## Mentions

- [Apple Pay on the Web Version 12 Release Notes](apple-pay-on-the-web-version-12-release-notes.md)

#### Overview

The Apple Pay sheet displays all the properties of a shipping method except `identifier`. The following listing is an example of a shipping method that shows free shipping.

```javascript
{    
    "label": "Free Shipping",
    "detail": "Arrives in 5 to 7 days",
    "amount": "0.00",
    "identifier": "FreeShip"
}
    
```

## Topics

### Working with shipping method properties
- [label](applepayshippingmethod/label.md)
  A short description of the shipping method.
- [detail](applepayshippingmethod/detail.md)
  Additional description of the shipping method.
- [dateComponentsRange](applepayshippingmethod/datecomponentsrange.md)
  The expected range of dates for shipping or picking up an item.
- [identifier](applepayshippingmethod/identifier.md)
  A client-defined value used to identify this shipping method.
- [amount](applepayshippingmethod/amount.md)
  The nonnegative cost associated with this shipping method.
- [ApplePayDateComponentsRange](applepaydatecomponentsrange.md)
  A dictionary that specifies the start and end dates for a range of time.

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
- [ApplePayShippingType](applepayshippingtype.md)
  A type that indicates how to ship purchased items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepayshippingmethod)*