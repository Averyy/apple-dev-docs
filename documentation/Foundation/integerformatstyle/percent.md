# IntegerFormatStyle.Percent

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A format style that converts between integer percentage values and their textual representations.

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

Available when `Value` conforms to `BinaryInteger`.

## Topics

### Creating an integer percent format style
- [init(locale: Locale)](./percent/init%28locale%29.md)
  Creates an integer percent format style that uses the given locale.
### Customizing style behavior
- [func decimalSeparator(strategy: IntegerFormatStyle<Value>.Percent.Configuration.DecimalSeparatorDisplayStrategy) -> IntegerFormatStyle<Value>.Percent](./percent/decimalseparator%28strategy%29.md)
  Modifies the format style to use the specified decimal separator display strategy.
- [func grouping(IntegerFormatStyle<Value>.Percent.Configuration.Grouping) -> IntegerFormatStyle<Value>.Percent](./percent/grouping%28_%29.md)
  Modifies the format style to use the specified grouping.
- [func locale(Locale) -> IntegerFormatStyle<Value>.Percent](./percent/locale%28_%29.md)
  Modifies the format style to use the specified locale.
- [func notation(IntegerFormatStyle<Value>.Percent.Configuration.Notation) -> IntegerFormatStyle<Value>.Percent](./percent/notation%28_%29.md)
  Modifies the format style to use the specified notation.
- [func precision(IntegerFormatStyle<Value>.Percent.Configuration.Precision) -> IntegerFormatStyle<Value>.Percent](./percent/precision%28_%29.md)
  Modifies the format style to use the specified precision.
- [func rounded(rule: IntegerFormatStyle<Value>.Percent.Configuration.RoundingRule, increment: Int?) -> IntegerFormatStyle<Value>.Percent](./percent/rounded%28rule,increment%29.md)
  Modifies the format style to use the specified rounding rule and increment.
- [func scale(Double) -> IntegerFormatStyle<Value>.Percent](./percent/scale%28_%29.md)
  Modifies the format style to use the specified scale.
- [func sign(strategy: IntegerFormatStyle<Value>.Percent.Configuration.SignDisplayStrategy) -> IntegerFormatStyle<Value>.Percent](./percent/sign%28strategy%29.md)
  Modifies the format style to use the specified sign display strategy.
- [IntegerFormatStyle.Percent.Configuration](./percent/configuration.md)
  The type the format style uses for configuration settings.
- [enum NumberFormatStyleConfiguration](../numberformatstyleconfiguration.md)
  Configuration settings for formatting numbers of different types.
### Formatting integer percent values
- [func format(Value) -> String](./percent/format%28_%29.md)
  Formats an integer, using this style.
### Creating attributed strings
- [var attributed: IntegerFormatStyle<Value>.Attributed](./percent/attributed.md)
  An attributed format style based on the integer percent format style.
- [IntegerFormatStyle.Attributed](./attributed-swift.struct.md)
  A format style that converts integers into attributed strings.
### Accessing style properties
- [var locale: Locale](./percent/locale.md)
  The locale of the format style.
### Parsing integer percent values
- [var parseStrategy: IntegerParseStrategy<IntegerFormatStyle<Value>.Percent>](./percent/parsestrategy.md)
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

### Applying percentage styles for integers
- [static var percent: IntegerFormatStyle<Int>.Percent](../formatstyle/percent-cl9k.md)
  A style for formatting signed integer types in Swift as a percent representation.
- [static var percent: IntegerFormatStyle<UInt>.Percent](../formatstyle/percent-9pj79.md)
  A style for formatting signed integer types in Swift as a percent representation.
- [static var percent: IntegerFormatStyle<Int8>.Percent](../formatstyle/percent-7r4rl.md)
  A style for formatting 8-bit signed integers as a percent representation.
- [static var percent: IntegerFormatStyle<Int16>.Percent](../formatstyle/percent-3qjzh.md)
  A style for formatting 16-bit signed integers as a percent representation.
- [static var percent: IntegerFormatStyle<Int32>.Percent](../formatstyle/percent-1f0q.md)
  A style for formatting 32-bit signed integers as a percent representation.
- [static var percent: IntegerFormatStyle<Int64>.Percent](../formatstyle/percent-934se.md)
  A style for formatting 64-bit signed integers as a percent representation.
- [static var percent: IntegerFormatStyle<UInt8>.Percent](../formatstyle/percent-8izzv.md)
  A style for formatting 8-bit unsigned integers as a percent representation.
- [static var percent: IntegerFormatStyle<UInt16>.Percent](../formatstyle/percent-4kdme.md)
  A style for formatting 16-bit unsigned integers as a percent representation.
- [static var percent: IntegerFormatStyle<UInt32>.Percent](../formatstyle/percent-2f11j.md)
  A style for formatting 32-bit unsigned integers as a percent representation.
- [static var percent: IntegerFormatStyle<UInt64>.Percent](../formatstyle/percent-8bxla.md)
  A style for formatting 64-bit unsigned integers as a percent representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/integerformatstyle/percent)*