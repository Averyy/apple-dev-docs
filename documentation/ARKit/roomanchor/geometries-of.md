# geometries(of:)

**Framework**: ARKit  
**Kind**: method

Returns the disjoint mesh geometries of a given classification.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func geometries(of classification: MeshAnchor.MeshClassification) -> [MeshAnchor.Geometry]
```

#### Return Value

An array of [`MeshAnchor.Geometry`](meshanchor/geometry-swift.struct.md) structures that match the provided classification.

#### Discussion

##Discussion

`RoomAnchor.geometries(of:)` supports the `floor` and `wall` mesh classifications.

## Parameters

- `classification`: The mesh classification to look for.

## See Also

- [func contains(SIMD3<Float>) -> Bool](roomanchor/contains(_:).md)
  Returns a Boolean value that indicates whether a room contains the provided point.
- [var description: String](roomanchor/description.md)
  A textual representation of this anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/roomanchor/geometries(of:))*