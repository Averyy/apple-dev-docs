# ARRaycastResult

**Framework**: ARKit  
**Kind**: class  
**Role**: Class

Information about a real-world surface found by examining a point on the screen.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
class ARRaycastResult
```

```objc
@interface ARRaycastResult : NSObject
```

## Overview

A raycast projects a ray from a screen point into the physical environment and returns an [`ARRaycastResult`](./arraycastresult.md) describing each real-world surface the ray intersects.

If you use [`ARView`](../RealityKit/arview.md) as your renderer, you can raycast from a screen point directly with [`raycast(from:allowing:alignment:)`](../RealityKit/arview/raycast%28from,allowing,alignment%29.md). With [`ARSCNView`](./arscnview.md) or a custom renderer, you first build a query and then run it:

- Create a query with [`raycastQuery(from:allowing:alignment:)`](./arscnview/raycastquery%28from,allowing,alignment%29.md) or [`raycastQuery(from:allowing:alignment:)`](./arframe/raycastquery%28from,allowing,alignment%29.md).
- Search for surfaces by passing that query to [`raycast(_:)`](./arsession/raycast%28_%29.md).

For tracked raycasting, you call [`trackedRaycast(_:updateHandler:)`](./arsession/trackedraycast%28_,updatehandler%29.md) on your app’s current [`ARSession`](./arsession.md).

## Topics

### Identifying Results
- [var worldTransform: simd_float4x4](./arraycastresult/worldtransform.md)
  The position, rotation, and scale, of the ray’s intersection with the target.
- [var anchor: ARAnchor?](./arraycastresult/anchor.md)
  The anchor for the plane that the ray intersected.
- [var target: ARRaycastQuery.Target](./arraycastresult/target.md)
  The type of surface that the ray intersects.
- [ARRaycastQuery.Target](./arraycastquery/target-swift.enum.md)
  The types of surface you allow a raycast to intersect with.
- [var targetAlignment: ARRaycastQuery.TargetAlignment](./arraycastresult/targetalignment.md)
  The alignment of the plane that the ray intersected.
- [ARRaycastQuery.TargetAlignment](./arraycastquery/targetalignment-swift.enum.md)
  A specification that indicates a target’s alignment with respect to gravity.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Raycasting
- [Placing objects and handling 3D interaction](./placing-objects-and-handling-3d-interaction.md)
  Place virtual content at tracked, real-world locations, and enable the user to interact with virtual content by using gestures.
- [class ARRaycastQuery](./arraycastquery.md)
  A mathematical ray you use to find 3D positions on real-world surfaces.
- [class ARTrackedRaycast](./artrackedraycast.md)
  A raycast query that ARKit repeats in succession to give you refined results over time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arraycastresult)*