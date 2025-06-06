# heapAccelerationStructureSizeAndAlign(size:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Returns the size and alignment, in bytes, of an acceleration structure if you create it from a heap.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func heapAccelerationStructureSizeAndAlign(size: Int) -> MTLSizeAndAlign
```

#### Return Value

An [`MTLSizeAndAlign`](mtlsizeandalign.md) instance

#### Discussion

Use this method to help estimate an appropriate size for a new heap before you create it.

## Parameters

- `size`: The size of an acceleration structure, in bytes.

## See Also

- [func makeHeap(descriptor: MTLHeapDescriptor) -> (any MTLHeap)?](mtldevice/makeheap(descriptor:).md)
  Creates a new GPU heap instance.
- [func heapBufferSizeAndAlign(length: Int, options: MTLResourceOptions) -> MTLSizeAndAlign](mtldevice/heapbuffersizeandalign(length:options:).md)
  Returns the size and alignment, in bytes, of a buffer if you create it from a heap.
- [func heapTextureSizeAndAlign(descriptor: MTLTextureDescriptor) -> MTLSizeAndAlign](mtldevice/heaptexturesizeandalign(descriptor:).md)
  Returns the size and alignment, in bytes, of a texture if you create it from a heap.
- [func heapAccelerationStructureSizeAndAlign(descriptor: MTLAccelerationStructureDescriptor) -> MTLSizeAndAlign](mtldevice/heapaccelerationstructuresizeandalign(descriptor:).md)
  Returns the size and alignment, in bytes, of an acceleration structure if you create it from a heap with a descriptor.
- [struct MTLSizeAndAlign](mtlsizeandalign.md)
  The size and alignment of a resource, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/heapaccelerationstructuresizeandalign(size:))*