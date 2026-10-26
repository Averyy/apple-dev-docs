# node(for:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Returns the SceneKit node associated with the specified AR anchor, if any.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
func node(for anchor: ARAnchor) -> SCNNode?
```

```objc
- (SCNNode *) nodeForAnchor:(ARAnchor *) anchor;
```

#### Return Value

The node whose position in the AR scene the anchor tracks, or `nil` if the anchor has no associated node or is not in the view’s AR session.

## Parameters

- `anchor`: An anchor in the view’s AR session.

## See Also

### Mapping Content to Real-World Positions
- [func anchor(for: SCNNode) -> ARAnchor?](./anchor%28for%29.md)
  Returns the AR anchor associated with the specified SceneKit node, if any.
- [func unprojectPoint(CGPoint, ontoPlane: simd_float4x4) -> simd_float3?](./unprojectpoint%28_,ontoplane%29.md)
  Returns the projection of a point from 2D view onto a plane in the 3D world space detected by ARKit.
- [- unprojectPoint:ontoPlaneWithTransform:](./unprojectpoint_ontoplanewithtransform_.md)
  Returns the projection of a point from 2D view onto a plane in the 3D world space detected by ARKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arscnview/node(for:))*