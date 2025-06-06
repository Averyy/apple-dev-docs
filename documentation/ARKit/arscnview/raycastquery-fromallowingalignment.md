# raycastQuery(from:allowing:alignment:)

**Framework**: ARKit  
**Kind**: method

Creates a raycast query that originates from a point on the view, aligned with the center of the camera’s field of view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func raycastQuery(from point: CGPoint, allowing target: ARRaycastQuery.Target, alignment: ARRaycastQuery.TargetAlignment) -> ARRaycastQuery?
```

#### Discussion

When you call this function, ARKit creates a ray that extends in the positive z-direction from the argument screen space point, to determine if any of the argument targets exist in the physical environment anywhere along the ray. If so, ARKit returns a 3D position where the ray intersects the target.

## See Also

- [func hitTest(CGPoint, types: ARHitTestResult.ResultType) -> [ARHitTestResult]](arscnview/hittest(_:types:).md)
  Searches for real-world objects or AR anchors in the captured camera image corresponding to a point in the SceneKit view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arscnview/raycastquery(from:allowing:alignment:))*