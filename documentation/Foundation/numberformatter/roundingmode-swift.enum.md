# NumberFormatter.RoundingMode

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

These constants are used to specify how numbers should be rounded. These constants are used by the [`roundingMode`](./roundingmode-swift.property.md) property.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum RoundingMode
```

```c
enum NSNumberFormatterRoundingMode : NSUInteger;
```

## Topics

### Constants
- [NumberFormatter.RoundingMode.ceiling](./roundingmode-swift.enum/ceiling.md)
  Round towards positive infinity.
- [NumberFormatter.RoundingMode.floor](./roundingmode-swift.enum/floor.md)
  Round towards negative infinity.
- [NumberFormatter.RoundingMode.down](./roundingmode-swift.enum/down.md)
  Round towards zero.
- [NumberFormatter.RoundingMode.up](./roundingmode-swift.enum/up.md)
  Round away from zero.
- [NumberFormatter.RoundingMode.halfEven](./roundingmode-swift.enum/halfeven.md)
  Round towards the nearest integer, or towards an even number if equidistant.
- [NumberFormatter.RoundingMode.halfDown](./roundingmode-swift.enum/halfdown.md)
  Round towards the nearest integer, or towards zero if equidistant.
- [NumberFormatter.RoundingMode.halfUp](./roundingmode-swift.enum/halfup.md)
  Round towards the nearest integer, or away from zero if equidistant.
### Initializers
- [init?(rawValue: UInt)](./roundingmode-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [NumberFormatter.Style](./style.md)
  The predefined number format styles used by the [`numberStyle`](./numberstyle.md) property.
- [NumberFormatter.Behavior](./behavior.md)
  These constants specify the behavior of a number formatter. These constants are returned by the [`defaultFormatterBehavior()`](./defaultformatterbehavior%28%29.md) class method and the [`formatterBehavior`](./formatterbehavior.md) property.
- [NumberFormatter.PadPosition](./padposition.md)
  These constants are used to specify how numbers should be padded. These constants are used by the [`paddingPosition`](./paddingposition.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/roundingmode-swift.enum)*