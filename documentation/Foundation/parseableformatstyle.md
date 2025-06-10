# ParseableFormatStyle

**Framework**: Foundation  
**Kind**: protocol

A type that can convert a given input data type into a representation in an output type.

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
protocol ParseableFormatStyle : FormatStyle
```

## Topics

### Declaring Parse Strategy
- [var parseStrategy: Self.Strategy](parseableformatstyle/parsestrategy.md)
- [associatedtype Strategy : ParseStrategy](parseableformatstyle/strategy.md)
### Type Properties
- [static var dateTime: Date.FormatStyle](parseableformatstyle/datetime.md)
- [static var http: Date.HTTPFormatStyle](parseableformatstyle/http-6qda5.md)
- [static var http: DateComponents.HTTPFormatStyle](parseableformatstyle/http-yfpc.md)
- [static var iso8601: Date.ISO8601FormatStyle](parseableformatstyle/iso8601-41vzo.md)
- [static var iso8601: DateComponents.ISO8601FormatStyle](parseableformatstyle/iso8601-55wjm.md)
- [static var number: Decimal.FormatStyle](parseableformatstyle/number.md)
- [static var percent: Decimal.FormatStyle.Percent](parseableformatstyle/percent.md)
- [static var url: URL.FormatStyle](parseableformatstyle/url.md)
### Type Methods
- [static func currency(code: String) -> Self](parseableformatstyle/currency(code:).md)
- [static func name(style: PersonNameComponents.FormatStyle.Style) -> Self](parseableformatstyle/name(style:).md)

## Relationships

### Inherits From
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [FormatStyle](formatstyle.md)
- [Hashable](../Swift/Hashable.md)
### Conforming Types
- [Date.FormatStyle](date/formatstyle.md)
- [Date.HTTPFormatStyle](date/httpformatstyle.md)
- [Date.ISO8601FormatStyle](date/iso8601formatstyle.md)
- [Date.VerbatimFormatStyle](date/verbatimformatstyle.md)
- [DateComponents.HTTPFormatStyle](datecomponents/httpformatstyle.md)
- [DateComponents.ISO8601FormatStyle](datecomponents/iso8601formatstyle.md)
- [Decimal.FormatStyle](decimal/formatstyle.md)
- [Decimal.FormatStyle.Currency](decimal/formatstyle/currency.md)
- [Decimal.FormatStyle.Percent](decimal/formatstyle/percent.md)
- [FloatingPointFormatStyle](floatingpointformatstyle.md)
- [FloatingPointFormatStyle.Currency](floatingpointformatstyle/currency.md)
- [FloatingPointFormatStyle.Percent](floatingpointformatstyle/percent.md)
- [IntegerFormatStyle](integerformatstyle.md)
- [IntegerFormatStyle.Currency](integerformatstyle/currency.md)
- [IntegerFormatStyle.Percent](integerformatstyle/percent.md)
- [PersonNameComponents.FormatStyle](personnamecomponents/formatstyle.md)
- [URL.FormatStyle](url/formatstyle.md)

## See Also

- [protocol ParseStrategy](parsestrategy.md)
  A type that parses an input representation, such as a formatted string, into a provided data type.
- [struct IntegerParseStrategy](integerparsestrategy.md)
  A parse strategy for creating integer values from formatted strings.
- [struct FloatingPointParseStrategy](floatingpointparsestrategy.md)
  A parse strategy for creating floating-point values from formatted strings.
- [Decimal.ParseStrategy](decimal/parsestrategy.md)
  A parse strategy for creating decimal values from formatted strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/parseableformatstyle)*