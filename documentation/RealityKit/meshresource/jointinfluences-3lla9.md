# MeshResource.JointInfluences

**Framework**: RealityKit  
**Kind**: struct

A buffer of vertex-joint influences which bind the mesh part’s vertices to a skeleton via a skinning deformation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
struct JointInfluences
```

#### Overview

Each vertex is associated with a fixed number of influences. If `influencesPerVertex` is 4, then there should be four elements in the buffer of joint influences for each vertex in the mesh part.

> **Note**: If a particular vertex needs fewer influences than the `influencesPerVertex` value, the influences for that vertex can be padded with zero-weight influences.

## Topics

### Initializers
- [init(influences:influencesPerVertex:)](meshresource/jointinfluences-3lla9/init(influences:influencespervertex:).md)
  Associates every vertex in the mesh with a fixed number of influences per vertex.
### Instance Properties
- [var influences: MeshBuffers.JointInfluences](meshresource/jointinfluences-3lla9/influences.md)
  Buffer of joint influences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/jointinfluences-3lla9)*