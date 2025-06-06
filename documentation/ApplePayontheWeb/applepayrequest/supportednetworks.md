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

## Mentions

- [Apple Pay on the Web Version 13 Release Notes](apple-pay-on-the-web-version-13-release-notes.md)
- [Apple Pay on the Web Version 11 Release Notes](apple-pay-on-the-web-version-11-release-notes.md)
- [Apple Pay on the Web Version 5 Release Notes](apple-pay-on-the-web-version-5-release-notes.md)
- [Apple Pay on the Web Version 14 Release Notes](apple-pay-on-the-web-version-14-release-notes.md)
- [Apple Pay on the Web Version 4 Release Notes](apple-pay-on-the-web-version-4-release-notes.md)
- [Apple Pay on the Web Version 2 Release Notes](apple-pay-on-the-web-version-2-release-notes.md)

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

To use a network introduced with a specific Apple Pay version, set the [`version`](applepayrequest/version.md) parameter to the required version number. For the best compatibility with operating systems and browsers, select the lowest possible version number that supports your payment networks and other required features.

In macOS 12.3, iOS 15.4, watchOS 8.5, and Mac Catalyst 15.4 or later, specify payment methods in the order you prefer. For example, to specify the default network to use for cobadged cards, set the first element in the array to the default network, and alternate networks afterward in the order you prefer.

> **Note**:  Websites supporting debit networks should check for regional regulations. For more information, see [`Complying with regional regulations`](https://developer.apple.com/documentation/PassKit/complying-with-regional-regulations).

## See Also

- [countryCode](applepayrequest/countrycode.md)
  The merchant’s two-letter ISO 3166 country code.
- [merchantCapabilities](applepayrequest/merchantcapabilities.md)
  An array of the payment capabilities the merchant supports, such as credit or debit.
- [supportedCountries](applepayrequest/supportedcountries.md)
  A list of two-letter country codes for limiting payment to cards from specific countries or regions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ApplePayontheWeb/applepayrequest/supportednetworks)*