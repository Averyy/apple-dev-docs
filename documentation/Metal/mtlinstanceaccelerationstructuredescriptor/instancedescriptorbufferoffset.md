# instanceDescriptorBufferOffset

**Framework**: Metal  
**Kind**: property

The offset, in bytes, to the descripton of the first instance.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var instanceDescriptorBufferOffset: Int { get set }
```

#### Discussion

The offset needs to be a multiple of 64 bytes. Check the [`Metal feature set tables (PDF)`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) for potential alignment restrictions.

## See Also

- [var instanceCount: Int](mtlinstanceaccelerationstructuredescriptor/instancecount.md)
  The number of instances in the instance descriptor buffer.
- [var instanceDescriptorBuffer: (any MTLBuffer)?](mtlinstanceaccelerationstructuredescriptor/instancedescriptorbuffer.md)
  A buffer that contains descriptions of each instance in the acceleration structure.
- [var instanceDescriptorStride: Int](mtlinstanceaccelerationstructuredescriptor/instancedescriptorstride.md)
  The stride, in bytes, between instance descriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlinstanceaccelerationstructuredescriptor/instancedescriptorbufferoffset)*