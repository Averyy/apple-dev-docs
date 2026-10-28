# init(from:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates a reverb mesh resource from a list of mesh descriptors.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
convenience init(from descriptors: [MeshDescriptor]) throws
```

**Other overloads**:

```swift
@MainActor
convenience init(from mesh: MeshResource) throws
```

## Parameters

- `descriptors`: The mesh descriptors to combine into a single reverb mesh.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/reverbmeshresource/init(from:)-4gz03)*