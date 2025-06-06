# removeAnnotations

**Framework**: MapKit JS  
**Kind**: method

Removes multiple annotations from the map.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
mapkit.Annotation[] removeAnnotations(
	mapkit.Annotation[] annotations
);
```

#### Return Value

Returns the array of annotations.

## Parameters

- `annotations`: An array of annotations to remove.

## See Also

- [annotations](mapkit.map/annotations.md)
  An array of all the annotations on the map.
- [selectedAnnotation](mapkit.map/selectedannotation.md)
  The selected annotation.
- [annotationForCluster](mapkit.map/annotationforcluster.md)
  A delegate method for modifying an annotation that represents a group of annotations that the framework combines into a cluster.
- [annotationsInMapRect](mapkit.map/annotationsinmaprect.md)
  Returns the list of annotation objects within the specified map rectangle.
- [addAnnotation](mapkit.map/addannotation.md)
  Adds an annotation to the map.
- [addAnnotations](mapkit.map/addannotations.md)
  Adds an array of annotations to the map.
- [removeAnnotation](mapkit.map/removeannotation.md)
  Removes an annotation from the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.map/removeannotations)*