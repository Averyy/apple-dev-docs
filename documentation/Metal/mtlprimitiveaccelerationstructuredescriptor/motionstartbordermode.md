# motionStartBorderMode

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

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
var motionStartBorderMode: MTLMotionBorderMode { get set }
```

```objc
@property (nonatomic) MTLMotionBorderMode motionStartBorderMode;
```

#### Discussion

The default value is [`MTLMotionBorderMode.clamp`](../mtlmotionbordermode/clamp.md).

## See Also

### Specifying motion behavior
- [var motionKeyframeCount: Int](./motionkeyframecount.md)
  The number of keyframes in the geometry data.
- [var motionStartTime: Float](./motionstarttime.md)
  The start time for the range of motion that the keyframe data describes.
- [var motionEndTime: Float](./motionendtime.md)
  The end time for the range of motion that the keyframe data describes.
- [var motionEndBorderMode: MTLMotionBorderMode](./motionendbordermode.md)
  The mode to use when handling timestamps after the end time.
- [enum MTLMotionBorderMode](../mtlmotionbordermode.md)
  Options for specifying how the acceleration structure handles timestamps that are outside the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlprimitiveaccelerationstructuredescriptor/motionstartbordermode)*