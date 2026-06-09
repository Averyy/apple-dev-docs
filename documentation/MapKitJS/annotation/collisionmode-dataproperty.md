# collisionMode

**Framework**: MapKit JS  
**Kind**: property

A mode that determines the shape of the collision frame.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
get collisionMode(): AnnotationCollisionMode;
set collisionMode(value: AnnotationCollisionMode);
```

#### Discussion

The collision mode indicates whether the annotation collides, and, if so, the shape of an annotation’s collision frame:

- **[`Rectangle`](annotationcollisionmode/rectangle.md)**: Indicates the bounding box of the annotation.
- **[`Circle`](annotationcollisionmode/circle.md)**: Indicates a circle within the bounding box.
- **[`None`](annotationcollisionmode/none.md)**: Indicates the annotation doesn’t collide with other annotations.

The default value is [`Rectangle`](annotationcollisionmode/rectangle.md).

## See Also

- [memberAnnotations](annotation/memberannotations.md)
  An array of annotations that the framework groups together in a cluster.
- [clusteringIdentifier](annotation/clusteringidentifier.md)
  An identifier for grouping annotations into the same cluster.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/annotation/collisionmode-data.property)*