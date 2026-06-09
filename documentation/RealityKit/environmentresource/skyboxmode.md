# EnvironmentResource.SkyboxMode

**Framework**: RealityKit  
**Kind**: struct

An enumeration controlling how to preserve the skybox.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct SkyboxMode
```

## Topics

### Choosing a skybox mode
- [static var preserve: EnvironmentResource.SkyboxMode](environmentresource/skyboxmode/preserve.md)
  Preserve and reference the original skybox cube texture.
- [static var discard: EnvironmentResource.SkyboxMode](environmentresource/skyboxmode/discard.md)
  Only keep a low-resolution proxy of the skybox, reducing memory usage.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [convenience init(named: String, in: Bundle?, skyboxMode: EnvironmentResource.SkyboxMode) async throws](environmentresource/init(named:in:skyboxmode:).md)
  Asynchronously loads an environment resource from a bundle.
- [convenience init(equirectangular: CGImage, options: EnvironmentResource.CreateOptions) async throws](environmentresource/init(equirectangular:options:)-8e7wv.md)
  Asynchronously generates an environment resource from an equirectangular image.
- [convenience init(equirectangular: CGImage, options: EnvironmentResource.CreateOptions) throws](environmentresource/init(equirectangular:options:)-5bxl3.md)
  Synchronously creates an environment resource from an equirectangular image.
- [convenience init(skybox: TextureResource?, specular: TextureResource, diffuse: TextureResource) throws](environmentresource/init(skybox:specular:diffuse:).md)
  Creates an EnvironmentResource a skybox, specular and diffuse texture resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/environmentresource/skyboxmode)*