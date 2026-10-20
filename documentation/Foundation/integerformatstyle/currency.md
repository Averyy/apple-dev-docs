# IntegerFormatStyle.Currency

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A format style that converts between integer currency values and their textual representations.

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

Available when `Value` conforms to `BinaryInteger`.

## Topics

### Creating an integer currency format style
- [init(code: String, locale: Locale)](./currency/init%28code,locale%29.md)
  Creates an integer currency format style that uses the given currency code and locale.
### Customizing style behavior
- [func decimalSeparator(strategy: IntegerFormatStyle<Value>.Currency.Configuration.DecimalSeparatorDisplayStrategy) -> IntegerFormatStyle<Value>.Currency](./currency/decimalseparator%28strategy%29.md)
  Modifies the format style to use the specified decimal separator display strategy.
- [func grouping(IntegerFormatStyle<Value>.Currency.Configuration.Grouping) -> IntegerFormatStyle<Value>.Currency](./currency/grouping%28_%29.md)
  Modifies the format style to use the specified grouping.
- [func locale(Locale) -> IntegerFormatStyle<Value>.Currency](./currency/locale%28_%29.md)
  Modifies the format style to use the specified locale.
- [func precision(IntegerFormatStyle<Value>.Currency.Configuration.Precision) -> IntegerFormatStyle<Value>.Currency](./currency/precision%28_%29.md)
  Modifies the format style to use the specified precision.
- [func presentation(IntegerFormatStyle<Value>.Currency.Configuration.Presentation) -> IntegerFormatStyle<Value>.Currency](./currency/presentation%28_%29.md)
  Modifies the format style to use the specified presentation.
- [func rounded(rule: IntegerFormatStyle<Value>.Currency.Configuration.RoundingRule, increment: Int?) -> IntegerFormatStyle<Value>.Currency](./currency/rounded%28rule,increment%29.md)
  Modifies the format style to use the specified rounding rule and increment.
- [func scale(Double) -> IntegerFormatStyle<Value>.Currency](./currency/scale%28_%29.md)
  Modifies the format style to use the specified scale.
- [func sign(strategy: IntegerFormatStyle<Value>.Currency.Configuration.SignDisplayStrategy) -> IntegerFormatStyle<Value>.Currency](./currency/sign%28strategy%29.md)
  Modifies the format style to use the specified sign display strategy.
- [IntegerFormatStyle.Currency.Configuration](./currency/configuration.md)
  The type the format style uses for configuration settings.
- [enum CurrencyFormatStyleConfiguration](../currencyformatstyleconfiguration.md)
  Configuration settings for formatting currency values.
### Formatting integer currency values
- [func format(Value) -> String](./currency/format%28_%29.md)
  Formats an integer, using this style.
### Creating attributed strings
- [var attributed: IntegerFormatStyle<Value>.Attributed](./currency/attributed.md)
  An attributed format style based on the integer currency format style.
- [IntegerFormatStyle.Attributed](./attributed-swift.struct.md)
  A format style that converts integers into attributed strings.
### Accessing style properties
- [let currencyCode: String](./currency/currencycode.md)
  The currency code this format style uses.
- [var locale: Locale](./currency/locale.md)
  The locale of the format style.
### Applying measurement styles
- [Measurement.FormatStyle](../measurement/formatstyle.md)
  A type that provides localized representations of measurements.
### Parsing integer currency values
- [var parseStrategy: IntegerParseStrategy<IntegerFormatStyle<Value>.Currency>](./currency/parsestrategy.md)
  The parse strategy that this format style uses.
### Locating currency values in regular expressions
- [func consuming(String, startingAt: String.Index, in: Range<String.Index>) throws -> (upperBound: String.Index, output: Value)?](./currency/consuming%28_,startingat,in%29.md)
  Process the input string within the specified bounds, beginning at the given index, and return the end position (upper bound) of the match and the produced output.
### Instance Methods
- [func notation(IntegerFormatStyle<Value>.Currency.Configuration.Notation) -> IntegerFormatStyle<Value>.Currency](./currency/notation%28_%29.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/integerformatstyle/currency)*