# anchor(for:)

**Framework**: ARKit  
**Kind**: method

Returns the AR anchor associated with the specified SceneKit node, if any.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func anchor(for node: SCNNode) -> ARAnchor?
```

#### Return Value

The [`ARAnchor`](aranchor.md) object tracking the node, or `nil` if the node is not associated with an anchor or not in the view’s scene.

## Parameters

- `node`: A SceneKit node in the view’s scene.

## See Also

- [func node(for: ARAnchor) -> SCNNode?](arscnview/node(for:).md)
  Returns the SceneKit node associated with the specified AR anchor, if any.
- [func unprojectPoint(CGPoint, ontoPlane: simd_float4x4) -> simd_float3?](arscnview/unprojectpoint(_:ontoplane:).md)
  Returns the projection of a point from 2D view onto a plane in the 3D world space detected by ARKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arscnview/anchor(for:))*