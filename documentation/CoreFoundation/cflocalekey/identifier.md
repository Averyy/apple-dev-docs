# identifier

**Framework**: Core Foundation  
**Kind**: property

Specifies locale identifier.

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
static let identifier: CFLocaleKey!
```

#### Discussion

The corresponding value is a CFString containing the POSIX locale identifier as used by ICU, such as “`ja_JP`”. If you have a variant locale or a different currency or calendar, it can be as complex as “`en_US_POSIX@calendar=japanese;currency=EUR`” or “`az_Cyrl_AZ@calendar=buddhist;currency=JPY`”.

## See Also

- [static let languageCode: CFLocaleKey!](cflocalekey/languagecode.md)
  Specifies the locale language code.
- [static let countryCode: CFLocaleKey!](cflocalekey/countrycode.md)
  Specifies the locale country code.
- [static let scriptCode: CFLocaleKey!](cflocalekey/scriptcode.md)
  Specifies the locale script code.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cflocalekey/identifier)*