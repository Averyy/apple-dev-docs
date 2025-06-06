# trackedRaycast(_:updateHandler:)

**Framework**: ARKit  
**Kind**: method

Repeats a ray-cast query over time to notify you of updated surfaces in the physical environment.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func trackedRaycast(_ query: ARRaycastQuery, updateHandler: @escaping ([ARRaycastResult]) -> Void) -> ARTrackedRaycast?
```

#### Discussion

A tracked ray cast wraps a ray-cast query that the session calls repeatedly, each time invoking your update handler to provide you with new results.

When you’re ready to stop a tracked ray cast, call [`stopTracking()`](artrackedraycast/stoptracking().md).

## Parameters

- `query`: The ray-cast query that ARKit will repeat. If you use a standard renderer, you ask the standard renderer to provide the ray-cast query; see Finding Real-World Surfaces of  . If you use a custom renderer, you create a ray-cast query by specifying a point on a particular frame; see   in  .
- `updateHandler`: A closure you provide that ARKit calls every time it has an updated ray-cast result for you. Use this opportunity to update the position of any virtual content your app may have placed using the prior results of the tracked ray cast. ARKit invokes this closure on your session’s delegate queue.

## See Also

- [func raycast(ARRaycastQuery) -> [ARRaycastResult]](arsession/raycast(_:).md)
  Checks once for intersections between a ray and real-world surfaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsession/trackedraycast(_:updatehandler:))*