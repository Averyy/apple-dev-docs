# entity(at:)

**Framework**: RealityKit  
**Kind**: method

Finds the entity in the AR scene closest to the specified point.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func entity(at point: CGPoint) -> Entity?
```

#### Return Value

The entity at `point`, or `nil` if no entity is found.

#### Discussion

The method ignores entities that lack a [`CollisionComponent`](collisioncomponent.md).

## Parameters

- `point`: A point in the view’s coordinate system.

## See Also

- [func entities(at: CGPoint) -> [Entity]](arview/entities(at:).md)
  Finds the collection of entities at the specified point in the scene.
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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/entity(at:))*