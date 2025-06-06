# merchantCapabilities

**Framework**: Apple Pay on the Web  
**Kind**: property

An array of the payment capabilities that the merchant supports, such as credit or debit card payments.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
required sequence <ApplePayMerchantCapability> merchantCapabilities;
```

#### Discussion

The supported values for `merchantCapabilities` are:

- `supports3DS` - Required. This value must be supplied.
- `supportsCredit` - Optional. If present, only transactions that are categorized as credit cards are allowed.
- `supportsDebit` - Optional. If present, only transactions that are categorized as debit cards are allowed.
- `supportsEMV` - Include this value only if you support China Union Pay transactions.

If both or neither `supportsCredit` and `supportsDebit` values are supplied, the transaction allows both credit and debit cards.

## See Also

- [countryCode](applepayrequestbase/countrycode.md)
  The merchant’s two-letter ISO-3166 country code.
- [supportedNetworks](applepayrequestbase/supportednetworks.md)
  The payment networks the merchant provides to their customers.
- [supportedCountries](applepayrequestbase/supportedcountries.md)
  A list of two-letter country codes for limiting payment to credit cards from specific countries or regions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepayrequestbase/merchantcapabilities)*