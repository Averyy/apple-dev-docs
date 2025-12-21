# makeHeap(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a new GPU heap instance.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func makeHeap(descriptor: MTLHeapDescriptor) -> (any MTLHeap)?
```

#### Return Value

A new [`MTLHeap`](mtlheap.md) instance if the method completed successfully; otherwise nil.

#### Discussion

For more information about using heaps, see [`Memory heaps`](memory-heaps.md).

## Parameters

- `descriptor`: An   instance.

## See Also

- [func heapBufferSizeAndAlign(length: Int, options: MTLResourceOptions) -> MTLSizeAndAlign](mtldevice/heapbuffersizeandalign(length:options:).md)
  Returns the size and alignment, in bytes, of a buffer if you create it from a heap.
- [func heapTextureSizeAndAlign(descriptor: MTLTextureDescriptor) -> MTLSizeAndAlign](mtldevice/heaptexturesizeandalign(descriptor:).md)
  Returns the size and alignment, in bytes, of a texture if you create it from a heap.
- [func heapAccelerationStructureSizeAndAlign(size: Int) -> MTLSizeAndAlign](mtldevice/heapaccelerationstructuresizeandalign(size:).md)
  Returns the size and alignment, in bytes, of an acceleration structure if you create it from a heap.
- [func heapAccelerationStructureSizeAndAlign(descriptor: MTLAccelerationStructureDescriptor) -> MTLSizeAndAlign](mtldevice/heapaccelerationstructuresizeandalign(descriptor:).md)
  Returns the size and alignment, in bytes, of an acceleration structure if you create it from a heap with a descriptor.
- [struct MTLSizeAndAlign](mtlsizeandalign.md)
  The size and alignment of a resource, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makeheap(descriptor:))*