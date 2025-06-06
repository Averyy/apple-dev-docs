# hitTest(_:options:)

**Framework**: SceneKit  
**Kind**: method  
**Required**: Yes

Searches the renderer’s scene for objects corresponding to a point in the rendered image.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func hitTest(_ point: CGPoint, options: [SCNHitTestOption : Any]? = nil) -> [SCNHitTestResult]
```

#### Return Value

An array of [`SCNHitTestResult`](scnhittestresult.md) objects representing search results.

#### Discussion

A 2D point in the rendered screen coordinate space can refer to any point along a line segment in the 3D scene coordinate space. Hit-testing is the process of finding elements of a scene located along this line segment. For example, you can use this method to find the geometry corresponding to a click event in a SceneKit view.

## Parameters

- `point`: A point in the screen-space (view, layer, or GPU viewport) coordinate system of the scene renderer.
- `options`: A dictionary of options affecting the search. See Hit Testing Options Keys for acceptable values.

## See Also

- [struct SCNHitTestOption](scnhittestoption.md)
  Options affecting the behavior of SceneKit hit-testing methods.
- [func isNode(SCNNode, insideFrustumOf: SCNNode) -> Bool](scnscenerenderer/isnode(_:insidefrustumof:).md)
  Returns a Boolean value indicating whether a node might be visible from a specified point of view.
- [func nodesInsideFrustum(of: SCNNode) -> [SCNNode]](scnscenerenderer/nodesinsidefrustum(of:).md)
  Returns all nodes that might be visible from a specified point of view.
- [func projectPoint(SCNVector3) -> SCNVector3](scnscenerenderer/projectpoint(_:).md)
  Projects a point from the 3D world coordinate system of the scene to the 2D pixel coordinate system of the renderer.
- [func unprojectPoint(SCNVector3) -> SCNVector3](scnscenerenderer/unprojectpoint(_:).md)
  Unprojects a point from the 2D pixel coordinate system of the renderer to the 3D world coordinate system of the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerenderer/hittest(_:options:))*