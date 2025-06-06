# NumberFormatStyleConfiguration.SignDisplayStrategy

**Framework**: Foundation  
**Kind**: struct

A structure that an integer format style uses to configure a sign display strategy.

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
struct SignDisplayStrategy
```

## Topics

### Sign display strategies
- [static var automatic: NumberFormatStyleConfiguration.SignDisplayStrategy](numberformatstyleconfiguration/signdisplaystrategy/automatic.md)
  A strategy to automatically configure locale-appropriate sign display behavior.
- [static func always(includingZero: Bool) -> NumberFormatStyleConfiguration.SignDisplayStrategy](numberformatstyleconfiguration/signdisplaystrategy/always(includingzero:).md)
  A strategy to always display sign symbols.
- [static var never: NumberFormatStyleConfiguration.SignDisplayStrategy](numberformatstyleconfiguration/signdisplaystrategy/never.md)
  A strategy to never display sign symbols.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [NumberFormatStyleConfiguration.DecimalSeparatorDisplayStrategy](numberformatstyleconfiguration/decimalseparatordisplaystrategy.md)
  A structure that an integer format style uses to configure a decimal separator display strategy.
- [NumberFormatStyleConfiguration.Grouping](numberformatstyleconfiguration/grouping.md)
  A structure that an integer format style uses to configure grouping.
- [NumberFormatStyleConfiguration.Precision](numberformatstyleconfiguration/precision.md)
  A structure that an integer format style uses to configure precision.
- [NumberFormatStyleConfiguration.RoundingRule](numberformatstyleconfiguration/roundingrule.md)
  The type used for rounding rule values.
- [NumberFormatStyleConfiguration.Notation](numberformatstyleconfiguration/notation.md)
  A structure that an integer format style uses to configure notation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatstyleconfiguration/signdisplaystrategy)*