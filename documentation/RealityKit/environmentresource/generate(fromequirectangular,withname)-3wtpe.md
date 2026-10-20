# generate(fromEquirectangular:withName:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

Synchronously generates an environment resource from an equirectangular image.

**Availability**:
- visionOS 1.0+ - Deprecated in 2.0 (renamed: EnvironmentResource.init(equirectangular:withName:))

## Declaration

```swift
@MainActor
@preconcurrency static func generate(fromEquirectangular cgImage: CGImage, withName resourceName: String? = nil) throws -> EnvironmentResource
```

**Other overloads**:

```swift
@MainActor
@preconcurrency static func generate(fromEquirectangular cgImage: CGImage, withName resourceName: String? = nil) async throws -> EnvironmentResource
```

## See Also

### Deprecated
- [static func generate(fromEquirectangular: CGImage, withName: String?) async throws -> EnvironmentResource](./generate%28fromequirectangular,withname%29-6mxsi.md)
  Asynchronously generates an environment resource from an equirectangular image.
- [static func loadAsync(named: String, in: Bundle?) -> LoadRequest<EnvironmentResource>](./loadasync%28named,in%29.md)
  Asynchronously loads an environment resource from a bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/environmentresource/generate(fromequirectangular:withname:)-3wtpe)*