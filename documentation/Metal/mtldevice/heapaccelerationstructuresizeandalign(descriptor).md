# heapAccelerationStructureSizeAndAlign(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the size and alignment, in bytes, of an acceleration structure if you create it from a heap with a descriptor.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func heapAccelerationStructureSizeAndAlign(descriptor: MTLAccelerationStructureDescriptor) -> MTLSizeAndAlign
```

```objc
- (MTLSizeAndAlign) heapAccelerationStructureSizeAndAlignWithDescriptor:(MTLAccelerationStructureDescriptor *) descriptor;
```

#### Return Value

An [`MTLSizeAndAlign`](../mtlsizeandalign.md) instance.

#### Discussion

Use this method to help estimate an appropriate size for a new heap before you create it.

## Parameters

- `descriptor`: An [`MTLAccelerationStructureDescriptor`](../mtlaccelerationstructuredescriptor.md) instance.

## See Also

### Working with resource heaps
- [func makeHeap(descriptor: MTLHeapDescriptor) -> (any MTLHeap)?](./makeheap%28descriptor%29.md)
  Creates a new GPU heap instance.
- [func heapBufferSizeAndAlign(length: Int, options: MTLResourceOptions) -> MTLSizeAndAlign](./heapbuffersizeandalign%28length,options%29.md)
  Returns the size and alignment, in bytes, of a buffer if you create it from a heap.
- [func heapTextureSizeAndAlign(descriptor: MTLTextureDescriptor) -> MTLSizeAndAlign](./heaptexturesizeandalign%28descriptor%29.md)
  Returns the size and alignment, in bytes, of a texture if you create it from a heap.
- [func heapAccelerationStructureSizeAndAlign(size: Int) -> MTLSizeAndAlign](./heapaccelerationstructuresizeandalign%28size%29.md)
  Returns the size and alignment, in bytes, of an acceleration structure if you create it from a heap.
- [struct MTLSizeAndAlign](../mtlsizeandalign.md)
  The size and alignment of a resource, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/heapaccelerationstructuresizeandalign(descriptor:))*