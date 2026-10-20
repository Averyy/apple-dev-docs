# NumberFormatter.Behavior

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

These constants specify the behavior of a number formatter. These constants are returned by the [`defaultFormatterBehavior()`](./defaultformatterbehavior%28%29.md) class method and the [`formatterBehavior`](./formatterbehavior.md) property.

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
enum Behavior
```

```c
enum NSNumberFormatterBehavior : NSUInteger;
```

## Topics

### Constants
- [NumberFormatter.Behavior.default](./behavior/default.md)
  The number-formatter behavior set as the default for new instances. You can set the default formatter behavior with the class method [`setDefaultFormatterBehavior(_:)`](./setdefaultformatterbehavior%28_%29.md).
- [NumberFormatter.Behavior.behavior10_0](./behavior/behavior10_0.md)
  The number-formatter behavior as it existed prior to macOS 10.4.
- [NumberFormatter.Behavior.behavior10_4](./behavior/behavior10_4.md)
  The number-formatter behavior since macOS 10.4.
### Initializers
- [init?(rawValue: UInt)](./behavior/init%28rawvalue%29.md)

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
- [NumberFormatter.PadPosition](./padposition.md)
  These constants are used to specify how numbers should be padded. These constants are used by the [`paddingPosition`](./paddingposition.md) property.
- [NumberFormatter.RoundingMode](./roundingmode-swift.enum.md)
  These constants are used to specify how numbers should be rounded. These constants are used by the [`roundingMode`](./roundingmode-swift.property.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/behavior)*