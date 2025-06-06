# instanceCount

**Framework**: Metal  
**Kind**: property

The number of instances in the instance descriptor buffer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var instanceCount: Int { get set }
```

## See Also

- [var instanceDescriptorBuffer: (any MTLBuffer)?](mtlinstanceaccelerationstructuredescriptor/instancedescriptorbuffer.md)
  A buffer that contains descriptions of each instance in the acceleration structure.
- [var instanceDescriptorBufferOffset: Int](mtlinstanceaccelerationstructuredescriptor/instancedescriptorbufferoffset.md)
  The offset, in bytes, to the descripton of the first instance.
- [var instanceDescriptorStride: Int](mtlinstanceaccelerationstructuredescriptor/instancedescriptorstride.md)
  The stride, in bytes, between instance descriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlinstanceaccelerationstructuredescriptor/instancecount)*