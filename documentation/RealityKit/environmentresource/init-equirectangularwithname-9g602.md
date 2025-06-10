# init(equirectangular:withName:)

**Framework**: RealityKit  
**Kind**: init

Synchronously creates an environment resource from an equirectangular image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(equirectangular cgImage: CGImage, withName resourceName: String? = nil) throws
```

#### Discussion

Loading an [`EnvironmentResource`](environmentresource.md) with this method blocks the main actor because it’s synchronous, so only call it from a command-line application. The method can stall a regular app, which makes it visibly hitch, and the system terminates an app if its UI becomes unresponsive.

## Parameters

- `cgImage`: The source equirectangular (latitude, longitude) image. To preserve all details use an image where the width is half the height.
- `resourceName`: A unique name the method assigns to the resource it loads,   for use in network synchronization.

## See Also

- [convenience(named:in:)](environmentresource/init(named:in:).md)
  Asynchronously loads an environment resource from a bundle.
- [convenience init(equirectangular: CGImage, withName: String?) async throws](environmentresource/init(equirectangular:withname:)-3xxrz.md)
  Asynchronously generates an environment resource from an equirectangular image.
- [convenience init(cube: TextureResource, options: EnvironmentResource.CreateOptions) async throws](environmentresource/init(cube:options:)-4xqiz.md)
  Asynchronously creates an environment resource from a cube texture.
- [convenience init(cube: TextureResource, options: EnvironmentResource.CreateOptions) throws](environmentresource/init(cube:options:)-4knhi.md)
  Synchronously generates an environment resource from a cube texture resource.
- [static func load(named: String, in: Bundle?) throws -> EnvironmentResource](environmentresource/load(named:in:).md)
  Synchronously loads an environment resource from a bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/environmentresource/init(equirectangular:withname:)-9g602)*