# MTL4UpdateSparseBufferMappingOperation

**Framework**: Metal  
**Kind**: struct

Groups together arguments for an operation to update a sparse buffer mapping.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
struct MTL4UpdateSparseBufferMappingOperation
```

## Topics

### Initializers
- [init()](mtl4updatesparsebuffermappingoperation/init.md)
- [init(mode: MTLSparseTextureMappingMode, bufferRange: NSRange, heapOffset: Int)](mtl4updatesparsebuffermappingoperation/init(mode:bufferrange:heapoffset:).md)
### Instance Properties
- [var bufferRange: NSRange](mtl4updatesparsebuffermappingoperation/bufferrange.md)
  The range in the buffer, in tiles.
- [var heapOffset: Int](mtl4updatesparsebuffermappingoperation/heapoffset.md)
  The starting offset in the heap, in tiles.
- [var mode: MTLSparseTextureMappingMode](mtl4updatesparsebuffermappingoperation/mode.md)
  The mode of the mapping operation to perform.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum MTLBufferSparseTier](mtlbuffersparsetier.md)
  Enumerates the different support levels for sparse buffers.
- [struct MTL4CopySparseBufferMappingOperation](mtl4copysparsebuffermappingoperation.md)
  Groups together arguments for an operation to copy a sparse buffer mapping.
- [enum MTLTextureSparseTier](mtltexturesparsetier.md)
  Enumerates the different support levels for sparse textures.
- [struct MTL4CopySparseTextureMappingOperation](mtl4copysparsetexturemappingoperation.md)
  Groups together arguments for an operation to copy a sparse texture mapping.
- [struct MTL4UpdateSparseTextureMappingOperation](mtl4updatesparsetexturemappingoperation.md)
  Groups together arguments for an operation to update a sparse texture mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4updatesparsebuffermappingoperation)*