# supportedNetworks

**Framework**: Applepayontheweb  
**Kind**: property

The payment networks the merchant supports.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
required sequence <DOMString> supportedNetworks;
```

#### Discussion

You must set this property to one or more of the payment network values in the following table:

| Payment network | Apple Pay version where first available |
| --- | --- |
| `amex` | 1 |
| `bancomat` | 14 |
| `bancontact` | 14 |
| `cartesBancaires` | 4 |
| `chinaUnionPay` | 1 |
| `dankort` | 13 |
| `discover` | 1 |
| `eftpos` | 4 |
| `electron` | 4 |
| `elo` | 5 |
| `girocard` | 11 |
| `interac` | 1 |
| `jcb` | 2 |
| `mada` | 5 |
| `maestro` | 4 |
| `masterCard` | 1 |
| `mir` | 11 |
| `privateLabel` | 1 |
| `visa` | 1 |
| `vPay` | 4 |

To use a network introduced with a specific Apple Pay version, set the [`ApplePaySession`](applepaysession/applepaysession.md) version parameter to the required version number, like this:

```swift
var session = new ApplePaySession(2, paymentRequest);
```

For the best compatibility with operating systems and browsers, use the lowest possible version number that supports your payment networks and other required features.

In macOS 12.3, iOS 15.4, watchOS 8.5, and Mac Catalyst 15.4 or later, specify payment methods in the order you prefer. For example, to specify the default network to use for cobadged cards, set the first element in the array to the default network, and alternate networks afterward in the order you prefer.

> **Note**:  Websites supporting debit networks should check for regional regulations. For more information, see [`Complying with regional regulations`](https://developer.apple.com/documentation/PassKit/complying-with-regional-regulations).

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
- [ApplePayMerchantCapability](applepaymerchantcapability.md)
  The payment capabilities the merchant supports.
- [ApplePayShippingMethod](applepayshippingmethod.md)
  A dictionary that describes the shipping method for delivering physical goods.
- [ApplePayShippingType](applepayshippingtype.md)
  A type that indicates how to ship purchased items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ApplePayontheWeb/applepaypaymentrequest/supportednetworks)*