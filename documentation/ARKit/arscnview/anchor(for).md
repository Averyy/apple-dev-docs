# anchor(for:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Returns the AR anchor associated with the specified SceneKit node, if any.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
func anchor(for node: SCNNode) -> ARAnchor?
```

```objc
- (ARAnchor *) anchorForNode:(SCNNode *) node;
```

#### Return Value

The [`ARAnchor`](../aranchor.md) object tracking the node, or `nil` if the node is not associated with an anchor or not in the view’s scene.

## Parameters

- `node`: A SceneKit node in the view’s scene.

## See Also

### Mapping Content to Real-World Positions
- [func node(for: ARAnchor) -> SCNNode?](./node%28for%29.md)
  Returns the SceneKit node associated with the specified AR anchor, if any.
- [func unprojectPoint(CGPoint, ontoPlane: simd_float4x4) -> simd_float3?](./unprojectpoint%28_,ontoplane%29.md)
  Returns the projection of a point from 2D view onto a plane in the 3D world space detected by ARKit.
- [- unprojectPoint:ontoPlaneWithTransform:](./unprojectpoint_ontoplanewithtransform_.md)
  Returns the projection of a point from 2D view onto a plane in the 3D world space detected by ARKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arscnview/anchor(for:))*