# contains(_:)

**Framework**: ARKit  
**Kind**: method

Returns a Boolean value that indicates whether a room contains the provided point.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func contains(_ point: SIMD3<Float>) -> Bool
```

#### Return Value

Returns `true` if the room contains the point, otherwise `false`.

## Parameters

- `point`: The point to search for.

## See Also

- [func geometries(of: MeshAnchor.MeshClassification) -> [MeshAnchor.Geometry]](roomanchor/geometries(of:).md)
  Returns the disjoint mesh geometries of a given classification.
- [var description: String](roomanchor/description.md)
  A textual representation of this anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/roomanchor/contains(_:))*