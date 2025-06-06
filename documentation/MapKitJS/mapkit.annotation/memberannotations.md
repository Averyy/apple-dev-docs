# memberAnnotations

**Framework**: MapKit JS  
**Kind**: property

An array of annotations that the framework groups together in a cluster.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute mapkit.Annotation[] memberAnnotations;
```

## Mentions

- [Clustering annotations](clustering-annotations.md)

#### Discussion

The [`memberAnnotations`](mapkit.annotation/memberannotations.md) array contains all of the annotations that MapKit JS groups together in a cluster. This is a flat array. If there are multiple clusters of annotations, this array contains all of the individual annotations within those clusters; it doesn’t contain any cluster annotations.

## See Also

- [clusteringIdentifier](mapkit.annotation/clusteringidentifier.md)
  An identifier for grouping annotations into the same cluster.
- [collisionMode](mapkit.annotation/collisionmode.md)
  A mode that determines the shape of the collision frame.
- [mapkit.Annotation.CollisionMode](mapkit.annotation.collisionmode.md)
  Constants that indicate whether an annotation collides and how to interpret the collision-frame rectangle of an annotation view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.annotation/memberannotations)*