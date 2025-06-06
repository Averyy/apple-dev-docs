# Locale Property Keys

**Framework**: Core Foundation

Predefined locale keys used to get property values.

#### Overview

Locale objects use key-value pairs to store property values. Use the [`CFLocaleGetValue(_:_:)`](cflocalegetvalue(_:_:).md) function to get the value of a specific property listed above.

## Topics

### Constants
- [static let identifier: CFLocaleKey!](cflocalekey/identifier.md)
  Specifies locale identifier.
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
- [static let quotationBeginDelimiterKey: CFLocaleKey!](cflocalekey/quotationbegindelimiterkey.md)
  Specifies the begin quotation symbol associated with the locale.
- [static let quotationEndDelimiterKey: CFLocaleKey!](cflocalekey/quotationenddelimiterkey.md)
  Specifies the end quotation symbol associated with the locale.
- [static let alternateQuotationBeginDelimiterKey: CFLocaleKey!](cflocalekey/alternatequotationbegindelimiterkey.md)
  Specifies the alternating begin quotation symbol associated with the locale. In some locales, when quotations are nested, the quotation characters alternate. Thus, `NSLocaleQuotationBeginDelimiterKey`, then `NSLocaleAlternateQuotationBeginDelimiterKey`, and so on.
- [static let alternateQuotationEndDelimiterKey: CFLocaleKey!](cflocalekey/alternatequotationenddelimiterkey.md)
  Specifies the alternating end quotation symbol associated with the locale. In some locales, when quotations are nested, the quotation characters alternate. Thus, `NSLocaleQuotationEndDelimiterKey`, then `NSLocaleAlternateQuotationEndDelimiterKey`, and so on.

## See Also

- [enum CFLocaleLanguageDirection](cflocalelanguagedirection.md)
  These constants describe the text direction for a language. They are returned by the functions [`CFLocaleGetLanguageCharacterDirection(_:)`](cflocalegetlanguagecharacterdirection(_:).md) and [`CFLocaleGetLanguageLineDirection(_:)`](cflocalegetlanguagelinedirection(_:).md).
- [Locale Calendar Identifiers](locale-calendar-identifiers.md)
  Predefined locale keys used to get calendar values—values for `kCFLocaleCalendarIdentifier`.
- [Locale Change Notification](locale-change-notification.md)
  Identifier for notification sent if the current locale changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/locale-property-keys)*