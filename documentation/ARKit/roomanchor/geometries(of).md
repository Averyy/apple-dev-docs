# geometries(of:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Returns the disjoint mesh geometries of a given classification.

**Availability**:
- visionOS 2.0+ - Deprecated in 26.0

> **Deprecated**: Use geometries(classifiedAs: SurfaceClassification) instead.

## Declaration

```swift
func geometries(of classification: MeshAnchor.MeshClassification) -> [MeshAnchor.Geometry]
```

## Return Value

An array of [`MeshAnchor.Geometry`](../meshanchor/geometry-swift.struct.md) structures that match the provided classification.

## Discussion

This method supports the [`MeshAnchor.MeshClassification.floor`](../meshanchor/meshclassification/floor.md) and [`MeshAnchor.MeshClassification.wall`](../meshanchor/meshclassification/wall.md) mesh classifications.

## Parameters

- `classification`: The mesh classification to look for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/roomanchor/geometries(of:))*