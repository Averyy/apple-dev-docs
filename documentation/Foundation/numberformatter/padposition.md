# NumberFormatter.PadPosition

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

These constants are used to specify how numbers should be padded. These constants are used by the [`paddingPosition`](./paddingposition.md) property.

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
enum PadPosition
```

```c
enum NSNumberFormatterPadPosition : NSUInteger;
```

## Topics

### Constants
- [NumberFormatter.PadPosition.beforePrefix](./padposition/beforeprefix.md)
  Specifies that the padding should occur before the prefix.
- [NumberFormatter.PadPosition.afterPrefix](./padposition/afterprefix.md)
  Specifies that the padding should occur after the prefix.
- [NumberFormatter.PadPosition.beforeSuffix](./padposition/beforesuffix.md)
  Specifies that the padding should occur before the suffix.
- [NumberFormatter.PadPosition.afterSuffix](./padposition/aftersuffix.md)
  Specifies that the padding should occur after the suffix.
### Initializers
- [init?(rawValue: UInt)](./padposition/init%28rawvalue%29.md)

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
- [NumberFormatter.RoundingMode](./roundingmode-swift.enum.md)
  These constants are used to specify how numbers should be rounded. These constants are used by the [`roundingMode`](./roundingmode-swift.property.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/padposition)*