# FloatingPointFormatStyle.Currency

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A format style that converts between floating-point currency values and their textual representations.

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
struct Currency
```

Available when `Value` conforms to `BinaryFloatingPoint`.

## Topics

### Creating a floating-point currency style
- [init(code: String, locale: Locale)](./currency/init%28code,locale%29.md)
  Creates a floating-point currency format style that uses the given currency code and locale.
### Customizing style behavior
- [func decimalSeparator(strategy: FloatingPointFormatStyle<Value>.Currency.Configuration.DecimalSeparatorDisplayStrategy) -> FloatingPointFormatStyle<Value>.Currency](./currency/decimalseparator%28strategy%29.md)
  Modifies the format style to use the specified decimal separator display strategy.
- [func grouping(FloatingPointFormatStyle<Value>.Currency.Configuration.Grouping) -> FloatingPointFormatStyle<Value>.Currency](./currency/grouping%28_%29.md)
  Modifies the format style to use the specified grouping.
- [func locale(Locale) -> FloatingPointFormatStyle<Value>.Currency](./currency/locale%28_%29.md)
  Modifies the format style to use the specified locale.
- [func precision(FloatingPointFormatStyle<Value>.Currency.Configuration.Precision) -> FloatingPointFormatStyle<Value>.Currency](./currency/precision%28_%29.md)
  Modifies the format style to use the specified precision.
- [func presentation(FloatingPointFormatStyle<Value>.Currency.Configuration.Presentation) -> FloatingPointFormatStyle<Value>.Currency](./currency/presentation%28_%29.md)
  Modifies the format style to use the specified presentation.
- [func rounded(rule: FloatingPointFormatStyle<Value>.Currency.Configuration.RoundingRule, increment: Double?) -> FloatingPointFormatStyle<Value>.Currency](./currency/rounded%28rule,increment%29.md)
  Modifies the format style to use the specified rounding rule and increment.
- [func scale(Double) -> FloatingPointFormatStyle<Value>.Currency](./currency/scale%28_%29.md)
  Modifies the format style to use the specified scale.
- [func sign(strategy: FloatingPointFormatStyle<Value>.Currency.Configuration.SignDisplayStrategy) -> FloatingPointFormatStyle<Value>.Currency](./currency/sign%28strategy%29.md)
  Modifies the format style to use the specified sign display strategy.
- [FloatingPointFormatStyle.Currency.Configuration](./currency/configuration.md)
  The type the format style uses for configuration settings.
- [enum CurrencyFormatStyleConfiguration](../currencyformatstyleconfiguration.md)
  Configuration settings for formatting currency values.
### Formatting floating-point currency values
- [func format(Value) -> String](./currency/format%28_%29.md)
  Formats a floating-point value, using this style.
### Creating attributed strings
- [var attributed: FloatingPointFormatStyle<Value>.Attributed](./currency/attributed.md)
  An attributed format style based on the floating-point currency format style.
- [FloatingPointFormatStyle.Attributed](./attributed-swift.struct.md)
  A format style that converts integers into attributed strings.
### Accessing style properties
- [let currencyCode: String](./currency/currencycode.md)
  The currency code this format style uses.
- [var locale: Locale](./currency/locale.md)
  The locale of the format style.
### Applying measurement styles
- [Measurement.FormatStyle](../measurement/formatstyle.md)
  A type that provides localized representations of measurements.
### Applying list styles
- [struct ListFormatStyle](../listformatstyle.md)
  A type that formats lists of items with a separator and conjunction appropriate for a given locale.
### Parsing floating-point currency values
- [var parseStrategy: FloatingPointParseStrategy<FloatingPointFormatStyle<Value>.Currency>](./currency/parsestrategy.md)
  The parse strategy that this format style uses.
### Locating currency values in regular expressions
- [func consuming(String, startingAt: String.Index, in: Range<String.Index>) throws -> (upperBound: String.Index, output: Value)?](./currency/consuming%28_,startingat,in%29.md)
  Process the input string within the specified bounds, beginning at the given index, and return the end position (upper bound) of the match and the produced output.
### Instance Methods
- [func notation(FloatingPointFormatStyle<Value>.Currency.Configuration.Notation) -> FloatingPointFormatStyle<Value>.Currency](./currency/notation%28_%29.md)
  Modifies the format style to use the specified notation.
### Default Implementations
- [CustomConsumingRegexComponent Implementations](./currency/customconsumingregexcomponent-implementations.md)
- [FormatStyle Implementations](./currency/formatstyle-implementations.md)
- [ParseableFormatStyle Implementations](./currency/parseableformatstyle-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomConsumingRegexComponent](../../Swift/customconsumingregexcomponent.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [FormatStyle](../formatstyle.md)
- [Hashable](../../Swift/hashable.md)
- [ParseableFormatStyle](../parseableformatstyle.md)
- [RegexComponent](../../Swift/regexcomponent.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/floatingpointformatstyle/currency)*