# FloatingPointFormatStyle.Configuration

**Framework**: Foundation  
**Kind**: typealias

The type the format style uses for configuration settings.

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
typealias Configuration = NumberFormatStyleConfiguration
```

#### Discussion

[`FloatingPointFormatStyle`](floatingpointformatstyle.md) uses [`NumberFormatStyleConfiguration`](numberformatstyleconfiguration.md) for its configuration type.

## See Also

- [func decimalSeparator(strategy: FloatingPointFormatStyle<Value>.Configuration.DecimalSeparatorDisplayStrategy) -> FloatingPointFormatStyle<Value>](floatingpointformatstyle/decimalseparator(strategy:).md)
  Modifies the format style to use the specified decimal separator display strategy.
- [func grouping(FloatingPointFormatStyle<Value>.Configuration.Grouping) -> FloatingPointFormatStyle<Value>](floatingpointformatstyle/grouping(_:).md)
  Modifies the format style to use the specified grouping.
- [func notation(FloatingPointFormatStyle<Value>.Configuration.Notation) -> FloatingPointFormatStyle<Value>](floatingpointformatstyle/notation(_:).md)
  Modifies the format style to use the specified notation.
- [func precision(FloatingPointFormatStyle<Value>.Configuration.Precision) -> FloatingPointFormatStyle<Value>](floatingpointformatstyle/precision(_:).md)
  Modifies the format style to use the specified precision.
- [func rounded(rule: FloatingPointFormatStyle<Value>.Configuration.RoundingRule, increment: Double?) -> FloatingPointFormatStyle<Value>](floatingpointformatstyle/rounded(rule:increment:).md)
  Modifies the format style to use the specified rounding rule and increment.
- [func scale(Double) -> FloatingPointFormatStyle<Value>](floatingpointformatstyle/scale(_:).md)
  Modifies the format style to use the specified scale.
- [func sign(strategy: FloatingPointFormatStyle<Value>.Configuration.SignDisplayStrategy) -> FloatingPointFormatStyle<Value>](floatingpointformatstyle/sign(strategy:).md)
  Modifies the format style to use the specified sign display strategy for displaying or omitting sign symbols.
- [enum NumberFormatStyleConfiguration](numberformatstyleconfiguration.md)
  Configuration settings for formatting numbers of different types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/floatingpointformatstyle/configuration)*