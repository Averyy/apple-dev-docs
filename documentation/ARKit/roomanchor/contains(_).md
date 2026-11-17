# contains(_:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether a room contains the provided point.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func contains(_ point: SIMD3<Float>) -> Bool
```

## Return Value

`true` if the room contains the point, otherwise `false`.

## Parameters

- `point`: The point to search for.

## See Also

### Inspecting a room anchor
- [func geometries(classifiedAs: SurfaceClassification) -> [MeshAnchor.Geometry]](./geometries%28classifiedas%29.md)
  Get disjoint mesh geometries of a given surface classification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/roomanchor/contains(_:))*