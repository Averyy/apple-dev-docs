# init(influences:influencesPerVertex:)

**Framework**: RealityKit  
**Kind**: init

Associates every vertex in the mesh with a fixed number of influences per vertex.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
init(influences: MeshBuffers.JointInfluences, influencesPerVertex: Int)
```

#### Discussion

> **Note**: The buffer should contain `vertexCount * influencesPerVertex` elements.

## Parameters

- `influences`: Buffer of joint influences.
- `influencesPerVertex`: The number of consecutive influences used by each vertex.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/jointinfluences-3lla9/init(influences:influencespervertex:))*