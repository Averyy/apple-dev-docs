# MTL4CopySparseTextureMappingOperation

**Framework**: Metal  
**Kind**: struct

Groups together arguments for an operation to copy a sparse texture mapping.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
struct MTL4CopySparseTextureMappingOperation
```

## Topics

### Initializers
- [init()](mtl4copysparsetexturemappingoperation/init.md)
- [init(sourceRegion: MTLRegion, sourceLevel: Int, sourceSlice: Int, destinationOrigin: MTLOrigin, destinationLevel: Int, destinationSlice: Int)](mtl4copysparsetexturemappingoperation/init(sourceregion:sourcelevel:sourceslice:destinationorigin:destinationlevel:destinationslice:).md)
### Instance Properties
- [var destinationLevel: Int](mtl4copysparsetexturemappingoperation/destinationlevel.md)
  The index of the mipmap level in the destination texture.
- [var destinationOrigin: MTLOrigin](mtl4copysparsetexturemappingoperation/destinationorigin.md)
  The origin in the destination texture to copy into, in tiles.
- [var destinationSlice: Int](mtl4copysparsetexturemappingoperation/destinationslice.md)
  The index of the array slice in the destination texture to copy into.
- [var sourceLevel: Int](mtl4copysparsetexturemappingoperation/sourcelevel.md)
  The index of the mipmap level in the source texture.
- [var sourceRegion: MTLRegion](mtl4copysparsetexturemappingoperation/sourceregion.md)
  The region in the source texture, in tiles.
- [var sourceSlice: Int](mtl4copysparsetexturemappingoperation/sourceslice.md)
  The index of the array slice in the texture source of the copy operation.

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
- [struct MTL4UpdateSparseTextureMappingOperation](mtl4updatesparsetexturemappingoperation.md)
  Groups together arguments for an operation to update a sparse texture mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4copysparsetexturemappingoperation)*