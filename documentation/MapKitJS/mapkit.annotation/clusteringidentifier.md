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

## Mentions

- [Clustering annotations](clustering-annotations.md)
- [MapKit JS 5](mapkit-js-5.md)

#### Discussion

For MapKit JS to cluster annotations, an annotation needs a `clusteringIdentifie`r. When annotations collide and have the same `clusteringIdentifier`, MapKit JS clusters them together.

The default value is `null`.

For more details, see [`Clustering annotations`](clustering-annotations.md).

## See Also

- [memberAnnotations](mapkit.annotation/memberannotations.md)
  An array of annotations that the framework groups together in a cluster.
- [collisionMode](mapkit.annotation/collisionmode.md)
  A mode that determines the shape of the collision frame.
- [mapkit.Annotation.CollisionMode](mapkit.annotation.collisionmode.md)
  Constants that indicate whether an annotation collides and how to interpret the collision-frame rectangle of an annotation view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.annotation/clusteringidentifier)*