# makeTexture(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a texture on the heap.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func makeTexture(descriptor: MTLTextureDescriptor) -> (any MTLTexture)?
```

#### Return Value

A new texture object backed by heap memory, or `nil` if the heap memory is full.

#### Discussion

The heap’s type must be [`MTLHeapType.automatic`](mtlheaptype/automatic.md).

The texture’s CPU cache mode must match the heap’s [`cpuCacheMode`](mtlheap/cpucachemode.md) value. The texture’s storage mode must either match the heap’s [`storageMode`](mtlheap/storagemode.md) value or be a [`MTLStorageMode.memoryless`](mtlstoragemode/memoryless.md) value.

## Parameters

- `descriptor`: A descriptor object that describes the properties of the texture.

## See Also

- [func makeBuffer(length: Int, options: MTLResourceOptions) -> (any MTLBuffer)?](mtlheap/makebuffer(length:options:).md)
  Creates a buffer on the heap.
- [func makeBuffer(length: Int, options: MTLResourceOptions, offset: Int) -> (any MTLBuffer)?](mtlheap/makebuffer(length:options:offset:).md)
  Creates a buffer at a specified offset on the heap.
- [func makeTexture(descriptor: MTLTextureDescriptor, offset: Int) -> (any MTLTexture)?](mtlheap/maketexture(descriptor:offset:).md)
  Creates a texture at a specified offset on the heap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheap/maketexture(descriptor:))*