# IntegerParseStrategy

**Framework**: Foundation  
**Kind**: struct

A parse strategy for creating integer values from formatted strings.

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
struct IntegerParseStrategy<Format> where Format : FormatStyle, Format.FormatInput : BinaryInteger
```

#### Overview

Create an explicit [`IntegerParseStrategy`](integerparsestrategy.md) to parse multiple strings according to the same parse strategy. In the following example, `usCurrencyStrategy` is an [`IntegerParseStrategy`](integerparsestrategy.md) that uses US dollars and the `en_US` locale’s conventions for number formatting. The example then uses this strategy to parse an array of strings, some of which represent valid US currency values.

```swift
let usCurrencyStrategy: IntegerParseStrategy =
    IntegerFormatStyle<Int>.Currency(code: "USD",
                                     locale: Locale(identifier: "en_US"))
    .parseStrategy
let currencyValues = ["$100", "$1,000", "$10,000", "€100"]
let parsedValues = currencyValues.map { try? usCurrencyStrategy.parse($0) } // [Optional(100), Optional(1000), Optional(10000), nil]
```

You don’t need to instantiate a parse strategy variable to parse a single string. Instead, use the [`BinaryInteger`](https://developer.apple.com/documentation/Swift/BinaryInteger) initializers that take a source [`String`](https://developer.apple.com/documentation/Swift/String) and a `format` parameter to parse the string according to the provided [`FormatStyle`](formatstyle.md). The following example parses a string that represents a currency value in US dollars.

```swift
let formattedUSDollars = "$1,234"
let parsedUSDollars = try? Int(formattedUSDollars, format: .currency(code: "USD")
    .locale(Locale(identifier: "en_US"))) // 1234
```

## Topics

### Creating an integer parse strategy
- [init<Value>(format: Format, lenient: Bool)](integerparsestrategy/init(format:lenient:)-124xn.md)
  Creates a parse strategy instance using the specified integer format style.
- [init<Value>(format: Format, lenient: Bool)](integerparsestrategy/init(format:lenient:)-7tox3.md)
  Creates a parse strategy instance using the specified integer currency format style.
- [init<Value>(format: Format, lenient: Bool)](integerparsestrategy/init(format:lenient:)-3gbvo.md)
  Creates a parse strategy instance using the specified integer percentage format style.
### Accessing strategy properties
- [var formatStyle: Format](integerparsestrategy/formatstyle.md)
  The format style this strategy uses when parsing strings.
- [var lenient: Bool](integerparsestrategy/lenient.md)
  A Boolean value that indicates whether parsing allows any discrepencies in the expected format.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [ParseStrategy](parsestrategy.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol ParseableFormatStyle](parseableformatstyle.md)
  A type that can convert a given input data type into a representation in an output type.
- [protocol ParseStrategy](parsestrategy.md)
  A type that parses an input representation, such as a formatted string, into a provided data type.
- [struct FloatingPointParseStrategy](floatingpointparsestrategy.md)
  A parse strategy for creating floating-point values from formatted strings.
- [Decimal.ParseStrategy](decimal/parsestrategy.md)
  A parse strategy for creating decimal values from formatted strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/integerparsestrategy)*