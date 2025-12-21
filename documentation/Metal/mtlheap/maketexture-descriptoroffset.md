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

You can call the method with the following restrictions:

- The heap’s type needs to be [`MTLHeapType.placement`](mtlheaptype/placement.md)
- The texture’s CPU cache mode option needs to match the heap’s [`cpuCacheMode`](mtlheap/cpucachemode.md) property
- The texture’s storage mode option needs to be [`MTLStorageMode.memoryless`](mtlstoragemode/memoryless.md), or match the heap’s [`storageMode`](mtlheap/storagemode.md) property

> ❗ **Important**:  Avoid potentially erratic behavior by aligning the texture correctly so that it doesn’t extend past the end of the heap.

Use the [`heapBufferSizeAndAlign(length:options:)`](mtldevice/heapbuffersizeandalign(length:options:).md) to determine the correct size and alignment.

> **Note**:  The new texture can implicitly alias the underlying memory of other resources already in the heap within the overlapping half-open range of `[offset, offset + requiredSize)`.

## Parameters

- `descriptor`: A descriptor object that describes the properties of the texture.
- `offset`: The distance, in bytes, to place the texture relative to the start of the heap.

## See Also

- [func makeTexture(descriptor: MTLTextureDescriptor) -> (any MTLTexture)?](mtlheap/maketexture(descriptor:).md)
  Creates a texture on the heap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheap/maketexture(descriptor:offset:))*