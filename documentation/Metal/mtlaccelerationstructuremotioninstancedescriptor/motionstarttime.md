# motionStartTime

**Framework**: Metal  
**Kind**: property

A starting time for the range of motion that the key-frame data represents.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var motionStartTime: Float
```

#### Discussion

The [`motionTransformsStartIndex`](mtlaccelerationstructuremotioninstancedescriptor/motiontransformsstartindex.md) and [`motionTransformsCount`](mtlaccelerationstructuremotioninstancedescriptor/motiontransformscount.md) properties represent the key-frame motion data.

The property’s default value is `0.0`.

## See Also

- [var motionEndTime: Float](mtlaccelerationstructuremotioninstancedescriptor/motionendtime.md)
  An ending time for the range of motion that the key-frame data represents.
- [var motionStartBorderMode: MTLMotionBorderMode](mtlaccelerationstructuremotioninstancedescriptor/motionstartbordermode.md)
  A behavior that configures how a motion instance handles timestamps before a starting time.
- [var motionEndBorderMode: MTLMotionBorderMode](mtlaccelerationstructuremotioninstancedescriptor/motionendbordermode.md)
  A behavior that configures how a motion instance handles timestamps after an ending time.
- [var motionTransformsStartIndex: UInt32](mtlaccelerationstructuremotioninstancedescriptor/motiontransformsstartindex.md)
  The index of motion data that represents the first key-frame motion data, which applies to the next acceleration-structure motion instance you create with the descriptor.
- [var motionTransformsCount: UInt32](mtlaccelerationstructuremotioninstancedescriptor/motiontransformscount.md)
  The number of motion data key-frames, which applies to the next acceleration-structure motion instance you create with the descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructuremotioninstancedescriptor/motionstarttime)*