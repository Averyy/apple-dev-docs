# collisionMode

**Framework**: MapKit JS  
**Kind**: property

A mode that determines the shape of the collision frame.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
collisionMode?: CollisionMode;
```

#### Discussion

Use one of the modes available in [`CollisionMode`](collisionmode.md):

- `mapkit.Annotation.CollisionMode.Rectangle` — Indicates the bounding box of the annotation.
- `mapkit.Annotation.CollisionMode.Circle` — Indicates a circle within the bounding box.

The default value is `Annotation.CollisionMode.Rectangle`.

## See Also

- [clusteringIdentifier](annotationconstructoroptions/clusteringidentifier.md)
  An identifier for grouping annotations into the same cluster.
- [id](annotationconstructoroptions/id.md)
  A Place ID that uniquely identifies a feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/annotationconstructoroptions/collisionmode)*