# updateTextureMappings(_:mode:regions:mipLevels:slices:numRegions:)

**Framework**: Metal  
**Kind**: method

Encodes a command to update memory mappings for multiple regions inside a texture.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
optional func updateTextureMappings(_ texture: any MTLTexture, mode: MTLSparseTextureMappingMode, regions: UnsafePointer<MTLRegion>, mipLevels: UnsafePointer<Int>, slices: UnsafePointer<Int>, numRegions: Int)
```

## Parameters

- `texture`: The sparse texture to update.
- `mode`: The change to make to the texture mapping.
- `regions`: A pointer to an array of regions to change. You need to provide as many regions as you specify in the   parameter.
- `mipLevels`: A pointer to an array of mipmap levels to change. You need to provide as many entries as you specify in the   parameter.
- `slices`: A pointer to an array of slices to change. You need to provide as many entries as you specify in the   parameter.
- `numRegions`: The number of regions to update.

## See Also

- [func updateTextureMapping(any MTLTexture, mode: MTLSparseTextureMappingMode, region: MTLRegion, mipLevel: Int, slice: Int)](mtlresourcestatecommandencoder/updatetexturemapping(_:mode:region:miplevel:slice:).md)
  Encodes a command to update the texture mappings for a region in a single texture mipmap.
- [enum MTLSparseTextureMappingMode](mtlsparsetexturemappingmode.md)
  Options for sparse texture mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresourcestatecommandencoder/updatetexturemappings(_:mode:regions:miplevels:slices:numregions:))*