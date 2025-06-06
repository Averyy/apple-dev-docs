# heapTextureSizeAndAlign(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Returns the size and alignment, in bytes, of a texture if you create it from a heap.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func heapTextureSizeAndAlign(descriptor desc: MTLTextureDescriptor) -> MTLSizeAndAlign
```

#### Return Value

An [`MTLSizeAndAlign`](mtlsizeandalign.md) instance.

#### Discussion

Use this method to help estimate an appropriate size for a new heap before you create it.

## Parameters

- `desc`: An   instance.

## See Also

- [func makeHeap(descriptor: MTLHeapDescriptor) -> (any MTLHeap)?](mtldevice/makeheap(descriptor:).md)
  Creates a new GPU heap instance.
- [func heapBufferSizeAndAlign(length: Int, options: MTLResourceOptions) -> MTLSizeAndAlign](mtldevice/heapbuffersizeandalign(length:options:).md)
  Returns the size and alignment, in bytes, of a buffer if you create it from a heap.
- [func heapAccelerationStructureSizeAndAlign(size: Int) -> MTLSizeAndAlign](mtldevice/heapaccelerationstructuresizeandalign(size:).md)
  Returns the size and alignment, in bytes, of an acceleration structure if you create it from a heap.
- [func heapAccelerationStructureSizeAndAlign(descriptor: MTLAccelerationStructureDescriptor) -> MTLSizeAndAlign](mtldevice/heapaccelerationstructuresizeandalign(descriptor:).md)
  Returns the size and alignment, in bytes, of an acceleration structure if you create it from a heap with a descriptor.
- [struct MTLSizeAndAlign](mtlsizeandalign.md)
  The size and alignment of a resource, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/heaptexturesizeandalign(descriptor:))*