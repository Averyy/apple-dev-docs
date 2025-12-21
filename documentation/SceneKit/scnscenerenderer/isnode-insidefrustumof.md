# isNode(_:insideFrustumOf:)

**Framework**: SceneKit  
**Kind**: method  
**Required**: Yes

Returns a Boolean value indicating whether a node might be visible from a specified point of view.

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
func isNode(_ node: SCNNode, insideFrustumOf pointOfView: SCNNode) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the bounding box of the tested node intersects the view frustum defined by the `pointOfView` node; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

Any node containing a camera or spotlight may serve as a point of view (see the [`pointOfView`](scnscenerenderer/pointofview.md) property for details). Such a node defines a —a portion of the scene’s coordinate space, shaped like a truncated pyramid, that encloses all points visible from that point of view.

Use this method to test whether a node lies within the viewing frustum defined by another node (which may or may not be the scene renderer’s current [`pointOfView`](scnscenerenderer/pointofview.md) node). For example, in a game scene containing multiple camera nodes, you could use this method to determine which camera is currently best for viewing a moving player character.

Note that this method does not perform occlusion testing. That is, it returns [`true`](https://developer.apple.com/documentation/Swift/true) if the tested node lies within the specified viewing frustum regardless of whether that node’s contents are obscured by other geometry.

## Parameters

- `node`: The node whose visibility is to be tested.
- `pointOfView`: A node defining a point of view, as used by the   property.

## See Also

- [func hitTest(CGPoint, options: [SCNHitTestOption : Any]?) -> [SCNHitTestResult]](scnscenerenderer/hittest(_:options:).md)
  Searches the renderer’s scene for objects corresponding to a point in the rendered image.
- [struct SCNHitTestOption](scnhittestoption.md)
  Options affecting the behavior of SceneKit hit-testing methods.
- [func nodesInsideFrustum(of: SCNNode) -> [SCNNode]](scnscenerenderer/nodesinsidefrustum(of:).md)
  Returns all nodes that might be visible from a specified point of view.
- [func projectPoint(SCNVector3) -> SCNVector3](scnscenerenderer/projectpoint(_:).md)
  Projects a point from the 3D world coordinate system of the scene to the 2D pixel coordinate system of the renderer.
- [func unprojectPoint(SCNVector3) -> SCNVector3](scnscenerenderer/unprojectpoint(_:).md)
  Unprojects a point from the 2D pixel coordinate system of the renderer to the 3D world coordinate system of the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerenderer/isnode(_:insidefrustumof:))*