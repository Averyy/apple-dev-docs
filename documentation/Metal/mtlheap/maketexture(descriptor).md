# makeTexture(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (id<MTLTexture>) newTextureWithDescriptor:(MTLTextureDescriptor *) descriptor;
```

## Return Value

A new texture object backed by heap memory, or `nil` if the heap memory is full.

## Discussion

You can call the method with the following restrictions:

- The heap’s type needs to be [`MTLHeapType.automatic`](../mtlheaptype/automatic.md)
- The texture’s CPU cache mode option needs to match the heap’s [`cpuCacheMode`](./cpucachemode.md) property
- The texture’s storage mode option needs to be [`MTLStorageMode.memoryless`](../mtlstoragemode/memoryless.md), or match the heap’s [`storageMode`](./storagemode.md) property

## Parameters

- `descriptor`: A descriptor object that describes the properties of the texture.

## See Also

### Creating textures from a heap
- [func makeTexture(descriptor: MTLTextureDescriptor, offset: Int) -> (any MTLTexture)?](./maketexture%28descriptor,offset%29.md)
  Creates a texture at a specified offset on the heap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheap/maketexture(descriptor:))*