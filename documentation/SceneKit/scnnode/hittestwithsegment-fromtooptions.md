# hitTestWithSegment(from:to:options:)

**Framework**: SceneKit  
**Kind**: method

Searches the node’s child node subtree for objects intersecting a line segment between two specified points.

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
func hitTestWithSegment(from pointA: SCNVector3, to pointB: SCNVector3, options: [String : Any]? = nil) -> [SCNHitTestResult]
```

#### Return Value

An array of [`SCNHitTestResult`](scnhittestresult.md) objects representing search results.

#### Discussion

Hit-testing is the process of finding elements of a scene located along a specified line segment in the scene’s coordinate space (or that of a particular node in the scene). For example, you can use this method to determine whether a projectile launched by a game character will hit its target.

To search for the scene element corresponding to a two-dimensional point in the rendered image, use the renderer’s [`hitTest(_:options:)`](scnscenerenderer/hittest(_:options:).md) method instead.

## Parameters

- `pointA`: An endpoint of the line segment to search along, specified in the node’s local coordinate system.
- `pointB`: The other endpoint of the line segment to search along, specified in the node’s local coordinate system.
- `options`: A dictionary of options affecting the search. See Hit Testing Options Keys for acceptable values.

## See Also

- [struct SCNHitTestOption](scnhittestoption.md)
  Options affecting the behavior of SceneKit hit-testing methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/hittestwithsegment(from:to:options:))*