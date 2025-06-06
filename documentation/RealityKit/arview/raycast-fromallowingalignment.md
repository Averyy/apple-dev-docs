# raycast(from:allowing:alignment:)

**Framework**: RealityKit  
**Kind**: method

Performs a ray cast, where a ray is cast into the scene from the center of the camera through a point in the view, and the results are immediately returned.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency func raycast(from point: CGPoint, allowing target: ARRaycastQuery.Target, alignment: ARRaycastQuery.TargetAlignment) -> [ARRaycastResult]
```

## Mentions

- [Taking Control of Scene Anchoring](taking-control-of-scene-anchoring.md)

#### Return Value

A list of ray-cast results, sorted from nearest to farthest from the camera. The list is empty if the ray cast fails.

## Parameters

- `point`: A point in the view’s local coordinate system.
- `target`: The type of target where the ray should terminate.
- `alignment`: The alignment of the target.

## See Also

- [func entity(at: CGPoint) -> Entity?](arview/entity(at:).md)
  Finds the entity in the AR scene closest to the specified point.
- [func entities(at: CGPoint) -> [Entity]](arview/entities(at:).md)
  Finds the collection of entities at the specified point in the scene.
- [func hitTest(CGPoint, query: CollisionCastQueryType, mask: CollisionGroup) -> [CollisionCastHit]](arview/hittest(_:query:mask:).md)
  Searches for objects corresponding to a point in the view based on a query and a collision mask.
- [func hitTest(CGPoint, types: ARHitTestResult.ResultType) -> [ARHitTestResult]](arview/hittest(_:types:).md)
  Searches for objects corresponding to a point in the view based on a set of result types.
- [func makeRaycastQuery(from: CGPoint, allowing: ARRaycastQuery.Target, alignment: ARRaycastQuery.TargetAlignment) -> ARRaycastQuery?](arview/makeraycastquery(from:allowing:alignment:).md)
  Creates a ray-cast query originating from a point in the view, centered on the camera’s field of view.
- [func trackedRaycast(from: CGPoint, allowing: ARRaycastQuery.Target, alignment: ARRaycastQuery.TargetAlignment, updateHandler: ([ARRaycastResult]) -> Void) -> ARTrackedRaycast?](arview/trackedraycast(from:allowing:alignment:updatehandler:).md)
  Performs a tracked ray cast, where a ray is cast into the scene from the center of the camera through a point in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/raycast(from:allowing:alignment:))*