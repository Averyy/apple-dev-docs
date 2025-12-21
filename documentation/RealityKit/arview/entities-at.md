# entities(at:)

**Framework**: RealityKit  
**Kind**: method

Finds the collection of entities at the specified point in the scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency func entities(at point: CGPoint) -> [Entity]
```

#### Return Value

An array of entities at `point`. The array is empty if there are no entities.

#### Discussion

The method ignores entities that lack a [`CollisionComponent`](collisioncomponent.md).

## Parameters

- `point`: A point in the view’s coordinate system.

## See Also

- [func entity(at: CGPoint) -> Entity?](arview/entity(at:).md)
  Finds the entity in the AR scene closest to the specified point.
- [func hitTest(CGPoint, query: CollisionCastQueryType, mask: CollisionGroup) -> [CollisionCastHit]](arview/hittest(_:query:mask:).md)
  Searches for objects corresponding to a point in the view based on a query and a collision mask.
- [func hitTest(CGPoint, types: ARHitTestResult.ResultType) -> [ARHitTestResult]](arview/hittest(_:types:).md)
  Searches for objects corresponding to a point in the view based on a set of result types.
- [func makeRaycastQuery(from: CGPoint, allowing: ARRaycastQuery.Target, alignment: ARRaycastQuery.TargetAlignment) -> ARRaycastQuery?](arview/makeraycastquery(from:allowing:alignment:).md)
  Creates a ray-cast query originating from a point in the view, centered on the camera’s field of view.
- [func raycast(from: CGPoint, allowing: ARRaycastQuery.Target, alignment: ARRaycastQuery.TargetAlignment) -> [ARRaycastResult]](arview/raycast(from:allowing:alignment:).md)
  Performs a ray cast, where a ray is cast into the scene from the center of the camera through a point in the view, and the results are immediately returned.
- [func trackedRaycast(from: CGPoint, allowing: ARRaycastQuery.Target, alignment: ARRaycastQuery.TargetAlignment, updateHandler: ([ARRaycastResult]) -> Void) -> ARTrackedRaycast?](arview/trackedraycast(from:allowing:alignment:updatehandler:).md)
  Performs a tracked ray cast, where a ray is cast into the scene from the center of the camera through a point in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/entities(at:))*