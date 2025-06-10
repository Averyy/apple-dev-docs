# hitTest(_:types:)

**Framework**: ARKit  
**Kind**: method

Searches for real-world objects or AR anchors in the captured camera image corresponding to a point in the SceneKit view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func hitTest(_ point: CGPoint, types: ARHitTestResult.ResultType) -> [ARHitTestResult]
```

#### Return Value

A list of results, sorted from nearest to farthest (in distance from the camera).

#### Discussion

Hit testing searches for real-world objects or surfaces detected through the AR session’s processing of the camera image. A 2D point in the view’s coordinate system can refer to any point along a 3D line that starts at the device camera and extends in a direction determined by the device orientation and camera projection. This method searches along that line, returning all objects that intersect it in order of distance from the camera.

> **Note**:  This method searches for AR anchors and real-world objects detected by the AR session, not SceneKit content displayed in the view. To search for SceneKit objects, use the view’s [`hitTest(_:options:)`](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1522929-hittest) method instead.

The behavior of a hit test depends on which `types` you specify and the order you specify them in. For details, see [`ARHitTestResult`](arhittestresult.md) and the various [`ARHitTestResult.ResultType`](arhittestresult/resulttype.md) options.

## Parameters

- `point`: A point in the 2D coordinate system of the view.
- `types`: The types of hit-test result to search for.

## See Also

- [func raycastQuery(from: CGPoint, allowing: ARRaycastQuery.Target, alignment: ARRaycastQuery.TargetAlignment) -> ARRaycastQuery?](arscnview/raycastquery(from:allowing:alignment:).md)
  Creates a raycast query that originates from a point on the view, aligned with the center of the camera’s field of view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arscnview/hittest(_:types:))*