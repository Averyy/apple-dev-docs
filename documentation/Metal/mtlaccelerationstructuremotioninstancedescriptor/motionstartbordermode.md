# motionStartBorderMode

**Framework**: Metal  
**Kind**: property

The mode to use when handling timestamps before the start time.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var motionStartBorderMode: MTLMotionBorderMode
```

#### Discussion

The default value is [`MTLMotionBorderMode.clamp`](mtlmotionbordermode/clamp.md).

## See Also

- [var motionStartTime: Float](mtlaccelerationstructuremotioninstancedescriptor/motionstarttime.md)
  The start time for the range of motion described by the keyframe data.
- [var motionEndTime: Float](mtlaccelerationstructuremotioninstancedescriptor/motionendtime.md)
  The end time for the range of motion described by the keyframe data.
- [var motionEndBorderMode: MTLMotionBorderMode](mtlaccelerationstructuremotioninstancedescriptor/motionendbordermode.md)
  The mode to use when handling timestamps after the end time.
- [var motionTransformsStartIndex: UInt32](mtlaccelerationstructuremotioninstancedescriptor/motiontransformsstartindex.md)
  The index for the instance’s first keyframe motion data.
- [var motionTransformsCount: UInt32](mtlaccelerationstructuremotioninstancedescriptor/motiontransformscount.md)
  The number of keyframes for this instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructuremotioninstancedescriptor/motionstartbordermode)*