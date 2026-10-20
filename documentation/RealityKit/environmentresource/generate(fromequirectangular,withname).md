# generate(fromEquirectangular:withName:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

Asynchronously generates an environment resource from an equirectangular image.

**Availability**:
- visionOS 1.0+ - Deprecated in 2.0 (renamed: EnvironmentResource.init(equirectangular:withName:))

## Declaration

```swift
@MainActor
@preconcurrency static func generate(fromEquirectangular cgImage: CGImage, withName resourceName: String? = nil) async throws -> EnvironmentResource
```

**Other overloads**:

```swift
@MainActor
@preconcurrency static func generate(fromEquirectangular cgImage: CGImage, withName resourceName: String? = nil) throws -> EnvironmentResource
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/environmentresource/generate(fromequirectangular:withname:))*