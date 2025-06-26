# MTL4UpdateSparseTextureMappingOperation

**Framework**: Metal  
**Kind**: struct

Groups together arguments for an operation to update a sparse texture mapping.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
struct MTL4UpdateSparseTextureMappingOperation
```

#### Overview

When performing a sparse mapping update, you are responsible for issuing a barrier against stage `MTLStageResourceState`.

You can determine the sparse texture tier by calling `MTLTexture/sparseTextureTier`.

## Topics

### Initializers
- [init()](mtl4updatesparsetexturemappingoperation/init.md)
- [init(mode: MTLSparseTextureMappingMode, textureRegion: MTLRegion, textureLevel: Int, textureSlice: Int, heapOffset: Int)](mtl4updatesparsetexturemappingoperation/init(mode:textureregion:texturelevel:textureslice:heapoffset:).md)
### Instance Properties
- [var heapOffset: Int](mtl4updatesparsetexturemappingoperation/heapoffset.md)
  The starting offset in the heap, in tiles.
- [var mode: MTLSparseTextureMappingMode](mtl4updatesparsetexturemappingoperation/mode.md)
  The mode of the mapping operation to perform.
- [var textureLevel: Int](mtl4updatesparsetexturemappingoperation/texturelevel.md)
  The index of the mipmap level in the texture to update.
- [var textureRegion: MTLRegion](mtl4updatesparsetexturemappingoperation/textureregion.md)
  The region in the texture to update, in tiles.
- [var textureSlice: Int](mtl4updatesparsetexturemappingoperation/textureslice.md)
  The index of the array slice in the texture to update.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum MTLBufferSparseTier](mtlbuffersparsetier.md)
  Enumerates the different support levels for sparse buffers.
- [struct MTL4CopySparseBufferMappingOperation](mtl4copysparsebuffermappingoperation.md)
  Groups together arguments for an operation to copy a sparse buffer mapping.
- [struct MTL4UpdateSparseBufferMappingOperation](mtl4updatesparsebuffermappingoperation.md)
  Groups together arguments for an operation to update a sparse buffer mapping.
- [enum MTLTextureSparseTier](mtltexturesparsetier.md)
  Enumerates the different support levels for sparse textures.
- [struct MTL4CopySparseTextureMappingOperation](mtl4copysparsetexturemappingoperation.md)
  Groups together arguments for an operation to copy a sparse texture mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4updatesparsetexturemappingoperation)*