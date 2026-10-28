# currencyCode

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The currency code for the locale.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var currencyCode: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * currencyCode;
```

## Discussion

Example currency codes include `"USD"`, `"EUR"`, and `"JPY"`.

Use [`localizedString(forCurrencyCode:)`](./localizedstring%28forcurrencycode%29.md) to obtain a version of the value suitable for display to the user.

This property contains the same value returned by the [`object(forKey:)`](./object%28forkey%29.md) method when passing the [`currencyCode`](./key/currencycode.md) key.

## See Also

### Related Documentation
- [class var commonISOCurrencyCodes: [String]](./commonisocurrencycodes.md)
  A list of commonly encountered currency codes.
- [class var isoCurrencyCodes: [String]](./isocurrencycodes.md)
  The list of known currency codes.
### Getting Information About a Locale
- [var localeIdentifier: String](./localeidentifier.md)
  The identifier for the locale.
- [var countryCode: String?](./countrycode.md)
  The country or region code for the locale.
- [var languageCode: String](./languagecode.md)
  The language code for the locale.
- [var scriptCode: String?](./scriptcode.md)
  The script code for the locale.
- [var variantCode: String?](./variantcode.md)
  The variant code for the locale.
- [var exemplarCharacterSet: CharacterSet](./exemplarcharacterset.md)
  The exemplar character set for the locale.
- [var collationIdentifier: String?](./collationidentifier.md)
  The collation identifier for the locale.
- [var collatorIdentifier: String](./collatoridentifier.md)
  The collator identifier for the locale.
- [var usesMetricSystem: Bool](./usesmetricsystem.md)
  A Boolean value that indicates whether the locale uses the metric system.
- [var decimalSeparator: String](./decimalseparator.md)
  The decimal separator for the locale.
- [var groupingSeparator: String](./groupingseparator.md)
  The grouping separator for the locale.
- [var currencySymbol: String](./currencysymbol.md)
  The currency symbol for the locale.
- [var calendarIdentifier: String](./calendaridentifier.md)
  The calendar identifier for the locale.
- [var quotationBeginDelimiter: String](./quotationbegindelimiter.md)
  The begin quotation symbol for the locale.
- [var quotationEndDelimiter: String](./quotationenddelimiter.md)
  The end quotation symbol for the locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale/currencycode)*