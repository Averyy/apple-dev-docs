# MTL4CopySparseBufferMappingOperation

**Framework**: Metal  
**Kind**: struct

Groups together arguments for an operation to copy a sparse buffer mapping.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct MTL4CopySparseBufferMappingOperation
```

## Topics

### Initializers
- [init()](mtl4copysparsebuffermappingoperation/init.md)
- [init(sourceRange: NSRange, destinationOffset: Int)](mtl4copysparsebuffermappingoperation/init(sourcerange:destinationoffset:).md)
### Instance Properties
- [var destinationOffset: Int](mtl4copysparsebuffermappingoperation/destinationoffset.md)
  The origin in the destination buffer, in tiles.
- [var sourceRange: NSRange](mtl4copysparsebuffermappingoperation/sourcerange.md)
  The range in the source buffer, in tiles.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum MTLBufferSparseTier](mtlbuffersparsetier.md)
  Enumerates the different support levels for sparse buffers.
- [struct MTL4UpdateSparseBufferMappingOperation](mtl4updatesparsebuffermappingoperation.md)
  Groups together arguments for an operation to update a sparse buffer mapping.
- [enum MTLTextureSparseTier](mtltexturesparsetier.md)
  Enumerates the different support levels for sparse textures.
- [struct MTL4CopySparseTextureMappingOperation](mtl4copysparsetexturemappingoperation.md)
  Groups together arguments for an operation to copy a sparse texture mapping.
- [struct MTL4UpdateSparseTextureMappingOperation](mtl4updatesparsetexturemappingoperation.md)
  Groups together arguments for an operation to update a sparse texture mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4copysparsebuffermappingoperation)*