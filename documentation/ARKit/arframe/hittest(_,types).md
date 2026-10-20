# hitTest(_:types:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Searches for real-world objects or AR anchors in the captured camera image.

**Availability**:
- iOS 11.0+ - Deprecated in 14.0
- iPadOS 11.0+ - Deprecated in 14.0

> **Deprecated**: Use [ARSession raycast:]

## Declaration

```swift
func hitTest(_ point: CGPoint, types: ARHitTestResult.ResultType) -> [ARHitTestResult]
```

```objc
- (NSArray<ARHitTestResult *> *) hitTest:(CGPoint) point types:(ARHitTestResultType) types;
```

## Mentions

- [Displaying an AR Experience with Metal](../displaying-an-ar-experience-with-metal.md)

#### Return Value

A list of results, sorted from nearest to farthest (in distance from the camera).

#### Discussion

Hit testing searches for real-world objects or surfaces detected through the AR session’s processing of the camera image. A 2D point in the image coordinates can refer to any point along a 3D line that starts at the device camera and extends in a direction determined by the device orientation and camera projection. This method searches along that line, returning all objects that intersect it in order of distance from the camera.

> **Note**:  If you use ARKit with a SceneKit or SpriteKit view, the [`ARSCNView`](../arscnview.md) [`hitTest(_:types:)`](../arscnview/hittest%28_,types%29.md) or [`ARSKView`](../arskview.md) [`hitTest(_:types:)`](../arskview/hittest%28_,types%29.md) method lets you specify a search point in view coordinates.

The behavior of a hit test depends on which `types` you specify and the order you specify them in. For details, see [`ARHitTestResult`](../arhittestresult.md) and the various [`ARHitTestResult.ResultType`](../arhittestresult/resulttype.md) options.

## Parameters

- `point`: A point in normalized image coordinate space. (The point `(0,0)` represents the top left corner of the image, and the point `(1,1)` represents the bottom right corner.)
- `types`: The types of hit-test result to search for.

## See Also

### Tracking and interacting with the real world
- [var anchors: [ARAnchor]](./anchors.md)
  The list of anchors representing positions tracked or objects detected in the scene.
- [func raycastQuery(from: CGPoint, allowing: ARRaycastQuery.Target, alignment: ARRaycastQuery.TargetAlignment) -> ARRaycastQuery](./raycastquery%28from,allowing,alignment%29.md)
  Get a ray-cast query for a screen point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arframe/hittest(_:types:))*