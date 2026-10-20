# motionTransformBufferOffset

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The offset, in bytes, to the descripton of the first motion transform.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var motionTransformBufferOffset: Int { get set }
```

```objc
@property (nonatomic) NSUInteger motionTransformBufferOffset;
```

#### Discussion

The offset needs to be a multiple of 64 bytes. Check the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) for potential alignment restrictions.

## See Also

### Specifying motion data
- [var motionTransformCount: Int](./motiontransformcount.md)
  The number of motion transforms in the motion transform buffer.
- [var motionTransformBuffer: (any MTLBuffer)?](./motiontransformbuffer.md)
  A buffer that contains descriptions of each motion transform in the acceleration structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlinstanceaccelerationstructuredescriptor/motiontransformbufferoffset)*