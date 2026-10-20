# motionTransformCount

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The number of motion transforms in the motion transform buffer.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var motionTransformCount: Int { get set }
```

```objc
@property (nonatomic) NSUInteger motionTransformCount;
```

## See Also

### Specifying motion data
- [var motionTransformBuffer: (any MTLBuffer)?](./motiontransformbuffer.md)
  A buffer that contains descriptions of each motion transform in the acceleration structure.
- [var motionTransformBufferOffset: Int](./motiontransformbufferoffset.md)
  The offset, in bytes, to the descripton of the first motion transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlinstanceaccelerationstructuredescriptor/motiontransformcount)*