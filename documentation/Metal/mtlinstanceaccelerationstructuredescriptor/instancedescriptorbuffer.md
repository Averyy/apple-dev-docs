# instanceDescriptorBuffer

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

A buffer that contains descriptions of each instance in the acceleration structure.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var instanceDescriptorBuffer: (any MTLBuffer)? { get set }
```

```objc
@property (nonatomic, retain, nullable) id<MTLBuffer> instanceDescriptorBuffer;
```

#### Discussion

You need to set a buffer before creating the instanced acceleration structure. The buffer needs to contain a list of instance data structures, each defining the characteristics of an instance. The descriptor’s [`instanceDescriptorType`](./instancedescriptortype.md) property determines which memory layout to use for the instance data; see [`MTLAccelerationStructureInstanceDescriptorType`](../mtlaccelerationstructureinstancedescriptortype.md) for more information.

## See Also

### Specifying the list of instances
- [var instanceCount: Int](./instancecount.md)
  The number of instances in the instance descriptor buffer.
- [var instanceDescriptorBufferOffset: Int](./instancedescriptorbufferoffset.md)
  The offset, in bytes, to the descripton of the first instance.
- [var instanceDescriptorStride: Int](./instancedescriptorstride.md)
  The stride, in bytes, between instance descriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlinstanceaccelerationstructuredescriptor/instancedescriptorbuffer)*