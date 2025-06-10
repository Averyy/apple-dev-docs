# hitTest(_:options:)

**Framework**: SpriteKit  
**Kind**: method

Searches the Scene Kit scene for objects corresponding to a point in the rendered image.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@MainActor
func hitTest(_ point: CGPoint, options: [String : Any]? = nil) -> [SCNHitTestResult]
```

#### Return Value

An array of [`SCNHitTestResult`](https://developer.apple.com/documentation/SceneKit/SCNHitTestResult) objects representing search results.

#### Discussion

A point in the SpriteKit node’s 2D viewport coordinate space can refer to any point along a line segment in the 3D SceneKit coordinate space. Hit-testing is the process of finding elements of a scene located along this line segment. For example, you can use this method to find the geometry corresponding to a touch event.

## Parameters

- `point`: A point in the viewport coordinate system of the SpriteKit node.
- `options`: A dictionary of options affecting the search. See Hit Testing Options Keys for acceptable values.

## See Also

- [func projectPoint(vector_float3) -> vector_float3](sk3dnode/projectpoint(_:).md)
  Projects a point from the 3D world coordinate system of the SceneKit scene to the 2D viewport coordinate system of the SpriteKit node.
- [func unprojectPoint(vector_float3) -> vector_float3](sk3dnode/unprojectpoint(_:).md)
  Unprojects a point from the SpriteKit node’s 2D viewport coordinate system to the 3D world coordinate system of the SceneKit scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sk3dnode/hittest(_:options:))*