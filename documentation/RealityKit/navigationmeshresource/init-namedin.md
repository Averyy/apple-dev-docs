# init(named:in:)

**Framework**: RealityKit  
**Kind**: init

Asynchronously creates a NavigationMeshResource by importing an existing one from a Bundle. The name is the path of the NavigationMeshResource within the bundle. The bundle is the app package that contains the NavigationMeshResource. If nothing is specified, then the main bundle is used. This loads an existing Navigation Mesh and will not process and create a new one.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
convenience init(named name: String, in bundle: Bundle? = nil) async throws
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationmeshresource/init(named:in:))*