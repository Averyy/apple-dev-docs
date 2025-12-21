# MTLMotionBorderMode

**Framework**: Metal  
**Kind**: enum

Options for specifying how the acceleration structure handles timestamps that are outside the specified range.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum MTLMotionBorderMode
```

#### Overview

The [`motionStartBorderMode`](mtlprimitiveaccelerationstructuredescriptor/motionstartbordermode.md) and [`motionEndBorderMode`](mtlprimitiveaccelerationstructuredescriptor/motionendbordermode.md) properties use this type to describe the behavior for a motion-based object when a timestamp is outside the specified range.

## Topics

### Specifying motion modes
- [MTLMotionBorderMode.clamp](mtlmotionbordermode/clamp.md)
  A mode that specifies treating times outside the specified endpoint as if they were at the endpoint.
- [MTLMotionBorderMode.vanish](mtlmotionbordermode/vanish.md)
  A mode that specifies that times outside the specified endpoint need to prevent any ray-intersections with the primitive.
### Initializers
- [init?(rawValue: UInt32)](mtlmotionbordermode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var motionKeyframeCount: Int](mtlprimitiveaccelerationstructuredescriptor/motionkeyframecount.md)
  The number of keyframes in the geometry data.
- [var motionStartTime: Float](mtlprimitiveaccelerationstructuredescriptor/motionstarttime.md)
  The start time for the range of motion that the keyframe data describes.
- [var motionEndTime: Float](mtlprimitiveaccelerationstructuredescriptor/motionendtime.md)
  The end time for the range of motion that the keyframe data describes.
- [var motionStartBorderMode: MTLMotionBorderMode](mtlprimitiveaccelerationstructuredescriptor/motionstartbordermode.md)
  The mode to use when handling timestamps before the start time.
- [var motionEndBorderMode: MTLMotionBorderMode](mtlprimitiveaccelerationstructuredescriptor/motionendbordermode.md)
  The mode to use when handling timestamps after the end time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlmotionbordermode)*