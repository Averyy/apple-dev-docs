# NumberFormatStyleConfiguration.Precision

**Framework**: Foundation  
**Kind**: struct

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
- [static func significantDigits<R>(R) -> NumberFormatStyleConfiguration.Precision](numberformatstyleconfiguration/precision/significantdigits(_:)-2rp7g.md)
  Returns a precision that constrains formatted values to a range of significant digits.
- [static func significantDigits(Int) -> NumberFormatStyleConfiguration.Precision](numberformatstyleconfiguration/precision/significantdigits(_:)-9dvpr.md)
  Returns a precision that constrains formatted values to a given number of significant digits.
- [static func integerAndFractionLength<R1, R2>(integerLimits: R1, fractionLimits: R2) -> NumberFormatStyleConfiguration.Precision](numberformatstyleconfiguration/precision/integerandfractionlength(integerlimits:fractionlimits:).md)
  Returns a precision that constrains formatted values to ranges of allowed digits in the integer and fraction parts.
- [static func integerAndFractionLength(integer: Int, fraction: Int) -> NumberFormatStyleConfiguration.Precision](numberformatstyleconfiguration/precision/integerandfractionlength(integer:fraction:).md)
  Returns a precision that constrains formatted values a given number of allowed digits in the integer and fraction parts.
- [static func integerLength<R>(R) -> NumberFormatStyleConfiguration.Precision](numberformatstyleconfiguration/precision/integerlength(_:)-u8ua.md)
  Returns a precision that constrains formatted values to a range of allowed digits in the integer part.
- [static func integerLength(Int) -> NumberFormatStyleConfiguration.Precision](numberformatstyleconfiguration/precision/integerlength(_:)-1njyz.md)
  Returns a precision that constrains formatted values to a given number of allowed digits in the integer part.
- [static func fractionLength<R>(R) -> NumberFormatStyleConfiguration.Precision](numberformatstyleconfiguration/precision/fractionlength(_:)-w6fk.md)
  Returns a precision that constrains formatted values to a range of allowed digits in the fraction part.
- [static func fractionLength(Int) -> NumberFormatStyleConfiguration.Precision](numberformatstyleconfiguration/precision/fractionlength(_:)-3wkd9.md)
  Returns a precision that constrains formatted values to a given number of allowed digits in the fraction part.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [NumberFormatStyleConfiguration.DecimalSeparatorDisplayStrategy](numberformatstyleconfiguration/decimalseparatordisplaystrategy.md)
  A structure that an integer format style uses to configure a decimal separator display strategy.
- [NumberFormatStyleConfiguration.Grouping](numberformatstyleconfiguration/grouping.md)
  A structure that an integer format style uses to configure grouping.
- [NumberFormatStyleConfiguration.RoundingRule](numberformatstyleconfiguration/roundingrule.md)
  The type used for rounding rule values.
- [NumberFormatStyleConfiguration.SignDisplayStrategy](numberformatstyleconfiguration/signdisplaystrategy.md)
  A structure that an integer format style uses to configure a sign display strategy.
- [NumberFormatStyleConfiguration.Notation](numberformatstyleconfiguration/notation.md)
  A structure that an integer format style uses to configure notation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatstyleconfiguration/precision)*