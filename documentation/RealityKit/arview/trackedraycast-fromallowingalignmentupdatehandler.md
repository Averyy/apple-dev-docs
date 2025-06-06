# trackedRaycast(from:allowing:alignment:updateHandler:)

**Framework**: RealityKit  
**Kind**: method

Performs a tracked ray cast, where a ray is cast into the scene from the center of the camera through a point in the view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency func trackedRaycast(from point: CGPoint, allowing target: ARRaycastQuery.Target, alignment: ARRaycastQuery.TargetAlignment, updateHandler: @escaping ([ARRaycastResult]) -> Void) -> ARTrackedRaycast?
```

#### Return Value

A tracked ray-cast instance used to update or stop ray casting. The result is `nil` if the ray cast fails or if the AR [`session`](arview/session.md) configuration isn’t [`ARWorldTrackingConfiguration`](https://developer.apple.com/documentation/ARKit/ARWorldTrackingConfiguration) or one of its subclasses.

## Parameters

- `point`: A point in the view’s local coordinate system.
- `target`: The type of target where the ray should terminate.
- `alignment`: The alignment of the target.
- `updateHandler`: A closure the method calls to update the list of   results, sorted from nearest to farthest from the camera. The closure is   called on the   instance’s delegate queue.

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
- [func raycast(from: CGPoint, allowing: ARRaycastQuery.Target, alignment: ARRaycastQuery.TargetAlignment) -> [ARRaycastResult]](arview/raycast(from:allowing:alignment:).md)
  Performs a ray cast, where a ray is cast into the scene from the center of the camera through a point in the view, and the results are immediately returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/trackedraycast(from:allowing:alignment:updatehandler:))*