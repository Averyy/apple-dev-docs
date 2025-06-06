# IntegerFormatStyle.Percent

**Framework**: Foundation  
**Kind**: struct

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

## Topics

### Creating an integer percent format style
- [init(locale: Locale)](integerformatstyle/percent/init(locale:).md)
  Creates an integer percent format style that uses the given locale.
### Customizing style behavior
- [func decimalSeparator(strategy: IntegerFormatStyle<Value>.Percent.Configuration.DecimalSeparatorDisplayStrategy) -> IntegerFormatStyle<Value>.Percent](integerformatstyle/percent/decimalseparator(strategy:).md)
  Modifies the format style to use the specified decimal separator display strategy.
- [func grouping(IntegerFormatStyle<Value>.Percent.Configuration.Grouping) -> IntegerFormatStyle<Value>.Percent](integerformatstyle/percent/grouping(_:).md)
  Modifies the format style to use the specified grouping.
- [func notation(IntegerFormatStyle<Value>.Percent.Configuration.Notation) -> IntegerFormatStyle<Value>.Percent](integerformatstyle/percent/notation(_:).md)
  Modifies the format style to use the specified notation.
- [func precision(IntegerFormatStyle<Value>.Percent.Configuration.Precision) -> IntegerFormatStyle<Value>.Percent](integerformatstyle/percent/precision(_:).md)
  Modifies the format style to use the specified precision.
- [func rounded(rule: IntegerFormatStyle<Value>.Percent.Configuration.RoundingRule, increment: Int?) -> IntegerFormatStyle<Value>.Percent](integerformatstyle/percent/rounded(rule:increment:).md)
  Modifies the format style to use the specified rounding rule and increment.
- [func scale(Double) -> IntegerFormatStyle<Value>.Percent](integerformatstyle/percent/scale(_:).md)
  Modifies the format style to use the specified scale.
- [func sign(strategy: IntegerFormatStyle<Value>.Percent.Configuration.SignDisplayStrategy) -> IntegerFormatStyle<Value>.Percent](integerformatstyle/percent/sign(strategy:).md)
  Modifies the format style to use the specified sign display strategy.
- [IntegerFormatStyle.Percent.Configuration](integerformatstyle/percent/configuration.md)
  The type the format style uses for configuration settings.
- [enum NumberFormatStyleConfiguration](numberformatstyleconfiguration.md)
  Configuration settings for formatting numbers of different types.
### Formatting integer percent values
- [func format(Value) -> String](integerformatstyle/percent/format(_:).md)
  Formats an integer, using this style.
### Creating attributed strings
- [var attributed: IntegerFormatStyle<Value>.Attributed](integerformatstyle/percent/attributed.md)
  An attributed format style based on the integer percent format style.
- [IntegerFormatStyle.Attributed](integerformatstyle/attributed-swift.struct.md)
  A format style that converts integers into attributed strings.
### Accessing style properties
- [var locale: Locale](integerformatstyle/percent/locale.md)
  The locale of the format style.
### Default Implementations
- [FormatStyle Implementations](integerformatstyle/percent/formatstyle-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomConsumingRegexComponent](../Swift/CustomConsumingRegexComponent.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [FormatStyle](formatstyle.md)
- [Hashable](../Swift/Hashable.md)
- [ParseableFormatStyle](parseableformatstyle.md)
- [RegexComponent](../Swift/RegexComponent.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [static var percent: IntegerFormatStyle<Int>.Percent](formatstyle/percent-cl9k.md)
  A style for formatting signed integer types in Swift as a percent representation.
- [static var percent: IntegerFormatStyle<UInt>.Percent](formatstyle/percent-9pj79.md)
  A style for formatting signed integer types in Swift as a percent representation.
- [static var percent: IntegerFormatStyle<Int8>.Percent](formatstyle/percent-7r4rl.md)
  A style for formatting 8-bit signed integers as a percent representation.
- [static var percent: IntegerFormatStyle<Int16>.Percent](formatstyle/percent-3qjzh.md)
  A style for formatting 16-bit signed integers as a percent representation.
- [static var percent: IntegerFormatStyle<Int32>.Percent](formatstyle/percent-1f0q.md)
  A style for formatting 32-bit signed integers as a percent representation.
- [static var percent: IntegerFormatStyle<Int64>.Percent](formatstyle/percent-934se.md)
  A style for formatting 64-bit signed integers as a percent representation.
- [static var percent: IntegerFormatStyle<UInt8>.Percent](formatstyle/percent-8izzv.md)
  A style for formatting 8-bit unsigned integers as a percent representation.
- [static var percent: IntegerFormatStyle<UInt16>.Percent](formatstyle/percent-4kdme.md)
  A style for formatting 16-bit unsigned integers as a percent representation.
- [static var percent: IntegerFormatStyle<UInt32>.Percent](formatstyle/percent-2f11j.md)
  A style for formatting 32-bit unsigned integers as a percent representation.
- [static var percent: IntegerFormatStyle<UInt64>.Percent](formatstyle/percent-8bxla.md)
  A style for formatting 64-bit unsigned integers as a percent representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/integerformatstyle/percent)*