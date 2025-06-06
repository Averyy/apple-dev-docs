# instanceDescriptorStride

**Framework**: Metal  
**Kind**: property

The stride, in bytes, between instance descriptions.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var instanceDescriptorStride: Int { get set }
```

#### Discussion

The stride must be at least 64 bytes and must be a multiple of 4 bytes. Defaults to 64 bytes.

## See Also

- [var instanceCount: Int](mtlinstanceaccelerationstructuredescriptor/instancecount.md)
  The number of instances in the instance descriptor buffer.
- [var instanceDescriptorBuffer: (any MTLBuffer)?](mtlinstanceaccelerationstructuredescriptor/instancedescriptorbuffer.md)
  A buffer that contains descriptions of each instance in the acceleration structure.
- [var instanceDescriptorBufferOffset: Int](mtlinstanceaccelerationstructuredescriptor/instancedescriptorbufferoffset.md)
  The offset, in bytes, to the descripton of the first instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlinstanceaccelerationstructuredescriptor/instancedescriptorstride)*