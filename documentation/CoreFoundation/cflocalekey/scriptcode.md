# scriptCode

**Framework**: Core Foundation  
**Kind**: property

Specifies the locale script code.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
static let scriptCode: CFLocaleKey!
```

#### Discussion

The corresponding value is a CFString containing a Unicode script tag (strictly, an ISO 15924 script tag). Usually this is empty (it is for “`ja_JP`”). It may be present for locales where a script  be specified, for example “`uz-Latn-UZ`” vs. “`uz-Cyrl-UZ`” for Uzbek in Latin vs. Cyrillic (in the first case the script code is “`Latn`”, and in the second it is “`Cyrl`”).

## See Also

- [static let identifier: CFLocaleKey!](cflocalekey/identifier.md)
  Specifies locale identifier.
- [static let languageCode: CFLocaleKey!](cflocalekey/languagecode.md)
  Specifies the locale language code.
- [static let countryCode: CFLocaleKey!](cflocalekey/countrycode.md)
  Specifies the locale country code.
- [static let variantCode: CFLocaleKey!](cflocalekey/variantcode.md)
  Specifies the locale variant code.
- [static let exemplarCharacterSet: CFLocaleKey!](cflocalekey/exemplarcharacterset.md)
  Specifies the locale character set.
- [static let calendarIdentifier: CFLocaleKey!](cflocalekey/calendaridentifier.md)
  Specifies the locale calendar identifier.
- [static let calendar: CFLocaleKey!](cflocalekey/calendar.md)
  Specifies the locale calendar.
- [static let collationIdentifier: CFLocaleKey!](cflocalekey/collationidentifier.md)
  Specifies the locale collation identifier.
- [static let usesMetricSystem: CFLocaleKey!](cflocalekey/usesmetricsystem.md)
  Specifies the whether the locale uses the metric system.
- [static let measurementSystem: CFLocaleKey!](cflocalekey/measurementsystem.md)
  Specifies the measurement system used.
- [static let decimalSeparator: CFLocaleKey!](cflocalekey/decimalseparator.md)
  Specifies the decimal point string.
- [static let groupingSeparator: CFLocaleKey!](cflocalekey/groupingseparator.md)
  Specifies the separator string between groups of digits.
- [static let currencySymbol: CFLocaleKey!](cflocalekey/currencysymbol.md)
  Specifies the currency symbol.
- [static let currencyCode: CFLocaleKey!](cflocalekey/currencycode.md)
  Specifies the locale currency code.
- [static let collatorIdentifier: CFLocaleKey!](cflocalekey/collatoridentifier.md)
  Specifies the collation identifier for the locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cflocalekey/scriptcode)*