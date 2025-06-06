# motionStartBorderMode

**Framework**: Metal  
**Kind**: property

The motion border mode describing what happens if Metal samples the acceleration structure before the motion start time.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var motionStartBorderMode: MTLMotionBorderMode
```

## See Also

- [var motionStartTime: Float](mtlindirectaccelerationstructuremotioninstancedescriptor/motionstarttime.md)
  The start time of the motion instance.
- [var motionEndTime: Float](mtlindirectaccelerationstructuremotioninstancedescriptor/motionendtime.md)
  The end time of the motion instance.
- [var motionEndBorderMode: MTLMotionBorderMode](mtlindirectaccelerationstructuremotioninstancedescriptor/motionendbordermode.md)
  The motion border mode describing what happens if Metal samples the acceleration structure after the motion end time.
- [var motionTransformsCount: UInt32](mtlindirectaccelerationstructuremotioninstancedescriptor/motiontransformscount.md)
  The number of motion transforms belonging to the motion instance.
- [var motionTransformsStartIndex: UInt32](mtlindirectaccelerationstructuremotioninstancedescriptor/motiontransformsstartindex.md)
  The index of the first set of transforms describing one keyframe of the animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectaccelerationstructuremotioninstancedescriptor/motionstartbordermode)*