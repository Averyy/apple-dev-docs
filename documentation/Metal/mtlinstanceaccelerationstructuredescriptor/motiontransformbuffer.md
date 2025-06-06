# motionTransformBuffer

**Framework**: Metal  
**Kind**: property

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

## See Also

- [var motionTransformCount: Int](mtlinstanceaccelerationstructuredescriptor/motiontransformcount.md)
  The number of motion transforms in the motion transform buffer.
- [var motionTransformBufferOffset: Int](mtlinstanceaccelerationstructuredescriptor/motiontransformbufferoffset.md)
  The offset, in bytes, to the descripton of the first motion transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlinstanceaccelerationstructuredescriptor/motiontransformbuffer)*