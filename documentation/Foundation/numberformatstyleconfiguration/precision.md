# NumberFormatStyleConfiguration.Precision

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A structure that an integer format style uses to configure precision.

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
struct Precision
```

## Topics

### Precision configurations
- [static func significantDigits<R>(R) -> NumberFormatStyleConfiguration.Precision](./precision/significantdigits%28_%29-2rp7g.md)
  Returns a precision that constrains formatted values to a range of significant digits.
- [static func significantDigits(Int) -> NumberFormatStyleConfiguration.Precision](./precision/significantdigits%28_%29-9dvpr.md)
  Returns a precision that constrains formatted values to a given number of significant digits.
- [static func integerAndFractionLength<R1, R2>(integerLimits: R1, fractionLimits: R2) -> NumberFormatStyleConfiguration.Precision](./precision/integerandfractionlength%28integerlimits,fractionlimits%29.md)
  Returns a precision that constrains formatted values to ranges of allowed digits in the integer and fraction parts.
- [static func integerAndFractionLength(integer: Int, fraction: Int) -> NumberFormatStyleConfiguration.Precision](./precision/integerandfractionlength%28integer,fraction%29.md)
  Returns a precision that constrains formatted values a given number of allowed digits in the integer and fraction parts.
- [static func integerLength<R>(R) -> NumberFormatStyleConfiguration.Precision](./precision/integerlength%28_%29-u8ua.md)
  Returns a precision that constrains formatted values to a range of allowed digits in the integer part.
- [static func integerLength(Int) -> NumberFormatStyleConfiguration.Precision](./precision/integerlength%28_%29-1njyz.md)
  Returns a precision that constrains formatted values to a given number of allowed digits in the integer part.
- [static func fractionLength<R>(R) -> NumberFormatStyleConfiguration.Precision](./precision/fractionlength%28_%29-w6fk.md)
  Returns a precision that constrains formatted values to a range of allowed digits in the fraction part.
- [static func fractionLength(Int) -> NumberFormatStyleConfiguration.Precision](./precision/fractionlength%28_%29-3wkd9.md)
  Returns a precision that constrains formatted values to a given number of allowed digits in the fraction part.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Specifying Configuration
- [NumberFormatStyleConfiguration.DecimalSeparatorDisplayStrategy](./decimalseparatordisplaystrategy.md)
  A structure that an integer format style uses to configure a decimal separator display strategy.
- [NumberFormatStyleConfiguration.Grouping](./grouping.md)
  A structure that an integer format style uses to configure grouping.
- [NumberFormatStyleConfiguration.RoundingRule](./roundingrule.md)
  The type used for rounding rule values.
- [NumberFormatStyleConfiguration.SignDisplayStrategy](./signdisplaystrategy.md)
  A structure that an integer format style uses to configure a sign display strategy.
- [NumberFormatStyleConfiguration.Notation](./notation.md)
  A structure that an integer format style uses to configure notation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatstyleconfiguration/precision)*