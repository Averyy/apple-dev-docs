# clusteringIdentifier

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Interface Property

An identifier for grouping annotations into the same cluster.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
clusteringIdentifier?: string | null;
```

#### Discussion

When zooming out on a map that contains many annotations, MapKit JS groups the colliding annotations based on a clustering identifier value.

The default value is `null`.

For more information, see [Clustering annotations](../clustering-annotations.md).

## See Also

### Grouping annotations
- [collisionMode](./collisionmode.md)
  A mode that determines the shape of the collision frame.
- [id](./id.md)
  A Place ID that uniquely identifies a feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/annotationconstructoroptions/clusteringidentifier)*