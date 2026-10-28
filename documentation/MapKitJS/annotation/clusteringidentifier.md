# clusteringIdentifier

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Instance Property

An identifier for grouping annotations into the same cluster.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
get clusteringIdentifier(): string | null;
set clusteringIdentifier(value: string | null);
```

## Mentions

- [MapKit JS 5](../mapkit-js-5.md)

## Discussion

For MapKit JS to cluster annotations, an annotation needs a `clusteringIdentifie`r. When annotations collide and have the same `clusteringIdentifier`, MapKit JS clusters them together.

The default value is `null`.

For more details, see [Clustering annotations](../clustering-annotations.md).

## See Also

### Managing clustering
- [memberAnnotations](./memberannotations.md)
  An array of annotations that the framework groups together in a cluster.
- [collisionMode](./collisionmode-data.property.md)
  A mode that determines the shape of the collision frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/annotation/clusteringidentifier)*