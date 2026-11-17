# geometries(classifiedAs:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Get disjoint mesh geometries of a given surface classification.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
func geometries(classifiedAs classification: SurfaceClassification) -> [MeshAnchor.Geometry]
```

## Return Value

The array of mesh geometries.

## Parameters

- `classification`: The classification of the geometries. `SurfaceClassification/floor` and `SurfaceClassification/wall` are supported.

## See Also

### Inspecting a room anchor
- [func contains(SIMD3<Float>) -> Bool](./contains%28_%29.md)
  Returns a Boolean value that indicates whether a room contains the provided point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/roomanchor/geometries(classifiedas:))*