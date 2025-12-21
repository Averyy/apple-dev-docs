# memberAnnotations

**Framework**: MapKit JS  
**Kind**: property

An array of annotations that the framework groups together in a cluster.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
get memberAnnotations(): Annotation[] | undefined;
```

#### Discussion

The [`memberAnnotations`](annotation/memberannotations.md) array contains all of the annotations that MapKit JS groups together in a cluster. This is a flat array. If there are multiple clusters of annotations, this array contains all of the individual annotations within those clusters; it doesn’t contain any cluster annotations.

## See Also

- [clusteringIdentifier](annotation/clusteringidentifier.md)
  An identifier for grouping annotations into the same cluster.
- [collisionMode](annotation/collisionmode-data.property.md)
  A mode that determines the shape of the collision frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/annotation/memberannotations)*