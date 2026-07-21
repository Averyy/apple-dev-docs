# init(perEntityData:)

**Framework**: RealityKit  
**Kind**: init

Initializes the resource with the given entity descriptors, but does not specify any atlas textures. Skips validation of atlas texture indices and slices within bake descriptors. This is helpful for providing a SurfaceExtractor with information about how entities are laid out in the lightmap without needing to provide any texture data along with it.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
convenience init(perEntityData: [LightmapResource.EntityLightmapDescriptor]) throws
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lightmapresource/init(perentitydata:))*