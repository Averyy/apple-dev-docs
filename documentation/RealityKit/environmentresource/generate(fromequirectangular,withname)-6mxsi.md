# generate(fromEquirectangular:withName:)

**Framework**: RealityKit  
**Kind**: method

Asynchronously generates an environment resource from an equirectangular image.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency static func generate(fromEquirectangular cgImage: CGImage, withName resourceName: String? = nil) async throws -> EnvironmentResource
```

## See Also

- [static func generate(fromEquirectangular: CGImage, withName: String?) throws -> EnvironmentResource](environmentresource/generate(fromequirectangular:withname:)-3wtpe.md)
  Synchronously generates an environment resource from an equirectangular image.
- [static func loadAsync(named: String, in: Bundle?) -> LoadRequest<EnvironmentResource>](environmentresource/loadasync(named:in:).md)
  Asynchronously loads an environment resource from a bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/environmentresource/generate(fromequirectangular:withname:)-6mxsi)*