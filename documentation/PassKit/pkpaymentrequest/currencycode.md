# currencyCode

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The three-letter ISO 4217 currency code that determines the currency the payment request uses.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var currencyCode: String { get set }
```

```objc
@property (nonatomic, copy) NSString * currencyCode;
```

#### Discussion

Set this property to the three-letter code for the currency used by this payment request. Apple Pay interprets the amounts provided by the summary items attached to this request as amounts in this currency.

The framework translates the currency code from the alphabetic code to the corresponding numeric code. The numeric code is passed to the Secure Element and appears in the encrypted payment data. For more information on the Secure Element, see [A Payment Token Is Created When a Payment Is Authorized](https://developer.apple.com/library/archive/ApplePay_Guide/Authorization.html#//apple_ref/doc/uid/TP40014764-CH4-SW4) in [Apple Pay Programming Guide](https://developer.apple.com/library/archive/ApplePay_Guide/index.html#//apple_ref/doc/uid/TP40014764).

## See Also

### Setting currency and region information
- [var supportedCountries: Set<String>?](./supportedcountries.md)
  A list of ISO 3166 country codes to limit payments to cards from specific countries or regions.
- [var countryCode: String](./countrycode.md)
  The merchant’s two-letter ISO 3166 country code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequest/currencycode)*