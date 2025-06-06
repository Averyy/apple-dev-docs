# update(from:)

**Framework**: ARKit  
**Kind**: method

Deforms the SceneKit geometry to match the specified face mesh.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func update(from faceGeometry: ARFaceGeometry)
```

#### Discussion

To update a SceneKit model of a face actively tracked in an AR session, call this method in your [`ARSCNViewDelegate`](arscnviewdelegate.md) object’s [`renderer(_:didUpdate:for:)`](arscnviewdelegate/renderer(_:didupdate:for:).md) callback, passing the [`geometry`](arfaceanchor/geometry.md) property from the [`ARFaceAnchor`](arfaceanchor.md) object that callback provides.

Alternatively, you can create, configure, and visualize face models independent of an AR session by creating face geometry objects using the [`ARFaceGeometry`](arfacegeometry.md) [`init(blendShapes:)`](arfacegeometry/init(blendshapes:).md) initializer and passing them to this method.

## Parameters

- `faceGeometry`: A coarse mesh representation of a face’s topology, dimensions, and expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arscnfacegeometry/update(from:))*