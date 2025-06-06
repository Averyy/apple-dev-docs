# clusteringIdentifier

**Framework**: MapKit JS  
**Kind**: property

An identifier for grouping annotations into the same cluster.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute string clusteringIdentifier;
```

#### Discussion

When zooming out on a map that contains many annotations, MapKit JS groups the colliding annotations based on a clustering identifier value.

The default value is `null`.

For more information, see [`Clustering annotations`](clustering-annotations.md).

## See Also

- [collisionMode](annotationconstructoroptions/collisionmode.md)
  A mode that determines the shape of the collision frame.
- [id](annotationconstructoroptions/id.md)
  A Place ID that uniquely identifies a feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/annotationconstructoroptions/clusteringidentifier)*