# annotationsInMapRect

**Framework**: MapKit JS  
**Kind**: method

Returns the list of annotation objects within the specified map rectangle.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
mapkit.Annotation[] annotationsInMapRect(
	mapkit.MapRect mapRect
);
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

#### Return Value

Returns an array of annotations that fall inside `mapRect`.

## Parameters

- `mapRect`: The portion of the map in which to look for annotations.

## See Also

- [annotations](mapkit.map/annotations.md)
  An array of all the annotations on the map.
- [selectedAnnotation](mapkit.map/selectedannotation.md)
  The selected annotation.
- [annotationForCluster](mapkit.map/annotationforcluster.md)
  A delegate method for modifying an annotation that represents a group of annotations that the framework combines into a cluster.
- [addAnnotation](mapkit.map/addannotation.md)
  Adds an annotation to the map.
- [addAnnotations](mapkit.map/addannotations.md)
  Adds an array of annotations to the map.
- [removeAnnotation](mapkit.map/removeannotation.md)
  Removes an annotation from the map.
- [removeAnnotations](mapkit.map/removeannotations.md)
  Removes multiple annotations from the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.map/annotationsinmaprect)*