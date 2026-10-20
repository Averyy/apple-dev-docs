# SKInterpolationMode

**Framework**: SpriteKit  
**Kind**: enum  
**Role**: Enumeration

The modes used to interpolate between keyframes in the sequence.

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
enum SKInterpolationMode
```

```c
enum SKInterpolationMode : NSInteger;
```

## Topics

### Constants
- [SKInterpolationMode.linear](./skinterpolationmode/linear.md)
  Values between two keyframes are interpolated linearly.
- [SKInterpolationMode.spline](./skinterpolationmode/spline.md)
  Values between two keyframes using a spline curve.
- [SKInterpolationMode.step](./skinterpolationmode/step.md)
  Values between two keyframes are not interpolated. Instead, the value is that of the most recent keyframe.
### Initializers
- [init?(rawValue: Int)](./skinterpolationmode/init%28rawvalue%29.md)

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
- [enum SKRepeatMode](./skrepeatmode.md)
  The modes used to determine how the sequence repeats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skinterpolationmode)*