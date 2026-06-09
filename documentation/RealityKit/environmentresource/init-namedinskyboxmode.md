# init(named:in:skyboxMode:)

**Framework**: RealityKit  
**Kind**: init

Asynchronously loads an environment resource from a bundle.

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
@preconcurrency convenience init(named name: String, in bundle: Bundle? = nil, skyboxMode: EnvironmentResource.SkyboxMode) async throws
```

## Parameters

- `skyboxMode`: Skybox’s preservation in the environment resource.

## See Also

- [EnvironmentResource.SkyboxMode](environmentresource/skyboxmode.md)
  An enumeration controlling how to preserve the skybox.
- [convenience init(equirectangular: CGImage, options: EnvironmentResource.CreateOptions) async throws](environmentresource/init(equirectangular:options:)-8e7wv.md)
  Asynchronously generates an environment resource from an equirectangular image.
- [convenience init(equirectangular: CGImage, options: EnvironmentResource.CreateOptions) throws](environmentresource/init(equirectangular:options:)-5bxl3.md)
  Synchronously creates an environment resource from an equirectangular image.
- [convenience init(skybox: TextureResource?, specular: TextureResource, diffuse: TextureResource) throws](environmentresource/init(skybox:specular:diffuse:).md)
  Creates an EnvironmentResource a skybox, specular and diffuse texture resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/environmentresource/init(named:in:skyboxmode:))*