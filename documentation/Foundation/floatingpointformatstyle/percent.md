# FloatingPointFormatStyle.Percent

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A format style that converts between floating-point percentage values and their textual representations.

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
struct Percent
```

Available when `Value` conforms to `BinaryFloatingPoint`.

## Topics

### Creating a floating-point percent format style
- [init(locale: Locale)](./percent/init%28locale%29.md)
  Creates a floating-point percent format style that uses the given locale.
### Customizing style behavior
- [func decimalSeparator(strategy: FloatingPointFormatStyle<Value>.Percent.Configuration.DecimalSeparatorDisplayStrategy) -> FloatingPointFormatStyle<Value>.Percent](./percent/decimalseparator%28strategy%29.md)
  Modifies the format style to use the specified decimal separator display strategy.
- [func grouping(FloatingPointFormatStyle<Value>.Percent.Configuration.Grouping) -> FloatingPointFormatStyle<Value>.Percent](./percent/grouping%28_%29.md)
  Modifies the format style to use the specified grouping.
- [func locale(Locale) -> FloatingPointFormatStyle<Value>.Percent](./percent/locale%28_%29.md)
  Modifies the format style to use the specified locale.
- [func notation(FloatingPointFormatStyle<Value>.Percent.Configuration.Notation) -> FloatingPointFormatStyle<Value>.Percent](./percent/notation%28_%29.md)
  Modifies the format style to use the specified notation.
- [func precision(FloatingPointFormatStyle<Value>.Percent.Configuration.Precision) -> FloatingPointFormatStyle<Value>.Percent](./percent/precision%28_%29.md)
  Modifies the format style to use the specified precision.
- [func rounded(rule: FloatingPointFormatStyle<Value>.Percent.Configuration.RoundingRule, increment: Double?) -> FloatingPointFormatStyle<Value>.Percent](./percent/rounded%28rule,increment%29.md)
  Modifies the format style to use the specified rounding rule and increment.
- [func scale(Double) -> FloatingPointFormatStyle<Value>.Percent](./percent/scale%28_%29.md)
  Modifies the format style to use the specified scale.
- [func sign(strategy: FloatingPointFormatStyle<Value>.Percent.Configuration.SignDisplayStrategy) -> FloatingPointFormatStyle<Value>.Percent](./percent/sign%28strategy%29.md)
  Modifies the format style to use the specified sign display strategy.
- [FloatingPointFormatStyle.Percent.Configuration](./percent/configuration.md)
  The type the format style uses for configuration settings.
- [enum NumberFormatStyleConfiguration](../numberformatstyleconfiguration.md)
  Configuration settings for formatting numbers of different types.
### Formatting floating-point percent values
- [func format(Value) -> String](./percent/format%28_%29.md)
  Formats an floating-point value, using this style.
### Creating attributed strings
- [var attributed: FloatingPointFormatStyle<Value>.Attributed](./percent/attributed.md)
  An attributed format style based on the floating-point percent format style.
- [FloatingPointFormatStyle.Attributed](./attributed-swift.struct.md)
  A format style that converts integers into attributed strings.
### Accessing style properties
- [var locale: Locale](./percent/locale.md)
  The locale of the format style.
### Parsing floating-point percent values
- [var parseStrategy: FloatingPointParseStrategy<FloatingPointFormatStyle<Value>.Percent>](./percent/parsestrategy.md)
  The parse strategy that this format style uses.
### Locating percent values in regular expressions
- [func consuming(String, startingAt: String.Index, in: Range<String.Index>) throws -> (upperBound: String.Index, output: Value)?](./percent/consuming%28_,startingat,in%29.md)
  Process the input string within the specified bounds, beginning at the given index, and return the end position (upper bound) of the match and the produced output.
### Default Implementations
- [CustomConsumingRegexComponent Implementations](./percent/customconsumingregexcomponent-implementations.md)
- [FormatStyle Implementations](./percent/formatstyle-implementations.md)
- [ParseableFormatStyle Implementations](./percent/parseableformatstyle-implementations.md)

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

## See Also

### Supporting types
- [FloatingPointFormatStyle.Currency](./currency.md)
  A format style that converts between floating-point currency values and their textual representations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/floatingpointformatstyle/percent)*