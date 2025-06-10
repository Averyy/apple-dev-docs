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


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/environmentresource/generate(fromequirectangular:withname:))*