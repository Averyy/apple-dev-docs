# init(origin:direction:allowing:alignment:)

**Framework**: ARKit  
**Kind**: init

Creates a new raycast query.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(origin: simd_float3, direction: simd_float3, allowing target: ARRaycastQuery.Target, alignment: ARRaycastQuery.TargetAlignment)
```

#### Discussion

This creates a query by supplying a 3D starting place and vector. To acquire a raycast query using a screen point and vector that points outward from the user, call [`raycastQuery(from:allowing:alignment:)`](arscnview/raycastquery(from:allowing:alignment:).md) on [`ARSCNView`](arscnview.md).

## Parameters

- `origin`: A 3D position that describes the raycast’s starting point.
- `direction`: A 3D vector that describes the raycast’s direction.
- `target`: The type of plane with which you allow the raycast to intersect.
- `alignment`: The target’s alignment with respect to gravity with which you allow the raycast to intersect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arraycastquery/init(origin:direction:allowing:alignment:))*