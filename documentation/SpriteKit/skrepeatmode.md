# SKRepeatMode

**Framework**: SpriteKit  
**Kind**: enum  
**Role**: Enumeration

The modes used to determine how the sequence repeats.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
enum SKRepeatMode
```

```c
enum SKRepeatMode : NSInteger;
```

## Topics

### Constants
- [SKRepeatMode.clamp](./skrepeatmode/clamp.md)
  When a sample is calculated, the time value is clamped to the range of time values found in the sequence. For example, if the last keyframe’s time value is `0.5`, a sample at any time value from `0.5` to `1.0` returns the last keyframe’s value.
- [SKRepeatMode.loop](./skrepeatmode/loop.md)
  When a sample is calculated, the sequence loops back to the beginning of the sequence. For example, if the last keyframe’s time value is `0.5`, then a sample at any time value from `0.5` to `1.0` returns the same value as the sequence did from `0.0` to `0.5`.
### Initializers
- [init?(rawValue: Int)](./skrepeatmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Constants
- [enum SKInterpolationMode](./skinterpolationmode.md)
  The modes used to interpolate between keyframes in the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skrepeatmode)*