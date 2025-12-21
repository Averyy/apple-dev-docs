# MTLBufferSparseTier

**Framework**: Metal  
**Kind**: enum

Enumerates the different support levels for sparse buffers.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum MTLBufferSparseTier
```

## Topics

### Enumeration Cases
- [MTLBufferSparseTier.tier1](mtlbuffersparsetier/tier1.md)
  Indicates support for sparse buffers tier 1.
- [MTLBufferSparseTier.tierNone](mtlbuffersparsetier/tiernone.md)
  Indicates that the buffer is not sparse.
### Initializers
- [init?(rawValue: Int)](mtlbuffersparsetier/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct MTL4CopySparseBufferMappingOperation](mtl4copysparsebuffermappingoperation.md)
  Groups together arguments for an operation to copy a sparse buffer mapping.
- [struct MTL4UpdateSparseBufferMappingOperation](mtl4updatesparsebuffermappingoperation.md)
  Groups together arguments for an operation to update a sparse buffer mapping.
- [enum MTLTextureSparseTier](mtltexturesparsetier.md)
  Enumerates the different support levels for sparse textures.
- [struct MTL4CopySparseTextureMappingOperation](mtl4copysparsetexturemappingoperation.md)
  Groups together arguments for an operation to copy a sparse texture mapping.
- [struct MTL4UpdateSparseTextureMappingOperation](mtl4updatesparsetexturemappingoperation.md)
  Groups together arguments for an operation to update a sparse texture mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlbuffersparsetier)*