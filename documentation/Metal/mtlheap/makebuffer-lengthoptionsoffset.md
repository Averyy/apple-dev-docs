# makeBuffer(length:options:offset:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a buffer at a specified offset on the heap.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func makeBuffer(length: Int, options: MTLResourceOptions = [], offset: Int) -> (any MTLBuffer)?
```

#### Return Value

A new buffer, or `nil` if the heap is not a placement heap.

#### Discussion

The heap’s type must be [`MTLHeapType.placement`](mtlheaptype/placement.md).

Use the [`heapBufferSizeAndAlign(length:options:)`](mtldevice/heapbuffersizeandalign(length:options:).md) method to determine the required size and alignment. If you don’t align the buffer correctly or it extends past the end of the heap, the behavior is undefined.

Any resources in the heap within an overlapping half-open range `[offset, offset + requiredSize)` are implicitly aliased with the new resource.

## Parameters

- `length`: The size of the buffer, in bytes.
- `options`: Options that describe the properties of the buffer. The buffer’s storage mode and CPU cache mode must match the heap’s   and   values.
- `offset`: The distance, in bytes, to place the buffer relative to the start of the heap.

## See Also

- [func makeBuffer(length: Int, options: MTLResourceOptions) -> (any MTLBuffer)?](mtlheap/makebuffer(length:options:).md)
  Creates a buffer on the heap.
- [func makeTexture(descriptor: MTLTextureDescriptor) -> (any MTLTexture)?](mtlheap/maketexture(descriptor:).md)
  Creates a texture on the heap.
- [func makeTexture(descriptor: MTLTextureDescriptor, offset: Int) -> (any MTLTexture)?](mtlheap/maketexture(descriptor:offset:).md)
  Creates a texture at a specified offset on the heap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheap/makebuffer(length:options:offset:))*