# EnvironmentResource

**Framework**: RealityKit  
**Kind**: class

An environmental resource that contains background and lighting information for a scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency class EnvironmentResource
```

#### Overview

RealityKit supports image-based lighting that enables realistic reflections on your scene’s 3D content. You can define the look of your scene’s background by supplying an environment resource image that determines the general color of the room, and the location of any spotlights or shadowed areas within the reflection. RealityKit applies the image’s characteristics to your scene’s reflective content.

![Two screenshots depicting the process of applying an environment resource image to a reflective surface in a RealityKit scene. The first screenshot defines the](https://docs-assets.developer.apple.com/published/1b295efdb644c044538354288c31d568/EnvironmentResource~dark%402x.png)

RealityKit checks a bundle for an environment resource by the filename you supply to one of the load functions.

##### Create a Skybox Folder

To add an environment resource to your Xcode project, make a folder with a name that ends in `.skybox` and place a single image inside. Ensure that the image is an environment map of equirectangular projection, also known as a . Drag the folder into the Project navigator. In the options pane, choose to create a folder reference (not a group), and add the folder to your app’s targets. At build time, Xcode compiles the image for use as an environment resource and inserts the result into the app bundle.

RealityKit supports the same input formats as Image I/O, such as `.png` and `.jpg` However, to achieve rich, vibrant lighting, use a `.exr` or `.hdr` format, which support a wide dynamic range.

## Topics

### Loading the resource
- [convenience init(named: String, in: Bundle?) async throws](environmentresource/init(named:in:).md)
  Asynchronously loads an environment resource from a bundle.
- [convenience init(equirectangular: CGImage, withName: String?) throws](environmentresource/init(equirectangular:withname:)-9g602.md)
  Synchronously creates an environment resource from an equirectangular image.
- [convenience init(equirectangular: CGImage, withName: String?) async throws](environmentresource/init(equirectangular:withname:)-3xxrz.md)
  Asynchronously generates an environment resource from an equirectangular image.
- [convenience init(cube: TextureResource, options: EnvironmentResource.CreateOptions) async throws](environmentresource/init(cube:options:)-4xqiz.md)
  Asynchronously creates an environment resource from a cube texture.
- [convenience init(cube: TextureResource, options: EnvironmentResource.CreateOptions) throws](environmentresource/init(cube:options:)-4knhi.md)
  Synchronously generates an environment resource from a cube texture resource.
- [static func load(named: String, in: Bundle?) throws -> EnvironmentResource](environmentresource/load(named:in:).md)
  Synchronously loads an environment resource from a bundle.
### Configuring the resource creation
- [EnvironmentResource.CreateOptions](environmentresource/createoptions.md)
  A type that controls compression, sampling quality, and cubemap dimensions when creating an environment resource.
- [EnvironmentResource.Compression](environmentresource/compression.md)
  The compression to apply when creating an environment resource.
### Accessing resource data
- [var skybox: TextureResource](environmentresource/skybox.md)
  The cube color texture that contains environment surrounding details.
### Deprecated
- [static func generate(fromEquirectangular: CGImage, withName: String?) throws -> EnvironmentResource](environmentresource/generate(fromequirectangular:withname:)-3wtpe.md)
  Synchronously generates an environment resource from an equirectangular image.
- [static func generate(fromEquirectangular: CGImage, withName: String?) async throws -> EnvironmentResource](environmentresource/generate(fromequirectangular:withname:)-6mxsi.md)
  Asynchronously generates an environment resource from an equirectangular image.
- [static func loadAsync(named: String, in: Bundle?) -> LoadRequest<EnvironmentResource>](environmentresource/loadasync(named:in:).md)
  Asynchronously loads an environment resource from a bundle.

## Relationships

### Conforms To
- [Resource](resource.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct EnvironmentLightingConfigurationComponent](environmentlightingconfigurationcomponent.md)
  A component that scales the amount of light that an entity receives from its environment.
- [struct VirtualEnvironmentProbeComponent](virtualenvironmentprobecomponent.md)
  A component that provides environment lighting for entities you place within the same virtual world.
- [VirtualEnvironmentProbeComponent.Probe](virtualenvironmentprobecomponent/probe.md)
  A sample of the environment around a point in a scene the system uses for environment-based lighting.
- [VirtualEnvironmentProbeComponent.Source](virtualenvironmentprobecomponent/source-swift.enum.md)
  Options that define the source of diffuse and specular lighting for environment lighting calculations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/environmentresource)*