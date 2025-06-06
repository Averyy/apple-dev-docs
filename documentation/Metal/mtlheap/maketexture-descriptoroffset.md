# makeTexture(descriptor:offset:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a texture at a specified offset on the heap.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func makeTexture(descriptor: MTLTextureDescriptor, offset: Int) -> (any MTLTexture)?
```

#### Return Value

A new texture, or `nil` if the heap is not a placement heap.

#### Discussion

The heap’s type must be [`MTLHeapType.placement`](mtlheaptype/placement.md).

The texture’s CPU cache mode must match the heap’s [`cpuCacheMode`](mtlheap/cpucachemode.md) value. The texture’s storage mode must either match the heap’s [`storageMode`](mtlheap/storagemode.md) value or be a [`MTLStorageMode.memoryless`](mtlstoragemode/memoryless.md) value.

Use the [`heapBufferSizeAndAlign(length:options:)`](mtldevice/heapbuffersizeandalign(length:options:).md) to determine the required size and alignment. If you don’t align the texture correctly or it extends past the end of the heap, the behavior is undefined.

Any resources in the heap within an overlapping half-open range `[offset, offset + requiredSize)` are implicitly aliased with the new resource.

## Parameters

- `descriptor`: A descriptor object that describes the properties of the texture.
- `offset`: The distance, in bytes, to place the texture relative to the start of the heap.

## See Also

- [func makeBuffer(length: Int, options: MTLResourceOptions) -> (any MTLBuffer)?](mtlheap/makebuffer(length:options:).md)
  Creates a buffer on the heap.
- [func makeTexture(descriptor: MTLTextureDescriptor) -> (any MTLTexture)?](mtlheap/maketexture(descriptor:).md)
  Creates a texture on the heap.
- [func makeBuffer(length: Int, options: MTLResourceOptions, offset: Int) -> (any MTLBuffer)?](mtlheap/makebuffer(length:options:offset:).md)
  Creates a buffer at a specified offset on the heap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheap/maketexture(descriptor:offset:))*