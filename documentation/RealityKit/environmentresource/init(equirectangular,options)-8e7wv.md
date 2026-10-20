# init(equirectangular:options:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Asynchronously generates an environment resource from an equirectangular image.

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
convenience init(equirectangular cgImage: CGImage, options: EnvironmentResource.CreateOptions) async throws
```

**Other overloads**:

```swift
@MainActor
convenience init(equirectangular cgImage: CGImage, options: EnvironmentResource.CreateOptions) throws
```

## Parameters

- `cgImage`: The source equirectangular (latitude, longitude) image. To preserve all details use an image where the width is half the height.

## See Also

### Creating an environment resource
- [convenience init(named: String, in: Bundle?, skyboxMode: EnvironmentResource.SkyboxMode) async throws](./init%28named,in,skyboxmode%29.md)
  Asynchronously loads an environment resource from a bundle.
- [EnvironmentResource.SkyboxMode](./skyboxmode.md)
  An enumeration controlling how to preserve the skybox.
- [convenience init(equirectangular: CGImage, options: EnvironmentResource.CreateOptions) throws](./init%28equirectangular,options%29-5bxl3.md)
  Synchronously creates an environment resource from an equirectangular image.
- [convenience init(skybox: TextureResource?, specular: TextureResource, diffuse: TextureResource) throws](./init%28skybox,specular,diffuse%29.md)
  Creates an EnvironmentResource a skybox, specular and diffuse texture resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/environmentresource/init(equirectangular:options:)-8e7wv)*