# generateAsync(from:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

Create a mesh resource from a list of mesh descriptors asynchronously.

**Availability**:
- iOS 15.0+ - Deprecated in 18.0 (renamed: init(from:))
- iPadOS 15.0+ - Deprecated in 18.0 (renamed: init(from:))
- Mac Catalyst 15.0+ - Deprecated in 18.0 (renamed: init(from:))
- macOS 12.0+ - Deprecated in 15.0 (renamed: init(from:))
- visionOS 1.0+ - Deprecated in 1.0 (renamed: init(from:))

## Declaration

```swift
@MainActor
@preconcurrency static func generateAsync(from descriptors: [MeshDescriptor]) -> LoadRequest<MeshResource>
```

**Other overloads**:

```swift
@MainActor
@preconcurrency static func generateAsync(from content: MeshResource.Contents) -> LoadRequest<MeshResource>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/generateasync(from:)-5m3jh)*