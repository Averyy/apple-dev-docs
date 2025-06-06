# updateTextureMapping(_:mode:region:mipLevel:slice:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command to update the texture mappings for a region in a single texture mipmap.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
optional func updateTextureMapping(_ texture: any MTLTexture, mode: MTLSparseTextureMappingMode, region: MTLRegion, mipLevel: Int, slice: Int)
```

#### Discussion

When the GPU executes the command that updates the texture’s memory mapping, the GPU gets details about the region from the `region` parameter.

To allocate tiles from the heap, pass [`MTLSparseTextureMappingMode.map`](mtlsparsetexturemappingmode/map.md) as the `mode` parameter, and to free files back to the heap, pass [`MTLSparseTextureMappingMode.unmap`](mtlsparsetexturemappingmode/unmap.md).

If you encode other commands that use the texture’s contents, such as rendering to the texture or sampling from a texture, synchronize the texture’s mapping updates with those commands to avoid race conditions. See [`Resource Synchronization`](resource-synchronization.md).

If you encode commands with multiple resource state passes, synchronize the resources to run the commands in the passes sequentially. See the [`MTLResourceStateCommandEncoder`](mtlresourcestatecommandencoder.md) protocol.

## Parameters

- `texture`: The sparse texture to update.
- `mode`: A mode that indicates whether the method allocates or frees a memory tile in the texture.
- `region`: A region, in tile coordinates, that describes the part of the mipmap to update.
- `mipLevel`: The mipmap to update.
- `slice`: The slice in the texture to update.

## See Also

- [func updateTextureMappings(any MTLTexture, mode: MTLSparseTextureMappingMode, regions: UnsafePointer<MTLRegion>, mipLevels: UnsafePointer<Int>, slices: UnsafePointer<Int>, numRegions: Int)](mtlresourcestatecommandencoder/updatetexturemappings(_:mode:regions:miplevels:slices:numregions:).md)
  Encodes a command to update memory mappings for multiple regions inside a texture.
- [enum MTLSparseTextureMappingMode](mtlsparsetexturemappingmode.md)
  Options for sparse texture mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresourcestatecommandencoder/updatetexturemapping(_:mode:region:miplevel:slice:))*