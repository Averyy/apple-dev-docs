# MTLSparseTextureMappingMode

**Framework**: Metal  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum MTLSparseTextureMappingMode : NSUInteger;
```

## Topics

### Specifying the mapping mode
- [MTLSparseTextureMappingMode.map](./mtlsparsetexturemappingmode/map.md)
  A request to map sparse tiles from the heap to a region in the texture.
- [MTLSparseTextureMappingMode.unmap](./mtlsparsetexturemappingmode/unmap.md)
  A request to remove any mappings for a region in the texture.
### Initializers
- [init?(rawValue: UInt)](./mtlsparsetexturemappingmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Updating texture memory assignments
- [func updateTextureMapping(any MTLTexture, mode: MTLSparseTextureMappingMode, region: MTLRegion, mipLevel: Int, slice: Int)](./mtlresourcestatecommandencoder/updatetexturemapping%28_,mode,region,miplevel,slice%29.md)
  Encodes a command to update the texture mappings for a region in a single texture mipmap.
- [func updateTextureMappings(any MTLTexture, mode: MTLSparseTextureMappingMode, regions: UnsafePointer<MTLRegion>, mipLevels: UnsafePointer<Int>, slices: UnsafePointer<Int>, numRegions: Int)](./mtlresourcestatecommandencoder/updatetexturemappings%28_,mode,regions,miplevels,slices,numregions%29.md)
  Encodes a command to update memory mappings for multiple regions inside a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsparsetexturemappingmode)*