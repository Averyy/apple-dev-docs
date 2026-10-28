# unprojectPoint(_:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Unprojects a point from the 2D pixel coordinate system of the renderer to the 3D world coordinate system of the scene.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
func unprojectPoint(_ point: SCNVector3) -> SCNVector3
```

```objc
- (SCNVector3) unprojectPoint:(SCNVector3) point;
```

## Return Value

The corresponding point in the world coordinate system of the renderer’s scene.

## Discussion

The z-coordinate of the `point` parameter describes the depth at which to unproject the point relative to the near and far clipping planes of the renderer’s viewing frustum (defined by its [`pointOfView`](./pointofview.md) node). Unprojecting a point whose z-coordinate is `0.0` returns a point on the near clipping plane; unprojecting a point whose z-coordinate is `1.0` returns a point on the far clipping plane.

A 2D point in the rendered screen coordinate space can refer to any point along a line segment in the 3D scene coordinate space. To test for scene contents along this line—for example, to find the geometry corresponding to the location of a click event in a view—use the [`hitTest(_:options:)`](./hittest%28_,options%29.md) method.

## Parameters

- `point`: A point in the screen-space (view, layer, or GPU viewport) coordinate system of the scene renderer.

## See Also

### Working With Projected Scene Contents
- [func hitTest(CGPoint, options: [SCNHitTestOption : Any]?) -> [SCNHitTestResult]](./hittest%28_,options%29.md)
  Searches the renderer’s scene for objects corresponding to a point in the rendered image.
- [struct SCNHitTestOption](../scnhittestoption.md)
  Options affecting the behavior of SceneKit hit-testing methods.
- [func isNode(SCNNode, insideFrustumOf: SCNNode) -> Bool](./isnode%28_,insidefrustumof%29.md)
  Returns a Boolean value indicating whether a node might be visible from a specified point of view.
- [func nodesInsideFrustum(of: SCNNode) -> [SCNNode]](./nodesinsidefrustum%28of%29.md)
  Returns all nodes that might be visible from a specified point of view.
- [func projectPoint(SCNVector3) -> SCNVector3](./projectpoint%28_%29.md)
  Projects a point from the 3D world coordinate system of the scene to the 2D pixel coordinate system of the renderer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerenderer/unprojectpoint(_:))*