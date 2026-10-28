# identifier

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

The locale identifier.

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
static let identifier: NSLocale.Key
```

```c
extern NSLocaleKey const NSLocaleIdentifier;
```

## Discussion

The corresponding value is an `NSString` object; for example, `"en_GB"`, `"es_ES_PREEURO"`, or `"zh-Hant_HK_POSIX@collation=pinyin;currency=CNY"`.

## See Also

### Keys
- [static let countryCode: NSLocale.Key](./countrycode.md)
  The locale country or region code.
- [static let languageCode: NSLocale.Key](./languagecode.md)
  The locale language code.
- [static let scriptCode: NSLocale.Key](./scriptcode.md)
  The locale script code.
- [static let variantCode: NSLocale.Key](./variantcode.md)
  The locale variant code.
- [static let exemplarCharacterSet: NSLocale.Key](./exemplarcharacterset.md)
  The exemplar character set for the locale.
- [static let calendar: NSLocale.Key](./calendar.md)
  The calendar associated with the locale.
- [static let collationIdentifier: NSLocale.Key](./collationidentifier.md)
  The collation associated with the locale.
- [static let collatorIdentifier: NSLocale.Key](./collatoridentifier.md)
  The collation identifier for the locale.
- [static let usesMetricSystem: NSLocale.Key](./usesmetricsystem.md)
  A flag that indicates whether the locale uses the metric system.
- [static let measurementSystem: NSLocale.Key](./measurementsystem.md)
  The measurement system associated with the locale.
- [static let decimalSeparator: NSLocale.Key](./decimalseparator.md)
  The decimal separator associated with the locale.
- [static let groupingSeparator: NSLocale.Key](./groupingseparator.md)
  The numeric grouping separator associated with the locale.
- [static let currencySymbol: NSLocale.Key](./currencysymbol.md)
  The currency symbol associated with the locale.
- [static let currencyCode: NSLocale.Key](./currencycode.md)
  The currency code associated with the locale.
- [static let quotationEndDelimiterKey: NSLocale.Key](./quotationenddelimiterkey.md)
  The end quotation symbol associated with the locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale/key/identifier)*