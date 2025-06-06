# quotationEndDelimiter

**Framework**: Foundation  
**Kind**: property

The quotation end delimiter of the locale.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var quotationEndDelimiter: String? { get }
```

#### Discussion

For example, returns `”` for “en_US”, and `」` for “zh-Hant-HK”.

## See Also

- [var identifier: String](locale/identifier.md)
  The identifier of the locale.
- [func identifier(Locale.IdentifierType) -> String](locale/identifier(_:).md)
  Returns the locale identifier, in the specified standard format.
- [Locale.IdentifierType](locale/identifiertype.md)
  A type that indicates the standard that defines a locale’s identifier.
- [var calendar: Calendar](locale/calendar.md)
  The calendar for the locale, or the Gregorian calendar as a fallback.
- [var regionCode: String?](locale/regioncode.md)
  The region code of the locale, or `nil` if it has none.
- [var languageCode: String?](locale/languagecode-swift.property.md)
  The language code of the locale, or `nil` if has none.
- [var scriptCode: String?](locale/scriptcode.md)
  The script code of the locale, or `nil` if has none.
- [var variantCode: String?](locale/variantcode.md)
  The variant code for the locale, or `nil` if it has none.
- [var exemplarCharacterSet: CharacterSet?](locale/exemplarcharacterset.md)
  The exemplar character set for the locale, or `nil` if has none.
- [var collationIdentifier: String?](locale/collationidentifier.md)
  The collation identifier for the locale, or `nil` if it has none.
- [var collatorIdentifier: String?](locale/collatoridentifier.md)
  The collator identifier of the locale.
- [var usesMetricSystem: Bool](locale/usesmetricsystem.md)
  A Boolean that is true if the locale uses the metric system.
- [var decimalSeparator: String?](locale/decimalseparator.md)
  The decimal separator of the locale.
- [var groupingSeparator: String?](locale/groupingseparator.md)
  The grouping separator of the locale.
- [var currencyCode: String?](locale/currencycode.md)
  The currency code of the locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/quotationenddelimiter)*