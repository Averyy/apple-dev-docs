# init(string:locale:)

**Framework**: Foundation  
**Kind**: init

Creates and initializes a decimal by parsing a string according to the provided locale’s conventions.

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
init?(string: String, locale: Locale? = nil)
```

## Parameters

- `string`: A string containing a formatted decimal value.
- `locale`: A locale that indicates the formatting conventions used by  .

## See Also

- [init(String, format: Decimal.FormatStyle, lenient: Bool) throws](decimal/init(_:format:lenient:)-6fk71.md)
  Creates and initializes a decimal by parsing a string according to the provided format style.
- [init(String, format: Decimal.FormatStyle.Currency, lenient: Bool) throws](decimal/init(_:format:lenient:)-8t5o2.md)
  Creates and initializes a decimal by parsing a string according to the provided currency format style.
- [init(String, format: Decimal.FormatStyle.Percent, lenient: Bool) throws](decimal/init(_:format:lenient:)-3u6o6.md)
  Creates and initializes a percentage decimal by parsing a string according to the provided format style.
- [init<S>(S.ParseInput, strategy: S) throws](decimal/init(_:strategy:).md)
  Creates and initializes a decimal by parsing an arbitrary type according to the provided parse strategy.
- [Decimal.ParseStrategy](decimal/parsestrategy.md)
  A parse strategy for creating decimal values from formatted strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/decimal/init(string:locale:))*