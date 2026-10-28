# motionKeyframeCount

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The number of keyframes in the geometry data.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var motionKeyframeCount: Int { get set }
```

```objc
@property (nonatomic) NSUInteger motionKeyframeCount;
```

## Discussion

The default value is `1`. If the value is greater than `1`, all geometry descriptors that you attach to this descriptor need to be motion descriptors, and each needs to have exactly that many [`MTLMotionKeyframeData`](../mtlmotionkeyframedata.md) objects.

## See Also

### Related Documentation
- [var geometryDescriptors: [MTLAccelerationStructureGeometryDescriptor]?](./geometrydescriptors.md)
  An array that contains the individual pieces of geometry that compose the acceleration structure.
### Specifying motion behavior
- [var motionStartTime: Float](./motionstarttime.md)
  The start time for the range of motion that the keyframe data describes.
- [var motionEndTime: Float](./motionendtime.md)
  The end time for the range of motion that the keyframe data describes.
- [var motionStartBorderMode: MTLMotionBorderMode](./motionstartbordermode.md)
  The mode to use when handling timestamps before the start time.
- [var motionEndBorderMode: MTLMotionBorderMode](./motionendbordermode.md)
  The mode to use when handling timestamps after the end time.
- [enum MTLMotionBorderMode](../mtlmotionbordermode.md)
  Options for specifying how the acceleration structure handles timestamps that are outside the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlprimitiveaccelerationstructuredescriptor/motionkeyframecount)*