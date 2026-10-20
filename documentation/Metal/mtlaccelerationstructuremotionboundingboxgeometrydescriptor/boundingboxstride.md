# boundingBoxStride

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The stride, in bytes, between bounding boxes in each buffer.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var boundingBoxStride: Int { get set }
```

```objc
@property (nonatomic) NSUInteger boundingBoxStride;
```

## See Also

### Specifying bounding boxes data
- [var boundingBoxBuffers: [MTLMotionKeyframeData]](./boundingboxbuffers.md)
  A array of motion keyframes, each containing bounding box data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructuremotionboundingboxgeometrydescriptor/boundingboxstride)*