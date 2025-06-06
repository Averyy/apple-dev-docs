# update(from:)

**Framework**: ARKit  
**Kind**: method

Reshapes the SceneKit geometry to match the specified plane mesh.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.1+

## Declaration

```swift
func update(from planeGeometry: ARPlaneGeometry)
```

#### Discussion

To update a SceneKit model of a plane actively tracked in an AR session, call this method in your [`ARSCNViewDelegate`](arscnviewdelegate.md) object’s [`renderer(_:didUpdate:for:)`](arscnviewdelegate/renderer(_:didupdate:for:).md) callback, passing the [`geometry`](arplaneanchor/geometry.md) property from the [`ARPlaneAnchor`](arplaneanchor.md) object that callback provides.

## Parameters

- `planeGeometry`: A coarse mesh representation of a detected plane’s estimated shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arscnplanegeometry/update(from:))*