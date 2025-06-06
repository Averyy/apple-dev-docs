# FloatingPointFormatStyle.Percent

**Framework**: Foundation  
**Kind**: struct

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

## Topics

### Creating a floating-point percent format style
- [init(locale: Locale)](floatingpointformatstyle/percent/init(locale:).md)
  Creates a floating-point percent format style that uses the given locale.
### Customizing style behavior
- [func decimalSeparator(strategy: FloatingPointFormatStyle<Value>.Percent.Configuration.DecimalSeparatorDisplayStrategy) -> FloatingPointFormatStyle<Value>.Percent](floatingpointformatstyle/percent/decimalseparator(strategy:).md)
  Modifies the format style to use the specified decimal separator display strategy.
- [func grouping(FloatingPointFormatStyle<Value>.Percent.Configuration.Grouping) -> FloatingPointFormatStyle<Value>.Percent](floatingpointformatstyle/percent/grouping(_:).md)
  Modifies the format style to use the specified grouping.
- [func notation(FloatingPointFormatStyle<Value>.Percent.Configuration.Notation) -> FloatingPointFormatStyle<Value>.Percent](floatingpointformatstyle/percent/notation(_:).md)
  Modifies the format style to use the specified notation.
- [func precision(FloatingPointFormatStyle<Value>.Percent.Configuration.Precision) -> FloatingPointFormatStyle<Value>.Percent](floatingpointformatstyle/percent/precision(_:).md)
  Modifies the format style to use the specified precision.
- [func rounded(rule: FloatingPointFormatStyle<Value>.Percent.Configuration.RoundingRule, increment: Double?) -> FloatingPointFormatStyle<Value>.Percent](floatingpointformatstyle/percent/rounded(rule:increment:).md)
  Modifies the format style to use the specified rounding rule and increment.
- [func scale(Double) -> FloatingPointFormatStyle<Value>.Percent](floatingpointformatstyle/percent/scale(_:).md)
  Modifies the format style to use the specified scale.
- [func sign(strategy: FloatingPointFormatStyle<Value>.Percent.Configuration.SignDisplayStrategy) -> FloatingPointFormatStyle<Value>.Percent](floatingpointformatstyle/percent/sign(strategy:).md)
  Modifies the format style to use the specified sign display strategy.
- [FloatingPointFormatStyle.Percent.Configuration](floatingpointformatstyle/percent/configuration.md)
  The type the format style uses for configuration settings.
- [enum NumberFormatStyleConfiguration](numberformatstyleconfiguration.md)
  Configuration settings for formatting numbers of different types.
### Creating attributed strings
- [var attributed: FloatingPointFormatStyle<Value>.Attributed](floatingpointformatstyle/percent/attributed.md)
  An attributed format style based on the floating-point percent format style.
- [FloatingPointFormatStyle.Attributed](floatingpointformatstyle/attributed-swift.struct.md)
  A format style that converts integers into attributed strings.
### Accessing style properties
- [var locale: Locale](floatingpointformatstyle/percent/locale.md)
  The locale of the format style.

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

- [FloatingPointFormatStyle.Currency](floatingpointformatstyle/currency.md)
  A format style that converts between floating-point currency values and their textual representations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/floatingpointformatstyle/percent)*