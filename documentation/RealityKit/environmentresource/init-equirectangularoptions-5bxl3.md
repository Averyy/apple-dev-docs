# init(equirectangular:options:)

**Framework**: RealityKit  
**Kind**: init

Synchronously creates an environment resource from an equirectangular image.

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
convenience init(equirectangular cgImage: CGImage, options: EnvironmentResource.CreateOptions) throws
```

#### Discussion

Loading an [`EnvironmentResource`](environmentresource.md) with this method blocks the main actor because it’s synchronous, so only call it from a command-line application. The method can stall a regular app, which makes it visibly hitch, and the system terminates an app if its UI becomes unresponsive.

## Parameters

- `cgImage`: The source equirectangular (latitude, longitude) image. To preserve all details use an image where the width is half the height.

## See Also

- [convenience init(named: String, in: Bundle?, skyboxMode: EnvironmentResource.SkyboxMode) async throws](environmentresource/init(named:in:skyboxmode:).md)
  Asynchronously loads an environment resource from a bundle.
- [EnvironmentResource.SkyboxMode](environmentresource/skyboxmode.md)
  An enumeration controlling how to preserve the skybox.
- [convenience init(equirectangular: CGImage, options: EnvironmentResource.CreateOptions) async throws](environmentresource/init(equirectangular:options:)-8e7wv.md)
  Asynchronously generates an environment resource from an equirectangular image.
- [convenience init(skybox: TextureResource?, specular: TextureResource, diffuse: TextureResource) throws](environmentresource/init(skybox:specular:diffuse:).md)
  Creates an EnvironmentResource a skybox, specular and diffuse texture resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/environmentresource/init(equirectangular:options:)-5bxl3)*