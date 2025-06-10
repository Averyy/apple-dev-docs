# projectPoint(_:)

**Framework**: SceneKit  
**Kind**: method  
**Required**: Yes

Projects a point from the 3D world coordinate system of the scene to the 2D pixel coordinate system of the renderer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func projectPoint(_ point: SCNVector3) -> SCNVector3
```

#### Return Value

The corresponding point in the screen-space (view, layer, or GPU viewport) coordinate system of the scene renderer.

#### Discussion

The z-coordinate of the returned point describes the depth of the projected point relative to the near and far clipping planes of the renderer’s viewing frustum (defined by its [`pointOfView`](scnscenerenderer/pointofview.md) node). Projecting a point on the near clipping plane returns a point whose z-coordinate is `0.0`; projecting a point on the far clipping plane returns a point whose z-coordinate is `1.0`.

## Parameters

- `point`: A point in the world coordinate system of the renderer’s scene.

## See Also

- [func hitTest(CGPoint, options: [SCNHitTestOption : Any]?) -> [SCNHitTestResult]](scnscenerenderer/hittest(_:options:).md)
  Searches the renderer’s scene for objects corresponding to a point in the rendered image.
- [struct SCNHitTestOption](scnhittestoption.md)
  Options affecting the behavior of SceneKit hit-testing methods.
- [func isNode(SCNNode, insideFrustumOf: SCNNode) -> Bool](scnscenerenderer/isnode(_:insidefrustumof:).md)
  Returns a Boolean value indicating whether a node might be visible from a specified point of view.
- [func nodesInsideFrustum(of: SCNNode) -> [SCNNode]](scnscenerenderer/nodesinsidefrustum(of:).md)
  Returns all nodes that might be visible from a specified point of view.
- [func unprojectPoint(SCNVector3) -> SCNVector3](scnscenerenderer/unprojectpoint(_:).md)
  Unprojects a point from the 2D pixel coordinate system of the renderer to the 3D world coordinate system of the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerenderer/projectpoint(_:))*