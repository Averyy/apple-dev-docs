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

- [merchantCapabilities](applepayrequest/merchantcapabilities.md)
  An array of the payment capabilities the merchant supports, such as credit or debit.
- [supportedNetworks](applepayrequest/supportednetworks.md)
  The payment networks the merchant supports.
- [supportedCountries](applepayrequest/supportedcountries.md)
  A list of two-letter country codes for limiting payment to cards from specific countries or regions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepayrequest/countrycode)*