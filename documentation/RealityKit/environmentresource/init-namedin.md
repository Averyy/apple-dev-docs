# init(named:in:)

**Framework**: RealityKit  
**Kind**: init

Asynchronously loads an environment resource from a bundle.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(named name: String, in bundle: Bundle? = nil) async throws
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/environmentresource/init(named:in:))*