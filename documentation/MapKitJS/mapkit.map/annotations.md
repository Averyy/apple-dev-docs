# annotations

**Framework**: MapKit JS  
**Kind**: property

An array of all the annotations on the map.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute mapkit.Annotation[] annotations;
```

## Mentions

- [Clustering annotations](clustering-annotations.md)
- [MapKit JS 5](mapkit-js-5.md)

#### Discussion

You can set this attribute to a new (possibly empty) array of annotations, which updates all the annotations on the map.

## See Also

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
- [removeAnnotations](mapkit.map/removeannotations.md)
  Removes multiple annotations from the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.map/annotations)*