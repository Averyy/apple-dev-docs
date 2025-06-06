# ARRaycastQuery

**Framework**: ARKit  
**Kind**: class

A mathematical ray you use to find 3D positions on real-world surfaces.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class ARRaycastQuery
```

#### Overview

You create a raycast query by providing a 3D vector and starting place.

To create a raycast query using a 2D screen location and default vector that casts outward in the z-direction from the user, use the convenience functions, [`makeRaycastQuery(from:allowing:alignment:)`](https://developer.apple.com/documentation/RealityKit/ARView/makeRaycastQuery(from:allowing:alignment:)) on [`ARView`](https://developer.apple.com/documentation/RealityKit/ARView), or [`raycastQuery(from:allowing:alignment:)`](arscnview/raycastquery(from:allowing:alignment:).md) on [`ARSCNView`](arscnview.md).

Raycasts can intersect with planes (flat surfaces) or meshes (uneven surfaces). To intersect with planes, see [`ARRaycastQuery.Target`](arraycastquery/target-swift.enum.md). To intersect with meshes, see [`ARRaycastQuery.Target.estimatedPlane`](arraycastquery/target-swift.enum/estimatedplane.md).

## Topics

### Creating a Raycast Query
- [init(origin: simd_float3, direction: simd_float3, allowing: ARRaycastQuery.Target, alignment: ARRaycastQuery.TargetAlignment)](arraycastquery/init(origin:direction:allowing:alignment:).md)
  Creates a new raycast query.
### Specifying the Target
- [var target: ARRaycastQuery.Target](arraycastquery/target-swift.property.md)
  A plane type that allows the raycast to terminate if it’s encountered.
- [ARRaycastQuery.Target](arraycastquery/target-swift.enum.md)
  The types of surface you allow a raycast to intersect with.
- [var targetAlignment: ARRaycastQuery.TargetAlignment](arraycastquery/targetalignment-swift.property.md)
  The target’s alignment with respect to gravity.
- [ARRaycastQuery.TargetAlignment](arraycastquery/targetalignment-swift.enum.md)
  A specification that indicates a target’s alignment with respect to gravity
### Interpreting the Ray
- [var direction: simd_float3](arraycastquery/direction.md)
  A vector that describes the ray’s trajectory in 3D space.
- [var origin: simd_float3](arraycastquery/origin.md)
  A 3D coordinate that defines the ray’s starting place.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Placing objects and handling 3D interaction](placing-objects-and-handling-3d-interaction.md)
  Place virtual content at tracked, real-world locations, and enable the user to interact with virtual content by using gestures.
- [class ARTrackedRaycast](artrackedraycast.md)
  A raycast query that ARKit repeats in succession to give you refined results over time.
- [class ARRaycastResult](arraycastresult.md)
  Information about a real-world surface found by examining a point on the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arraycastquery)*