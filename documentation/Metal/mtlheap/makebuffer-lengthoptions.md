# makeBuffer(length:options:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a buffer on the heap.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func makeBuffer(length: Int, options: MTLResourceOptions = []) -> (any MTLBuffer)?
```

#### Return Value

A new buffer object backed by heap memory, or `nil` if the heap memory is full.

#### Discussion

The heap’s type must be [`MTLHeapType.automatic`](mtlheaptype/automatic.md).

The buffer’s storage mode and CPU cache mode must match the heap’s [`storageMode`](mtlheap/storagemode.md) and [`cpuCacheMode`](mtlheap/cpucachemode.md) values.

## Parameters

- `length`: The size, in bytes, of the buffer.
- `options`: Options that describe the properties of the buffer.

## See Also

- [func makeTexture(descriptor: MTLTextureDescriptor) -> (any MTLTexture)?](mtlheap/maketexture(descriptor:).md)
  Creates a texture on the heap.
- [func makeBuffer(length: Int, options: MTLResourceOptions, offset: Int) -> (any MTLBuffer)?](mtlheap/makebuffer(length:options:offset:).md)
  Creates a buffer at a specified offset on the heap.
- [func makeTexture(descriptor: MTLTextureDescriptor, offset: Int) -> (any MTLTexture)?](mtlheap/maketexture(descriptor:offset:).md)
  Creates a texture at a specified offset on the heap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheap/makebuffer(length:options:))*