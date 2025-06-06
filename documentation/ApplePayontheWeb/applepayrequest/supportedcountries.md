# supportedCountries

**Framework**: Apple Pay on the Web  
**Kind**: property

A list of two-letter country codes for limiting payment to cards from specific countries or regions.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
sequence <DOMString> supportedCountries;
```

#### Discussion

Use the list of supported countries or regions to limit payment cards to those issued in specific countries or regions. Indicate the supported countries or regions by using ISO 3166 country codes.

The [`supportedCountries`](applepaypaymentrequest/supportedcountries.md) list doesn’t affect the currency for the transaction, and it applies to all payment cards in Wallet.

## See Also

- [countryCode](applepayrequest/countrycode.md)
  The merchant’s two-letter ISO 3166 country code.
- [merchantCapabilities](applepayrequest/merchantcapabilities.md)
  An array of the payment capabilities the merchant supports, such as credit or debit.
- [supportedNetworks](applepayrequest/supportednetworks.md)
  The payment networks the merchant supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepayrequest/supportedcountries)*