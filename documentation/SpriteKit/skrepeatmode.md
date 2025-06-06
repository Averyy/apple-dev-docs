# SKRepeatMode

**Framework**: SpriteKit  
**Kind**: enum

The modes used to determine how the sequence repeats.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum SKRepeatMode
```

## Topics

### Constants
- [SKRepeatMode.clamp](skrepeatmode/clamp.md)
  When a sample is calculated, the time value is clamped to the range of time values found in the sequence. For example, if the last keyframe’s time value is `0.5`, a sample at any time value from `0.5` to `1.0` returns the last keyframe’s value.
- [SKRepeatMode.loop](skrepeatmode/loop.md)
  When a sample is calculated, the sequence loops back to the beginning of the sequence. For example, if the last keyframe’s time value is `0.5`, then a sample at any time value from `0.5` to `1.0` returns the same value as the sequence did from `0.0` to `0.5`.
### Initializers
- [init?(rawValue: Int)](skrepeatmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum SKInterpolationMode](skinterpolationmode.md)
  The modes used to interpolate between keyframes in the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skrepeatmode)*