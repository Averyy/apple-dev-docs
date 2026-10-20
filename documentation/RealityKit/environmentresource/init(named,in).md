# init(named:in:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Asynchronously loads an environment resource from a bundle.

**Availability**:
- iOS 18.0+ - Deprecated in 27.2
- iPadOS 18.0+ - Deprecated in 27.2
- Mac Catalyst 18.0+
- macOS 15.0+ - Deprecated in 27.2
- tvOS 26.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use `init(named:in:skyboxMode:)` instead. Will be deprecated to support skybox-free EnvironmentResource.

## Declaration

```swift
@MainActor
@preconcurrency convenience init(named name: String, in bundle: Bundle? = nil) async throws
```

## See Also

### Loading the resource
- [convenience init(equirectangular: CGImage, withName: String?) async throws](./init%28equirectangular,withname%29-8o2v7.md)
  Asynchronously generates an environment resource from an equirectangular image.
- [convenience init(equirectangular: CGImage, withName: String?) async throws](./init%28equirectangular,withname%29-8o2v7.md)
  Asynchronously generates an environment resource from an equirectangular image.
- [convenience init(cube: TextureResource, options: EnvironmentResource.CreateOptions) async throws](./init%28cube,options%29-9j9rn.md)
  Asynchronously creates an environment resource from a cube texture.
- [convenience init(cube: TextureResource, options: EnvironmentResource.CreateOptions) async throws](./init%28cube,options%29-9j9rn.md)
  Asynchronously creates an environment resource from a cube texture.
- [static func load(named: String, in: Bundle?) throws -> EnvironmentResource](./load%28named,in%29.md)
  Synchronously loads an environment resource from a bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/environmentresource/init(named:in:))*