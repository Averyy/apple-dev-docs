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

#### Overview

If you use [`ARView`](../RealityKit/arview.md) or [`ARSCNView`](./arscnview.md) as your renderer, you can search for real-world surfaces at a screen point using the [`raycast(from:allowing:alignment:)`](../RealityKit/arview/raycast%28from,allowing,alignment%29.md), and [`raycastQuery(from:allowing:alignment:)`](./arscnview/raycastquery%28from,allowing,alignment%29.md) functions, respectively.

If you use a custom renderer, you can find real-world positions using screen points with:

- The [`raycastQuery(from:allowing:alignment:)`](./arframe/raycastquery%28from,allowing,alignment%29.md) function of [`ARFrame`](./arframe.md).
- The [`raycast(_:)`](./arsession/raycast%28_%29.md) function of [`ARSession`](./arsession.md).

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
  A specification that indicates a target’s alignment with respect to gravity

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