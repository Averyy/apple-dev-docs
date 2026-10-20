# boundingBoxBuffers

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

A array of motion keyframes, each containing bounding box data.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var boundingBoxBuffers: [MTLMotionKeyframeData] { get set }
```

```objc
@property (nonatomic, copy) NSArray<MTLMotionKeyframeData *> * boundingBoxBuffers;
```

## See Also

### Specifying bounding boxes data
- [var boundingBoxStride: Int](./boundingboxstride.md)
  The stride, in bytes, between bounding boxes in each buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructuremotionboundingboxgeometrydescriptor/boundingboxbuffers)*