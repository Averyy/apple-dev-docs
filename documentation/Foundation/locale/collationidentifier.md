# collationIdentifier

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The collation identifier for the locale, or `nil` if it has none.

**Availability**:
- iOS 8.0+ - Deprecated in 16.0 (renamed: collation.identifier)
- iPadOS 8.0+ - Deprecated in 16.0 (renamed: collation.identifier)
- Mac Catalyst 8.0+ - Deprecated in 16.0 (renamed: collation.identifier)
- macOS 10.10+ - Deprecated in 13.0 (renamed: collation.identifier)
- tvOS 9.0+ - Deprecated in 16.0 (renamed: collation.identifier)
- visionOS 1.0+
- watchOS 2.0+ - Deprecated in 9.0 (renamed: collation.identifier)

## Declaration

```swift
var collationIdentifier: String? { get }
```

## Discussion

For example, for the locale “en_US@collation=phonebook”, returns “phonebook”.

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
- [var regionCode: String?](./regioncode.md)
  The region code of the locale, or `nil` if it has none.
- [var languageCode: String?](./languagecode-swift.property.md)
  The language code of the locale, or `nil` if has none.
- [var scriptCode: String?](./scriptcode.md)
  The script code of the locale, or `nil` if has none.
- [var variantCode: String?](./variantcode.md)
  The variant code for the locale, or `nil` if it has none.
- [var exemplarCharacterSet: CharacterSet?](./exemplarcharacterset.md)
  The exemplar character set for the locale, or `nil` if has none.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/collationidentifier)*