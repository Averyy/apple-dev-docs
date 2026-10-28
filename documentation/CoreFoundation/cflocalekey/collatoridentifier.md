# collatorIdentifier

**Framework**: Core Foundation  
**Kind**: property  
**Role**: Type Property

Specifies the collation identifier for the locale.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let collatorIdentifier: CFLocaleKey!
```

```c
extern CFLocaleKey const kCFLocaleCollatorIdentifier;
```

## Discussion

The corresponding value is a CFString object. If unknown, `nil` is returned.

## See Also

### Constants
- [static let identifier: CFLocaleKey!](./identifier.md)
  Specifies locale identifier.
- [static let languageCode: CFLocaleKey!](./languagecode.md)
  Specifies the locale language code.
- [static let countryCode: CFLocaleKey!](./countrycode.md)
  Specifies the locale country code.
- [static let scriptCode: CFLocaleKey!](./scriptcode.md)
  Specifies the locale script code.
- [static let variantCode: CFLocaleKey!](./variantcode.md)
  Specifies the locale variant code.
- [static let exemplarCharacterSet: CFLocaleKey!](./exemplarcharacterset.md)
  Specifies the locale character set.
- [static let calendarIdentifier: CFLocaleKey!](./calendaridentifier.md)
  Specifies the locale calendar identifier.
- [static let calendar: CFLocaleKey!](./calendar.md)
  Specifies the locale calendar.
- [static let collationIdentifier: CFLocaleKey!](./collationidentifier.md)
  Specifies the locale collation identifier.
- [static let usesMetricSystem: CFLocaleKey!](./usesmetricsystem.md)
  Specifies the whether the locale uses the metric system.
- [static let measurementSystem: CFLocaleKey!](./measurementsystem.md)
  Specifies the measurement system used.
- [static let decimalSeparator: CFLocaleKey!](./decimalseparator.md)
  Specifies the decimal point string.
- [static let groupingSeparator: CFLocaleKey!](./groupingseparator.md)
  Specifies the separator string between groups of digits.
- [static let currencySymbol: CFLocaleKey!](./currencysymbol.md)
  Specifies the currency symbol.
- [static let currencyCode: CFLocaleKey!](./currencycode.md)
  Specifies the locale currency code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cflocalekey/collatoridentifier)*