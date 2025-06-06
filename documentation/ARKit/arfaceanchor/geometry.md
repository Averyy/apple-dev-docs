# geometry

**Framework**: ARKit  
**Kind**: property

A coarse triangle mesh representing the topology of the detected face.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var geometry: ARFaceGeometry { get }
```

#### Discussion

This mesh provides vertex, index, and texture coordinate buffers describing the 3D shape of the face, conforming a generic face model to match the dimensions, shape, and current expression of the detected face.

You can visualize the face geometry by passing these buffers to your preferred rendering engine. To visualize a face geometry using SceneKit, create an [`ARSCNFaceGeometry`](arscnfacegeometry.md) instance and use its [`update(from:)`](arscnfacegeometry/update(from:).md) method to update it to match the face geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arfaceanchor/geometry)*