# raycastQuery(from:allowing:alignment:)

**Framework**: ARKit  
**Kind**: method

Get a ray-cast query for a screen point.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func raycastQuery(from point: CGPoint, allowing target: ARRaycastQuery.Target, alignment: ARRaycastQuery.TargetAlignment) -> ARRaycastQuery
```

#### Discussion

To cast the ray, you pass the resulting query to your current session via [`raycast(_:)`](arsession/raycast(_:).md) or [`trackedRaycast(_:updateHandler:)`](arsession/trackedraycast(_:updatehandler:).md).

## Parameters

- `point`: A normalized coordinate in the UI system, where 0 is top-left, and 1 is bottom-right.
- `target`: The types of plane you allow this ray cast to intersect with.
- `alignment`: An alignment with respect to gravity a plane must have to interset this ray.

## See Also

- [var anchors: [ARAnchor]](arframe/anchors.md)
  The list of anchors representing positions tracked or objects detected in the scene.
- [func hitTest(CGPoint, types: ARHitTestResult.ResultType) -> [ARHitTestResult]](arframe/hittest(_:types:).md)
  Searches for real-world objects or AR anchors in the captured camera image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arframe/raycastquery(from:allowing:alignment:))*