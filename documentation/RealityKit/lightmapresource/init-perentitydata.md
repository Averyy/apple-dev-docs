# init(perEntityData:)

**Framework**: RealityKit  
**Kind**: init

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
convenience init(perEntityData: [LightmapResource.EntityLightmapDescriptor]) throws
```

## See Also

- [convenience init(atlasTextures: [TextureResource], perEntityData: [LightmapResource.EntityLightmapDescriptor]) throws](lightmapresource/init(atlastextures:perentitydata:).md)
  Initializes the resource with the given atlases and entity descriptors. The resources within `atlasTextures` must be 2D texture arrays. Textures containing data for ambient occlusion should be single-channel textures. Textures containing data for beauty bakes should contain RGBA color. Textures for diffuse irradiance should contain RGBA data. There should be 3 slices per atlas page. Each of the 3 slices contains data red, green and blue channels of irradiance respectively. Each texel within a slice contains coefficients for spherical harmonic functions of 0th and 1st degree, with the R channel providing the coefficient for 0th degree spherical harmonic, and G, B and A channels providing coefficients for the 1st degree spherical harmonics (with orders -1, 0 and 1 respectively).
- [LightmapResource.EntityLightmapDescriptor](lightmapresource/entitylightmapdescriptor.md)
  Specifies a MeshPartLightmapDescriptor for each part of the entity’s model.
- [LightmapResource.MeshPartLightmapDescriptor](lightmapresource/meshpartlightmapdescriptor.md)
  Specifies bake descriptors for each instance of the given mesh part.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lightmapresource/init(perentitydata:))*