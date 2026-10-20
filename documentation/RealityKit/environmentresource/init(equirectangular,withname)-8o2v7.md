# init(equirectangular:withName:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Asynchronously generates an environment resource from an equirectangular image.

**Availability**:
- iOS 18.0+ - Deprecated in 27.2
- iPadOS 18.0+ - Deprecated in 27.2
- Mac Catalyst 18.0+
- macOS 15.0+ - Deprecated in 27.2
- tvOS 26.0+ - Deprecated in 27.2
- visionOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use `init(equirectangular:options:)` instead. Will be deprecated to support skybox-free EnvironmentResource.

## Declaration

```swift
@MainActor
@preconcurrency convenience init(equirectangular cgImage: CGImage, withName resourceName: String? = nil) async throws
```

**Other overloads**:

```swift
@MainActor
@preconcurrency convenience init(equirectangular cgImage: CGImage, withName resourceName: String? = nil) throws
```

## Parameters

- `cgImage`: The source equirectangular (latitude, longitude) image. To preserve all details use an image where the width is half the height.
- `resourceName`: A unique name the method assigns to the resource it loads, for use in network synchronization.

## See Also

### Loading the resource
- [convenience init(named: String, in: Bundle?) async throws](./init%28named,in%29.md)
  Asynchronously loads an environment resource from a bundle.
- [convenience init(cube: TextureResource, options: EnvironmentResource.CreateOptions) async throws](./init%28cube,options%29-9j9rn.md)
  Asynchronously creates an environment resource from a cube texture.
- [convenience init(cube: TextureResource, options: EnvironmentResource.CreateOptions) async throws](./init%28cube,options%29-9j9rn.md)
  Asynchronously creates an environment resource from a cube texture.
- [static func load(named: String, in: Bundle?) throws -> EnvironmentResource](./load%28named,in%29.md)
  Synchronously loads an environment resource from a bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/environmentresource/init(equirectangular:withname:)-8o2v7)*