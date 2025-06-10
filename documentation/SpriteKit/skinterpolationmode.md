# SKInterpolationMode

**Framework**: SpriteKit  
**Kind**: enum

The modes used to interpolate between keyframes in the sequence.

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
enum SKInterpolationMode
```

## Topics

### Constants
- [SKInterpolationMode.linear](skinterpolationmode/linear.md)
  Values between two keyframes are interpolated linearly.
- [SKInterpolationMode.spline](skinterpolationmode/spline.md)
  Values between two keyframes using a spline curve.
- [SKInterpolationMode.step](skinterpolationmode/step.md)
  Values between two keyframes are not interpolated. Instead, the value is that of the most recent keyframe.
### Initializers
- [init?(rawValue: Int)](skinterpolationmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum SKRepeatMode](skrepeatmode.md)
  The modes used to determine how the sequence repeats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skinterpolationmode)*