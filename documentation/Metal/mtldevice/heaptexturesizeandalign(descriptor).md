# heapTextureSizeAndAlign(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (MTLSizeAndAlign) heapTextureSizeAndAlignWithDescriptor:(MTLTextureDescriptor *) desc;
```

## Return Value

An [`MTLSizeAndAlign`](../mtlsizeandalign.md) instance.

## Discussion

Use this method to help estimate an appropriate size for a new heap before you create it.

## Parameters

- `desc`: An [`MTLTextureDescriptor`](../mtltexturedescriptor.md) instance.

## See Also

### Working with resource heaps
- [func makeHeap(descriptor: MTLHeapDescriptor) -> (any MTLHeap)?](./makeheap%28descriptor%29.md)
  Creates a new GPU heap instance.
- [func heapBufferSizeAndAlign(length: Int, options: MTLResourceOptions) -> MTLSizeAndAlign](./heapbuffersizeandalign%28length,options%29.md)
  Returns the size and alignment, in bytes, of a buffer if you create it from a heap.
- [func heapAccelerationStructureSizeAndAlign(size: Int) -> MTLSizeAndAlign](./heapaccelerationstructuresizeandalign%28size%29.md)
  Returns the size and alignment, in bytes, of an acceleration structure if you create it from a heap.
- [func heapAccelerationStructureSizeAndAlign(descriptor: MTLAccelerationStructureDescriptor) -> MTLSizeAndAlign](./heapaccelerationstructuresizeandalign%28descriptor%29.md)
  Returns the size and alignment, in bytes, of an acceleration structure if you create it from a heap with a descriptor.
- [struct MTLSizeAndAlign](../mtlsizeandalign.md)
  The size and alignment of a resource, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/heaptexturesizeandalign(descriptor:))*