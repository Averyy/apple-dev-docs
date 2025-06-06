# ARTrackedRaycast

**Framework**: ARKit  
**Kind**: class

A raycast query that ARKit repeats in succession to give you refined results over time.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class ARTrackedRaycast
```

#### Overview

Tracked raycasting improves hit-testing techniques by repeating the query for a 3D position in succession. ARKit provides you with an updated position as it refines its understanding of world over time.

To start a tracked raycast, you call [`trackedRaycast(_:updateHandler:)`](arsession/trackedraycast(_:updatehandler:).md) on your app’s current [`ARSession`](arsession.md).

## Topics

### Stopping Tracking
- [func stopTracking()](artrackedraycast/stoptracking.md)
  Stops repeating the raycast query.

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
- [class ARRaycastQuery](arraycastquery.md)
  A mathematical ray you use to find 3D positions on real-world surfaces.
- [class ARRaycastResult](arraycastresult.md)
  Information about a real-world surface found by examining a point on the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/artrackedraycast)*