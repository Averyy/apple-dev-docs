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

Specify an offset that is a multiple of 4 bytes and a multiple of the platform’s buffer offset alignment.

## See Also

- [var instanceCount: Int](mtlinstanceaccelerationstructuredescriptor/instancecount.md)
  The number of instances in the instance descriptor buffer.
- [var instanceDescriptorBuffer: (any MTLBuffer)?](mtlinstanceaccelerationstructuredescriptor/instancedescriptorbuffer.md)
  A buffer that contains descriptions of each instance in the acceleration structure.
- [var instanceDescriptorStride: Int](mtlinstanceaccelerationstructuredescriptor/instancedescriptorstride.md)
  The stride, in bytes, between instance descriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlinstanceaccelerationstructuredescriptor/instancedescriptorbufferoffset)*