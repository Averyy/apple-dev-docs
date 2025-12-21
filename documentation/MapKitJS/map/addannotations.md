# addAnnotations(annotations)

**Framework**: MapKit JS  
**Kind**: method

Adds an array of annotations to the map.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
addAnnotations(annotations: Annotation[]): Annotation[];
```

#### Return Value

Returns the array of annotations.

#### Discussion

The map shows annotations that have their [`animates`](annotation/animates.md) property set to `true` in a staggered manner, in order of latitude.

> **Note**:  MapKitJS immediately adds the annotations to the [`annotations`](map/annotations.md) array, then visually displays them on the map.

## Parameters

- `annotations`: An array of annotations to add.

## See Also

- [annotations](map/annotations.md)
  An array of all the annotations on the map.
- [selectedAnnotation](map/selectedannotation.md)
  The selected annotation.
- [annotationForCluster](map/annotationforcluster.md)
  A delegate method for modifying an annotation that represents a group of annotations that the framework combines into a cluster.
- [annotationsInMapRect(mapRect)](map/annotationsinmaprect.md)
  Returns the list of annotation objects within the specified map rectangle.
- [addAnnotation(annotation)](map/addannotation.md)
  Adds an annotation to the map.
- [removeAnnotation(annotation)](map/removeannotation.md)
  Removes an annotation from the map.
- [removeAnnotations(annotations)](map/removeannotations.md)
  Removes multiple annotations from the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/map/addannotations)*