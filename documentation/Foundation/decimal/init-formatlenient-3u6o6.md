# init(_:format:lenient:)

**Framework**: Foundation  
**Kind**: init

Creates and initializes a percentage decimal by parsing a string according to the provided format style.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init(_ value: String, format: Decimal.FormatStyle.Percent, lenient: Bool = true) throws
```

#### Discussion

This initializer throws an error if the format style fails to parse the string into a decimal value.

## Parameters

- `value`: A string that contains a formatted decimal value.
- `format`: A format style that describes percent formatting conventions used by the string. The initializer uses this format’s   to parse the string.
- `lenient`: A Boolean value that indicates whether the parse strategy should permit some discrepancies when parsing. Defaults to  .

## See Also

- [init(String, format: Decimal.FormatStyle, lenient: Bool) throws](decimal/init(_:format:lenient:)-6fk71.md)
  Creates and initializes a decimal by parsing a string according to the provided format style.
- [init(String, format: Decimal.FormatStyle.Currency, lenient: Bool) throws](decimal/init(_:format:lenient:)-8t5o2.md)
  Creates and initializes a decimal by parsing a string according to the provided currency format style.
- [init?(string: String, locale: Locale?)](decimal/init(string:locale:).md)
  Creates and initializes a decimal by parsing a string according to the provided locale’s conventions.
- [init<S>(S.ParseInput, strategy: S) throws](decimal/init(_:strategy:).md)
  Creates and initializes a decimal by parsing an arbitrary type according to the provided parse strategy.
- [Decimal.ParseStrategy](decimal/parsestrategy.md)
  A parse strategy for creating decimal values from formatted strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/decimal/init(_:format:lenient:)-3u6o6)*