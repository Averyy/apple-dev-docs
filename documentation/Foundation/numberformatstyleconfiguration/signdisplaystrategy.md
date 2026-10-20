# NumberFormatStyleConfiguration.SignDisplayStrategy

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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
- [static var automatic: NumberFormatStyleConfiguration.SignDisplayStrategy](./signdisplaystrategy/automatic.md)
  A strategy to automatically configure locale-appropriate sign display behavior.
- [static func always(includingZero: Bool) -> NumberFormatStyleConfiguration.SignDisplayStrategy](./signdisplaystrategy/always%28includingzero%29.md)
  A strategy to always display sign symbols.
- [static var never: NumberFormatStyleConfiguration.SignDisplayStrategy](./signdisplaystrategy/never.md)
  A strategy to never display sign symbols.

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
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
- [NumberFormatStyleConfiguration.Precision](./precision.md)
  A structure that an integer format style uses to configure precision.
- [NumberFormatStyleConfiguration.RoundingRule](./roundingrule.md)
  The type used for rounding rule values.
- [NumberFormatStyleConfiguration.Notation](./notation.md)
  A structure that an integer format style uses to configure notation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatstyleconfiguration/signdisplaystrategy)*