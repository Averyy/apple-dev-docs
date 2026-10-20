# memberAnnotations

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Instance Property

An array of annotations that the framework groups together in a cluster.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
get memberAnnotations(): Annotation[] | null;
```

#### Discussion

The [`memberAnnotations`](./memberannotations.md) array contains all of the annotations that MapKit JS groups together in a cluster. This is a flat array. If there are multiple clusters of annotations, this array contains all of the individual annotations within those clusters; it doesn’t contain any cluster annotations.

## See Also

### Managing clustering
- [clusteringIdentifier](./clusteringidentifier.md)
  An identifier for grouping annotations into the same cluster.
- [collisionMode](./collisionmode-data.property.md)
  A mode that determines the shape of the collision frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/annotation/memberannotations)*