# collisionMode

**Framework**: MapKit JS  
**Kind**: property

A mode that determines the shape of the collision frame.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
get collisionMode(): CollisionMode;
set collisionMode(value: CollisionMode);
```

#### Discussion

The collision mode indicates whether the annotation collides, and, if so, the shape of an annotation’s collision frame:

The default value is [`Rectangle`](collisionmode/rectangle.md).

## See Also

- [memberAnnotations](annotation/memberannotations.md)
  An array of annotations that the framework groups together in a cluster.
- [clusteringIdentifier](annotation/clusteringidentifier.md)
  An identifier for grouping annotations into the same cluster.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/annotation/collisionmode-data.property)*