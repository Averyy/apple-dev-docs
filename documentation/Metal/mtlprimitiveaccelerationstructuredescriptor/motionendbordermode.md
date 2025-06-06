# motionEndBorderMode

**Framework**: Metal  
**Kind**: property

The mode to use when handling timestamps after the end time.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var motionEndBorderMode: MTLMotionBorderMode { get set }
```

#### Discussion

The default value is [`MTLMotionBorderMode.clamp`](mtlmotionbordermode/clamp.md).

## See Also

- [var motionKeyframeCount: Int](mtlprimitiveaccelerationstructuredescriptor/motionkeyframecount.md)
  The number of keyframes in the geometry data.
- [var motionStartTime: Float](mtlprimitiveaccelerationstructuredescriptor/motionstarttime.md)
  The start time for the range of motion that the keyframe data describes.
- [var motionEndTime: Float](mtlprimitiveaccelerationstructuredescriptor/motionendtime.md)
  The end time for the range of motion that the keyframe data describes.
- [var motionStartBorderMode: MTLMotionBorderMode](mtlprimitiveaccelerationstructuredescriptor/motionstartbordermode.md)
  The mode to use when handling timestamps before the start time.
- [enum MTLMotionBorderMode](mtlmotionbordermode.md)
  Options for specifying how the acceleration structure handles timestamps that are outside the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlprimitiveaccelerationstructuredescriptor/motionendbordermode)*