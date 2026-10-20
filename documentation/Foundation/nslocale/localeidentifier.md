# localeIdentifier

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, readonly) NSString * localeIdentifier;
```

#### Discussion

Examples of locale identifiers include `"en_GB"`, `"es_ES_PREEURO"`, and `"zh-Hant_HK_POSIX@collation=pinyin;currency=CNY"`.

Use [`localizedString(forIdentifier:)`](../locale/localizedstring%28foridentifier%29.md) to obtain a version of the value suitable for display to the user.

> **Note**:  The value held in the property may differ from the identifier used to initialize the locale because [`NSLocale`](../nslocale.md) may canonicalize it during initialization.

This property contains the same value returned by the [`object(forKey:)`](./object%28forkey%29.md) method when passing the [`identifier`](./key/identifier.md) key.

## See Also

### Related Documentation
- [class var availableLocaleIdentifiers: [String]](./availablelocaleidentifiers.md)
  The list of locale identifiers available on the system.
### Getting Information About a Locale
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
- [var currencyCode: String?](./currencycode.md)
  The currency code for the locale.
- [var currencySymbol: String](./currencysymbol.md)
  The currency symbol for the locale.
- [var calendarIdentifier: String](./calendaridentifier.md)
  The calendar identifier for the locale.
- [var quotationBeginDelimiter: String](./quotationbegindelimiter.md)
  The begin quotation symbol for the locale.
- [var quotationEndDelimiter: String](./quotationenddelimiter.md)
  The end quotation symbol for the locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale/localeidentifier)*