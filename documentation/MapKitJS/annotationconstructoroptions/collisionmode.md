# collisionMode

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Interface Property

A mode that determines the shape of the collision frame.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
collisionMode?: AnnotationCollisionMode;
```

## Discussion

Use one of the modes available in [`AnnotationCollisionMode`](../annotationcollisionmode.md):

- [`Rectangle`](../annotationcollisionmode/rectangle.md) — Indicates the bounding box of the annotation.
- [`Circle`](../annotationcollisionmode/circle.md) — Indicates a circle within the bounding box.

The default value is [`Rectangle`](../annotationcollisionmode/rectangle.md).

## See Also

### Grouping annotations
- [clusteringIdentifier](./clusteringidentifier.md)
  An identifier for grouping annotations into the same cluster.
- [id](./id.md)
  A Place ID that uniquely identifies a feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/annotationconstructoroptions/collisionmode)*