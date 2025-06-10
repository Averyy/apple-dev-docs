# ParseStrategy

**Framework**: Foundation  
**Kind**: protocol

A type that parses an input representation, such as a formatted string, into a provided data type.

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
protocol ParseStrategy : Decodable, Encodable, Hashable
```

#### Overview

A [`ParseStrategy`](parsestrategy.md) allows you to convert a formatted representation into a data type, using one of two approaches:

- Initialize the data type by calling an initializer of that type that takes a formatted instance and a parse strategy as parameters. For example, you can create a [`Decimal`](decimal.md) from a formatted string with the initializer [`init(_:format:lenient:)`](decimal/init(_:format:lenient:)-6fk71.md).
- Create a parse strategy and call its [`parse(_:)`](parsestrategy/parse(_:).md) method on one or more formatted instances.

[`ParseStrategy`](parsestrategy.md) is closely related to [`FormatStyle`](formatstyle.md), which provides the opposite conversion: from data type to formatted representation. To use a parse strategy, you create a [`FormatStyle`](formatstyle.md) to define the representation you expect, then access the style’s `parseStrategy` property to get a strategy instance.

The following example creates a [`Decimal.FormatStyle.Currency`](decimal/formatstyle/currency.md) format style that uses US dollars and US English number-formatting conventions. It then creates a [`Decimal`](decimal.md) instance by providing a formatted string to parse and the format style’s `Decimal/FormatStyle/Currency/parseStrategy`.

```swift
let style = Decimal.FormatStyle.Currency(code: "USD",
                                         locale: Locale(identifier: "en_US"))
let parsed = try? Decimal("$12,345.67",
                           strategy: style.parseStrategy) // 12345.67
```

## Topics

### Performing parsing
- [func parse(Self.ParseInput) throws -> Self.ParseOutput](parsestrategy/parse(_:).md)
  Parses a value, using this strategy.
### Commonly-used parsers
- [static func fixed(format: Date.FormatString, timeZone: TimeZone, locale: Locale?) -> Self](parsestrategy/fixed(format:timezone:locale:).md)
  A fixed-format date parse strategy.
- [static var url: URL.ParseStrategy](parsestrategy/url.md)
  A parse strategy for URLs.
- [static var name: PersonNameComponents.ParseStrategy](parsestrategy/name.md)
  A parse strategy for person name components.
### Commonly-used format styles
- [static var dateTime: Date.FormatStyle](parsestrategy/datetime.md)
  A default format style for formatting dates.
### Supporting types
- [associatedtype ParseInput](parsestrategy/parseinput.md)
  The input type parsed by this strategy.
- [associatedtype ParseOutput](parsestrategy/parseoutput.md)
  The output type returned by this strategy.
### Type Properties
- [static var http: Date.HTTPFormatStyle](parsestrategy/http-5mpzc.md)
- [static var http: DateComponents.HTTPFormatStyle](parsestrategy/http-6hyig.md)
- [static var iso8601: DateComponents.ISO8601FormatStyle](parsestrategy/iso8601-69scf.md)
- [static var iso8601: Date.ISO8601FormatStyle](parsestrategy/iso8601-8z0au.md)

## Relationships

### Inherits From
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
### Conforming Types
- [Date.FormatStyle](date/formatstyle.md)
- [Date.HTTPFormatStyle](date/httpformatstyle.md)
- [Date.ISO8601FormatStyle](date/iso8601formatstyle.md)
- [Date.ParseStrategy](date/parsestrategy.md)
- [DateComponents.HTTPFormatStyle](datecomponents/httpformatstyle.md)
- [DateComponents.ISO8601FormatStyle](datecomponents/iso8601formatstyle.md)
- [Decimal.ParseStrategy](decimal/parsestrategy.md)
- [FloatingPointParseStrategy](floatingpointparsestrategy.md)
- [IntegerParseStrategy](integerparsestrategy.md)
- [PersonNameComponents.ParseStrategy](personnamecomponents/parsestrategy.md)
- [URL.ParseStrategy](url/parsestrategy.md)

## See Also

- [protocol ParseableFormatStyle](parseableformatstyle.md)
  A type that can convert a given input data type into a representation in an output type.
- [struct IntegerParseStrategy](integerparsestrategy.md)
  A parse strategy for creating integer values from formatted strings.
- [struct FloatingPointParseStrategy](floatingpointparsestrategy.md)
  A parse strategy for creating floating-point values from formatted strings.
- [Decimal.ParseStrategy](decimal/parsestrategy.md)
  A parse strategy for creating decimal values from formatted strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/parsestrategy)*