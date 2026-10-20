# motionStartTime

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The start time for the range of motion that the keyframe data describes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var motionStartTime: Float { get set }
```

```objc
@property (nonatomic) float motionStartTime;
```

#### Discussion

The default value is `0.0f`.

## See Also

### Specifying motion behavior
- [var motionKeyframeCount: Int](./motionkeyframecount.md)
  The number of keyframes in the geometry data.
- [var motionEndTime: Float](./motionendtime.md)
  The end time for the range of motion that the keyframe data describes.
- [var motionStartBorderMode: MTLMotionBorderMode](./motionstartbordermode.md)
  The mode to use when handling timestamps before the start time.
- [var motionEndBorderMode: MTLMotionBorderMode](./motionendbordermode.md)
  The mode to use when handling timestamps after the end time.
- [enum MTLMotionBorderMode](../mtlmotionbordermode.md)
  Options for specifying how the acceleration structure handles timestamps that are outside the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlprimitiveaccelerationstructuredescriptor/motionstarttime)*