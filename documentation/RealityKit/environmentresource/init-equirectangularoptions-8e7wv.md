# init(equirectangular:options:)

**Framework**: RealityKit  
**Kind**: init

Asynchronously generates an environment resource from an equirectangular image.

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
convenience init(equirectangular cgImage: CGImage, options: EnvironmentResource.CreateOptions) async throws
```

## Parameters

- `cgImage`: The source equirectangular (latitude, longitude) image. To preserve all details use an image where the width is half the height.

## See Also

- [convenience init(named: String, in: Bundle?, skyboxMode: EnvironmentResource.SkyboxMode) async throws](environmentresource/init(named:in:skyboxmode:).md)
  Asynchronously loads an environment resource from a bundle.
- [EnvironmentResource.SkyboxMode](environmentresource/skyboxmode.md)
  An enumeration controlling how to preserve the skybox.
- [convenience init(equirectangular: CGImage, options: EnvironmentResource.CreateOptions) throws](environmentresource/init(equirectangular:options:)-5bxl3.md)
  Synchronously creates an environment resource from an equirectangular image.
- [convenience init(skybox: TextureResource?, specular: TextureResource, diffuse: TextureResource) throws](environmentresource/init(skybox:specular:diffuse:).md)
  Creates an EnvironmentResource a skybox, specular and diffuse texture resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/environmentresource/init(equirectangular:options:)-8e7wv)*