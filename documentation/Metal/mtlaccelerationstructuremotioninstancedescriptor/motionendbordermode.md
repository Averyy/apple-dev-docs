# motionEndBorderMode

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

A behavior that configures how a motion instance handles timestamps after an ending time.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var motionEndBorderMode: MTLMotionBorderMode
```

```c
MTLMotionBorderMode motionEndBorderMode;
```

## Discussion

The property’s default value is [`MTLMotionBorderMode.clamp`](../mtlmotionbordermode/clamp.md).

## See Also

### Specifying motion data
- [var motionStartTime: Float](./motionstarttime.md)
  A starting time for the range of motion that the key-frame data represents.
- [var motionEndTime: Float](./motionendtime.md)
  An ending time for the range of motion that the key-frame data represents.
- [var motionStartBorderMode: MTLMotionBorderMode](./motionstartbordermode.md)
  A behavior that configures how a motion instance handles timestamps before a starting time.
- [var motionTransformsStartIndex: UInt32](./motiontransformsstartindex.md)
  The index of motion data that represents the first key-frame motion data, which applies to the next acceleration-structure motion instance you create with the descriptor.
- [var motionTransformsCount: UInt32](./motiontransformscount.md)
  The number of motion data key-frames, which applies to the next acceleration-structure motion instance you create with the descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructuremotioninstancedescriptor/motionendbordermode)*