# init(_:strategy:)

**Framework**: Foundation  
**Kind**: init

Creates and initializes a decimal by parsing an arbitrary type according to the provided parse strategy.

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
init<S>(_ value: S.ParseInput, strategy: S) throws where S : ParseStrategy, S.ParseOutput == Decimal
```

## Parameters

- `value`: An instance of  ’s input type.
- `strategy`: A parse strategy that describes how the parser converts the string to a decimal value.

## See Also

- [init(String, format: Decimal.FormatStyle, lenient: Bool) throws](decimal/init(_:format:lenient:)-6fk71.md)
  Creates and initializes a decimal by parsing a string according to the provided format style.
- [init(String, format: Decimal.FormatStyle.Currency, lenient: Bool) throws](decimal/init(_:format:lenient:)-8t5o2.md)
  Creates and initializes a decimal by parsing a string according to the provided currency format style.
- [init(String, format: Decimal.FormatStyle.Percent, lenient: Bool) throws](decimal/init(_:format:lenient:)-3u6o6.md)
  Creates and initializes a percentage decimal by parsing a string according to the provided format style.
- [init?(string: String, locale: Locale?)](decimal/init(string:locale:).md)
  Creates and initializes a decimal by parsing a string according to the provided locale’s conventions.
- [Decimal.ParseStrategy](decimal/parsestrategy.md)
  A parse strategy for creating decimal values from formatted strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/decimal/init(_:strategy:))*