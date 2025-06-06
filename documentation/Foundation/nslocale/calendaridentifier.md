# calendarIdentifier

**Framework**: Foundation  
**Kind**: property

The calendar identifier for the locale.

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
var calendarIdentifier: String { get }
```

#### Discussion

Possible values are listed in `Calendar Identifiers`.

Use [`localizedString(forCalendarIdentifier:)`](nslocale/localizedstring(forcalendaridentifier:).md) to obtain a version of the value suitable for display to the user.

## See Also

- [var localeIdentifier: String](nslocale/localeidentifier.md)
  The identifier for the locale.
- [var countryCode: String?](nslocale/countrycode.md)
  The country or region code for the locale.
- [var languageCode: String](nslocale/languagecode.md)
  The language code for the locale.
- [var scriptCode: String?](nslocale/scriptcode.md)
  The script code for the locale.
- [var variantCode: String?](nslocale/variantcode.md)
  The variant code for the locale.
- [var exemplarCharacterSet: CharacterSet](nslocale/exemplarcharacterset.md)
  The exemplar character set for the locale.
- [var collationIdentifier: String?](nslocale/collationidentifier.md)
  The collation identifier for the locale.
- [var collatorIdentifier: String](nslocale/collatoridentifier.md)
  The collator identifier for the locale.
- [var usesMetricSystem: Bool](nslocale/usesmetricsystem.md)
  A Boolean value that indicates whether the locale uses the metric system.
- [var decimalSeparator: String](nslocale/decimalseparator.md)
  The decimal separator for the locale.
- [var groupingSeparator: String](nslocale/groupingseparator.md)
  The grouping separator for the locale.
- [var currencyCode: String?](nslocale/currencycode.md)
  The currency code for the locale.
- [var currencySymbol: String](nslocale/currencysymbol.md)
  The currency symbol for the locale.
- [var quotationBeginDelimiter: String](nslocale/quotationbegindelimiter.md)
  The begin quotation symbol for the locale.
- [var quotationEndDelimiter: String](nslocale/quotationenddelimiter.md)
  The end quotation symbol for the locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale/calendaridentifier)*