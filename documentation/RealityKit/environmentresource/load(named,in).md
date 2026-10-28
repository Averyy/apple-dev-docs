# load(named:in:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

Synchronously loads an environment resource from a bundle.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.0+
- macOS 10.15+ - Deprecated in 27.2
- tvOS 26.0+ - Deprecated in 27.2
- visionOS - Deprecated in 27.2

> **Deprecated**: Use `init(named:in:skyboxMode:)` instead. Will be deprecated to support skybox-free EnvironmentResource.

## Declaration

```swift
@MainActor
@preconcurrency static func load(named name: String, in bundle: Bundle? = nil) throws -> EnvironmentResource
```

## Return Value

The environment resource that loads from the specified bundle.

## Discussion

Loading an [`EnvironmentResource`](../environmentresource.md) with this method blocks the main actor because it’s synchronous, so only call it from a command-line application. The method can stall a regular app, which makes it visibly hitch, and the system terminates an app if its UI becomes unresponsive.

If your image file is at the path `Foo.skybox/Bar.exr` in your Xcode project, use `Bar` for the name parameter.

To add an environment resource to your Xcode project, see [`EnvironmentResource`](../environmentresource.md).

> ❗ **Important**: This function blocks the calling thread while RealityKit loads the requested resource.

## Parameters

- `name`: The image name without the file extension.
- `bundle`: The bundle to search for the resource. Use `nil` to indicate the app’s bundle.

## See Also

### Loading the resource
- [convenience init(named: String, in: Bundle?) async throws](./init%28named,in%29.md)
  Asynchronously loads an environment resource from a bundle.
- [convenience init(equirectangular: CGImage, withName: String?) async throws](./init%28equirectangular,withname%29-8o2v7.md)
  Asynchronously generates an environment resource from an equirectangular image.
- [convenience init(equirectangular: CGImage, withName: String?) async throws](./init%28equirectangular,withname%29-8o2v7.md)
  Asynchronously generates an environment resource from an equirectangular image.
- [convenience init(cube: TextureResource, options: EnvironmentResource.CreateOptions) async throws](./init%28cube,options%29-9j9rn.md)
  Asynchronously creates an environment resource from a cube texture.
- [convenience init(cube: TextureResource, options: EnvironmentResource.CreateOptions) async throws](./init%28cube,options%29-9j9rn.md)
  Asynchronously creates an environment resource from a cube texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/environmentresource/load(named:in:))*