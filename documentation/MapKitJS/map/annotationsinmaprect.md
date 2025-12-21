# annotationsInMapRect(mapRect)

**Framework**: MapKit JS  
**Kind**: method

Returns the list of annotation objects within the specified map rectangle.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
annotationsInMapRect(mapRect: MapRect): Annotation[];
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

#### Return Value

Returns an array of annotations that fall inside `mapRect`.

## Parameters

- `mapRect`: The portion of the map in which to look for annotations.

## See Also

- [annotations](map/annotations.md)
  An array of all the annotations on the map.
- [selectedAnnotation](map/selectedannotation.md)
  The selected annotation.
- [annotationForCluster](map/annotationforcluster.md)
  A delegate method for modifying an annotation that represents a group of annotations that the framework combines into a cluster.
- [addAnnotation(annotation)](map/addannotation.md)
  Adds an annotation to the map.
- [addAnnotations(annotations)](map/addannotations.md)
  Adds an array of annotations to the map.
- [removeAnnotation(annotation)](map/removeannotation.md)
  Removes an annotation from the map.
- [removeAnnotations(annotations)](map/removeannotations.md)
  Removes multiple annotations from the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/map/annotationsinmaprect)*