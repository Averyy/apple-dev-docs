# EnvironmentResource.SkyboxMode

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An enumeration controlling how to preserve the skybox.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct SkyboxMode
```

## Topics

### Choosing a skybox mode
- [static var preserve: EnvironmentResource.SkyboxMode](./skyboxmode/preserve.md)
  Preserve and reference the original skybox cube texture.
- [static var discard: EnvironmentResource.SkyboxMode](./skyboxmode/discard.md)
  Only keep a low-resolution proxy of the skybox, reducing memory usage.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating an environment resource
- [convenience init(named: String, in: Bundle?, skyboxMode: EnvironmentResource.SkyboxMode) async throws](./init%28named,in,skyboxmode%29.md)
  Asynchronously loads an environment resource from a bundle.
- [convenience init(equirectangular: CGImage, options: EnvironmentResource.CreateOptions) async throws](./init%28equirectangular,options%29-8e7wv.md)
  Asynchronously generates an environment resource from an equirectangular image.
- [convenience init(equirectangular: CGImage, options: EnvironmentResource.CreateOptions) throws](./init%28equirectangular,options%29-5bxl3.md)
  Synchronously creates an environment resource from an equirectangular image.
- [convenience init(skybox: TextureResource?, specular: TextureResource, diffuse: TextureResource) throws](./init%28skybox,specular,diffuse%29.md)
  Creates an EnvironmentResource a skybox, specular and diffuse texture resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/environmentresource/skyboxmode)*