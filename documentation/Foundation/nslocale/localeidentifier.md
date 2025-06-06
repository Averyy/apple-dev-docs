# localeIdentifier

**Framework**: Foundation  
**Kind**: property

The identifier for the locale.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var localeIdentifier: String { get }
```

#### Discussion

Examples of locale identifiers include `"en_GB"`, `"es_ES_PREEURO"`, and `"zh-Hant_HK_POSIX@collation=pinyin;currency=CNY"`.

Use [`localizedString(forIdentifier:)`](locale/localizedstring(foridentifier:).md) to obtain a version of the value suitable for display to the user.

> **Note**:  The value held in the property may differ from the identifier used to initialize the locale because [`NSLocale`](nslocale.md) may canonicalize it during initialization.

 The value held in the property may differ from the identifier used to initialize the locale because [`NSLocale`](nslocale.md) may canonicalize it during initialization.

This property contains the same value returned by the [`object(forKey:)`](nslocale/object(forkey:).md) method when passing the [`identifier`](nslocale/key/identifier.md) key.

## See Also

- [class var availableLocaleIdentifiers: [String]](nslocale/availablelocaleidentifiers.md)
  The list of locale identifiers available on the system.
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
- [var calendarIdentifier: String](nslocale/calendaridentifier.md)
  The calendar identifier for the locale.
- [var quotationBeginDelimiter: String](nslocale/quotationbegindelimiter.md)
  The begin quotation symbol for the locale.
- [var quotationEndDelimiter: String](nslocale/quotationenddelimiter.md)
  The end quotation symbol for the locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale/localeidentifier)*