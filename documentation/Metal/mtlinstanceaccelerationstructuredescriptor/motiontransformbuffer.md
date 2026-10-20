# motionTransformBuffer

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

A buffer that contains descriptions of each motion transform in the acceleration structure.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var motionTransformBuffer: (any MTLBuffer)? { get set }
```

```objc
@property (nonatomic, retain, nullable) id<MTLBuffer> motionTransformBuffer;
```

## See Also

### Specifying motion data
- [var motionTransformCount: Int](./motiontransformcount.md)
  The number of motion transforms in the motion transform buffer.
- [var motionTransformBufferOffset: Int](./motiontransformbufferoffset.md)
  The offset, in bytes, to the descripton of the first motion transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlinstanceaccelerationstructuredescriptor/motiontransformbuffer)*