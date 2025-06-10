# CFLocaleKey

**Framework**: Core Foundation  
**Kind**: struct

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
struct CFLocaleKey
```

## Topics

### Type Properties
- [static let alternateQuotationBeginDelimiterKey: CFLocaleKey!](cflocalekey/alternatequotationbegindelimiterkey.md)
  Specifies the alternating begin quotation symbol associated with the locale. In some locales, when quotations are nested, the quotation characters alternate. Thus, `NSLocaleQuotationBeginDelimiterKey`, then `NSLocaleAlternateQuotationBeginDelimiterKey`, and so on.
- [static let alternateQuotationEndDelimiterKey: CFLocaleKey!](cflocalekey/alternatequotationenddelimiterkey.md)
  Specifies the alternating end quotation symbol associated with the locale. In some locales, when quotations are nested, the quotation characters alternate. Thus, `NSLocaleQuotationEndDelimiterKey`, then `NSLocaleAlternateQuotationEndDelimiterKey`, and so on.
- [static let calendar: CFLocaleKey!](cflocalekey/calendar.md)
  Specifies the locale calendar.
- [static let calendarIdentifier: CFLocaleKey!](cflocalekey/calendaridentifier.md)
  Specifies the locale calendar identifier.
- [static let collationIdentifier: CFLocaleKey!](cflocalekey/collationidentifier.md)
  Specifies the locale collation identifier.
- [static let collatorIdentifier: CFLocaleKey!](cflocalekey/collatoridentifier.md)
  Specifies the collation identifier for the locale.
- [static let countryCode: CFLocaleKey!](cflocalekey/countrycode.md)
  Specifies the locale country code.
- [static let currencyCode: CFLocaleKey!](cflocalekey/currencycode.md)
  Specifies the locale currency code.
- [static let currencySymbol: CFLocaleKey!](cflocalekey/currencysymbol.md)
  Specifies the currency symbol.
- [static let decimalSeparator: CFLocaleKey!](cflocalekey/decimalseparator.md)
  Specifies the decimal point string.
- [static let exemplarCharacterSet: CFLocaleKey!](cflocalekey/exemplarcharacterset.md)
  Specifies the locale character set.
- [static let groupingSeparator: CFLocaleKey!](cflocalekey/groupingseparator.md)
  Specifies the separator string between groups of digits.
- [static let identifier: CFLocaleKey!](cflocalekey/identifier.md)
  Specifies locale identifier.
- [static let languageCode: CFLocaleKey!](cflocalekey/languagecode.md)
  Specifies the locale language code.
- [static let measurementSystem: CFLocaleKey!](cflocalekey/measurementsystem.md)
  Specifies the measurement system used.
- [static let quotationBeginDelimiterKey: CFLocaleKey!](cflocalekey/quotationbegindelimiterkey.md)
  Specifies the begin quotation symbol associated with the locale.
- [static let quotationEndDelimiterKey: CFLocaleKey!](cflocalekey/quotationenddelimiterkey.md)
  Specifies the end quotation symbol associated with the locale.
- [static let scriptCode: CFLocaleKey!](cflocalekey/scriptcode.md)
  Specifies the locale script code.
- [static let usesMetricSystem: CFLocaleKey!](cflocalekey/usesmetricsystem.md)
  Specifies the whether the locale uses the metric system.
- [static let variantCode: CFLocaleKey!](cflocalekey/variantcode.md)
  Specifies the locale variant code.
### Initializers
- [init(rawValue: CFString)](cflocalekey/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [typealias CFAllocatorTypeID](cfallocatortypeid.md)
- [struct CFCalendarIdentifier](cfcalendaridentifier.md)
- [struct CFDateFormatterKey](cfdateformatterkey.md)
- [typealias CFErrorDomain](cferrordomain.md)
- [struct CFLocaleIdentifier](cflocaleidentifier.md)
- [struct CFNotificationName](cfnotificationname.md)
- [struct CFNumberFormatterKey](cfnumberformatterkey.md)
- [struct CFRunLoopMode](cfrunloopmode.md)
- [struct CFStreamPropertyKey](cfstreampropertykey.md)
- [typealias CFTypeRef](cftyperef.md)
  An untyped “generic” reference to any Core Foundation object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cflocalekey)*