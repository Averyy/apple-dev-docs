# init(atlasTextures:perEntityData:)

**Framework**: RealityKit  
**Kind**: init

Initializes the resource with the given atlases and entity descriptors. The resources within `atlasTextures` must be 2D texture arrays. Textures containing data for ambient occlusion should be single-channel textures. Textures containing data for beauty bakes should contain RGBA color. Textures for diffuse irradiance should contain RGBA data. There should be 3 slices per atlas page. Assuming a = sqrt(2), b = sqrt(3), c = sqrt(6), and N0 = (1/c, 1/a, 1/b), N1=(-1/c, -1/a, 1/b), N2 = (a/b, 0, 1/b), the first, second and third slices should contain lighting as if the surface normal was respectively N0, N1 and N2 in tangent space.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
convenience init(atlasTextures: [TextureResource], perEntityData: [LightmapResource.EntityLightmapDescriptor]) throws
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lightmapresource/init(atlastextures:perentitydata:))*