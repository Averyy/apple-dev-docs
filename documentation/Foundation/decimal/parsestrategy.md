# Decimal.ParseStrategy

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A parse strategy for creating decimal values from formatted strings.

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
struct ParseStrategy<Format> where Format : FormatStyle, Format.FormatInput == Decimal
```

## Overview

Create an explicit [`Decimal.ParseStrategy`](./parsestrategy.md) to parse mulitple strings according to the same parse strategy. In the following example, `usCurrencyStrategy` is a [`Decimal.ParseStrategy`](./parsestrategy.md) that uses US dollars and the `en_US` locale’s conventions for number formatting. The example then uses this strategy to parse an array of strings, some of which represent valid US currency values.

```swift
let usCurrencyStrategy: Decimal.ParseStrategy =
Decimal.FormatStyle.Currency(code: "USD",
                             locale: Locale(identifier: "en_US"))
.parseStrategy
let currencyValues = ["$100.11", "$1,000.22", "$10,000.33", "€100.44"]
let parsedValues = currencyValues.map { try? usCurrencyStrategy.parse($0) } // [Optional(100.11), Optional(1000.22), Optional(10000.33), nil]
```

You don’t need to instantiate a parse strategy variable to parse a single string. Instead, use the [`init(_:format:lenient:)`](./init%28_,format,lenient%29-3u6o6.md) initializer, which takes a source [`String`](../../Swift/string.md) and a `format` parameter to parse the string according to the provided [`Decimal.FormatStyle`](./formatstyle.md). The following example parses a string that represents a currency value in US dollars.

```swift
let formattedUSDollars = "$1,234.56"
let parsedUSDollars = try? Decimal(formattedUSDollars, format: .currency(code: "USD")
    .locale(Locale(identifier: "en_US"))) // 1234.56
```

Decimal also has an [`init(_:strategy:)`](./init%28_,strategy%29.md) initializer, if it’s more convenient to pass a [`Decimal.ParseStrategy`](./parsestrategy.md) instance rather than implicitly derive a strategy from a [`Decimal.FormatStyle`](./formatstyle.md).

## Topics

### Creating a decimal parse strategy
- [init(format: Format, lenient: Bool)](./parsestrategy/init%28format,lenient%29-46ix2.md)
  Creates a parse strategy instance using the specified decimal format style.
- [init(format: Format, lenient: Bool)](./parsestrategy/init%28format,lenient%29-22h06.md)
  Creates a parse strategy instance using the specified decimal currency format style.
- [init(format: Format, lenient: Bool)](./parsestrategy/init%28format,lenient%29-36ja3.md)
  Creates a parse strategy instance using the specified decimal percentage format style.
### Parsing strings
- [func parse(String) throws -> Format.FormatInput](./parsestrategy/parse%28_%29.md)
  Parses a decimal string in accordance with this strategy and returns the parsed value.
### Accessing strategy properties
- [var formatStyle: Format](./parsestrategy/formatstyle.md)
  The format style this strategy uses when parsing strings.
- [var lenient: Bool](./parsestrategy/lenient.md)
  A Boolean value that indicates whether parsing allows any discrepencies in the expected format.
### Default Implementations
- [ParseStrategy Implementations](./parsestrategy/parsestrategy-implementations.md)

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [ParseStrategy](../parsestrategy.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Data parsing in Swift
- [protocol ParseableFormatStyle](../parseableformatstyle.md)
  A type that can convert a given input data type into a representation in an output type.
- [protocol ParseStrategy](../parsestrategy.md)
  A type that parses an input representation, such as a formatted string, into a provided data type.
- [struct IntegerParseStrategy](../integerparsestrategy.md)
  A parse strategy for creating integer values from formatted strings.
- [struct FloatingPointParseStrategy](../floatingpointparsestrategy.md)
  A parse strategy for creating floating-point values from formatted strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/decimal/parsestrategy)*