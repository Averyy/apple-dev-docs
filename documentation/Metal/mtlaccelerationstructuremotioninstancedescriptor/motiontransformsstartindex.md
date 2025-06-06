# motionTransformsStartIndex

**Framework**: Metal  
**Kind**: property

The index for the instance’s first keyframe motion data.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var motionTransformsStartIndex: UInt32
```

#### Discussion

The index points to an entry in the [`MTLInstanceAccelerationStructureDescriptor`](mtlinstanceaccelerationstructuredescriptor.md)’s transform data, stored in its [`motionTransformBuffer`](mtlinstanceaccelerationstructuredescriptor/motiontransformbuffer.md) property.

## See Also

- [var motionStartTime: Float](mtlaccelerationstructuremotioninstancedescriptor/motionstarttime.md)
  The start time for the range of motion described by the keyframe data.
- [var motionEndTime: Float](mtlaccelerationstructuremotioninstancedescriptor/motionendtime.md)
  The end time for the range of motion described by the keyframe data.
- [var motionStartBorderMode: MTLMotionBorderMode](mtlaccelerationstructuremotioninstancedescriptor/motionstartbordermode.md)
  The mode to use when handling timestamps before the start time.
- [var motionEndBorderMode: MTLMotionBorderMode](mtlaccelerationstructuremotioninstancedescriptor/motionendbordermode.md)
  The mode to use when handling timestamps after the end time.
- [var motionTransformsCount: UInt32](mtlaccelerationstructuremotioninstancedescriptor/motiontransformscount.md)
  The number of keyframes for this instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructuremotioninstancedescriptor/motiontransformsstartindex)*