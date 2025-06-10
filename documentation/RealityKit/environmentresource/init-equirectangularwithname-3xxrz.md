# init(equirectangular:withName:)

**Framework**: RealityKit  
**Kind**: init

Asynchronously generates an environment resource from an equirectangular image.

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
@preconcurrency convenience init(equirectangular cgImage: CGImage, withName resourceName: String? = nil) async throws
```

## Parameters

- `cgImage`: The source equirectangular (latitude, longitude) image. To preserve all details use an image where the width is half the height.
- `resourceName`: A unique name the method assigns to the resource it loads,   for use in network synchronization.

## See Also

- [convenience(named:in:)](environmentresource/init(named:in:).md)
  Asynchronously loads an environment resource from a bundle.
- [convenience init(equirectangular: CGImage, withName: String?) throws](environmentresource/init(equirectangular:withname:)-9g602.md)
  Synchronously creates an environment resource from an equirectangular image.
- [convenience init(cube: TextureResource, options: EnvironmentResource.CreateOptions) async throws](environmentresource/init(cube:options:)-4xqiz.md)
  Asynchronously creates an environment resource from a cube texture.
- [convenience init(cube: TextureResource, options: EnvironmentResource.CreateOptions) throws](environmentresource/init(cube:options:)-4knhi.md)
  Synchronously generates an environment resource from a cube texture resource.
- [static func load(named: String, in: Bundle?) throws -> EnvironmentResource](environmentresource/load(named:in:).md)
  Synchronously loads an environment resource from a bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/environmentresource/init(equirectangular:withname:)-3xxrz)*