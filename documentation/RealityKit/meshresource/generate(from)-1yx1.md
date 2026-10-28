# generate(from:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

Create a mesh resource from a list of mesh descriptors.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency static func generate(from descriptors: [MeshDescriptor]) throws -> MeshResource
```

**Other overloads**:

```swift
@MainActor
@preconcurrency static func generate(from content: MeshResource.Contents) throws -> MeshResource
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/generate(from:)-1yx1)*