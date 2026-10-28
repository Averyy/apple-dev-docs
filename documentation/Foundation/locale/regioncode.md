# regionCode

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The region code of the locale, or `nil` if it has none.

**Availability**:
- iOS 8.0+ - Deprecated in 16.0 (renamed: region.identifier)
- iPadOS 8.0+ - Deprecated in 16.0 (renamed: region.identifier)
- Mac Catalyst 8.0+ - Deprecated in 16.0 (renamed: region.identifier)
- macOS 10.10+ - Deprecated in 13.0 (renamed: region.identifier)
- tvOS 9.0+ - Deprecated in 16.0 (renamed: region.identifier)
- visionOS 1.0+
- watchOS 2.0+ - Deprecated in 9.0 (renamed: region.identifier)

## Declaration

```swift
var regionCode: String? { get }
```

## Discussion

For example, for the locale “zh-Hant-HK”, returns “HK”.

## See Also

### Getting information about a locale
- [var identifier: String](./identifier.md)
  The identifier of the locale.
- [func identifier(Locale.IdentifierType) -> String](./identifier%28_%29.md)
  Returns the locale identifier, in the specified standard format.
- [Locale.IdentifierType](./identifiertype.md)
  A type that indicates the standard that defines a locale’s identifier.
- [var calendar: Calendar](./calendar.md)
  The calendar for the locale, or the Gregorian calendar as a fallback.
- [var languageCode: String?](./languagecode-swift.property.md)
  The language code of the locale, or `nil` if has none.
- [var scriptCode: String?](./scriptcode.md)
  The script code of the locale, or `nil` if has none.
- [var variantCode: String?](./variantcode.md)
  The variant code for the locale, or `nil` if it has none.
- [var exemplarCharacterSet: CharacterSet?](./exemplarcharacterset.md)
  The exemplar character set for the locale, or `nil` if has none.
- [var collationIdentifier: String?](./collationidentifier.md)
  The collation identifier for the locale, or `nil` if it has none.
- [var collatorIdentifier: String?](./collatoridentifier.md)
  The collator identifier of the locale.
- [var usesMetricSystem: Bool](./usesmetricsystem.md)
  A Boolean that is true if the locale uses the metric system.
- [var decimalSeparator: String?](./decimalseparator.md)
  The decimal separator of the locale.
- [var groupingSeparator: String?](./groupingseparator.md)
  The grouping separator of the locale.
- [var currencyCode: String?](./currencycode.md)
  The currency code of the locale.
- [var currencySymbol: String?](./currencysymbol.md)
  The currency symbol of the locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/regioncode)*