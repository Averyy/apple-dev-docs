# init(named:in:skyboxMode:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Asynchronously loads an environment resource from a bundle.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(named name: String, in bundle: Bundle? = nil, skyboxMode: EnvironmentResource.SkyboxMode) async throws
```

## Parameters

- `skyboxMode`: Skybox’s preservation in the environment resource.

## See Also

### Creating an environment resource
- [EnvironmentResource.SkyboxMode](./skyboxmode.md)
  An enumeration controlling how to preserve the skybox.
- [convenience init(equirectangular: CGImage, options: EnvironmentResource.CreateOptions) async throws](./init%28equirectangular,options%29-8e7wv.md)
  Asynchronously generates an environment resource from an equirectangular image.
- [convenience init(equirectangular: CGImage, options: EnvironmentResource.CreateOptions) throws](./init%28equirectangular,options%29-5bxl3.md)
  Synchronously creates an environment resource from an equirectangular image.
- [convenience init(skybox: TextureResource?, specular: TextureResource, diffuse: TextureResource) throws](./init%28skybox,specular,diffuse%29.md)
  Creates an EnvironmentResource a skybox, specular and diffuse texture resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/environmentresource/init(named:in:skyboxmode:))*