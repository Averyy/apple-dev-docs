# MTLSparseTextureMappingMode

**Framework**: Metal  
**Kind**: enum

Options for sparse texture mapping.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum MTLSparseTextureMappingMode
```

## Topics

### Specifying the Mapping Mode
- [MTLSparseTextureMappingMode.map](mtlsparsetexturemappingmode/map.md)
  A request to map sparse tiles from the heap to a region in the texture.
- [MTLSparseTextureMappingMode.unmap](mtlsparsetexturemappingmode/unmap.md)
  A request to remove any mappings for a region in the texture.
### Initializers
- [init?(rawValue: UInt)](mtlsparsetexturemappingmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func updateTextureMapping(any MTLTexture, mode: MTLSparseTextureMappingMode, region: MTLRegion, mipLevel: Int, slice: Int)](mtlresourcestatecommandencoder/updatetexturemapping(_:mode:region:miplevel:slice:).md)
  Encodes a command to update the texture mappings for a region in a single texture mipmap.
- [func updateTextureMappings(any MTLTexture, mode: MTLSparseTextureMappingMode, regions: UnsafePointer<MTLRegion>, mipLevels: UnsafePointer<Int>, slices: UnsafePointer<Int>, numRegions: Int)](mtlresourcestatecommandencoder/updatetexturemappings(_:mode:regions:miplevels:slices:numregions:).md)
  Encodes a command to update memory mappings for multiple regions inside a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsparsetexturemappingmode)*