# init(skybox:specular:diffuse:)

**Framework**: RealityKit  
**Kind**: init

Creates an EnvironmentResource a skybox, specular and diffuse texture resources.

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
convenience init(skybox skyboxTexture: TextureResource?, specular specularTexture: TextureResource, diffuse diffuseTexture: TextureResource) throws
```

#### Discussion

> **Note**: `SkyboxGenerator` and `ImageBasedLightTextureGenerator` can generate required textures into a `LowLevelTexture`, itself wrapped as a `TextureResource`.

> **Note**: The skybox is not needed for image based lighting with `VirtualEnvironmentProbeComponent` and `ImageBasedLightComponent`.

## Parameters

- `skyboxTexture`: A skybox texture to preserve. If nil, derives a low-resolution proxy from other inputs for lower memory usage.
- `specularTexture`: An image based light specular texture.
- `diffuseTexture`: An image based light diffuse texture.

## See Also

- [convenience init(named: String, in: Bundle?, skyboxMode: EnvironmentResource.SkyboxMode) async throws](environmentresource/init(named:in:skyboxmode:).md)
  Asynchronously loads an environment resource from a bundle.
- [EnvironmentResource.SkyboxMode](environmentresource/skyboxmode.md)
  An enumeration controlling how to preserve the skybox.
- [convenience init(equirectangular: CGImage, options: EnvironmentResource.CreateOptions) async throws](environmentresource/init(equirectangular:options:)-8e7wv.md)
  Asynchronously generates an environment resource from an equirectangular image.
- [convenience init(equirectangular: CGImage, options: EnvironmentResource.CreateOptions) throws](environmentresource/init(equirectangular:options:)-5bxl3.md)
  Synchronously creates an environment resource from an equirectangular image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/environmentresource/init(skybox:specular:diffuse:))*