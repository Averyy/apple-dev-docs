# annotations

**Framework**: MapKit JS  
**Kind**: property

An array of all the annotations on the map.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
get annotations(): Annotation[];
set annotations(annotations: Annotation[]);
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

#### Discussion

You can set this property to a new (possibly empty) array of annotations, which updates all the annotations on the map.

## See Also

- [selectedAnnotation](map/selectedannotation.md)
  The selected annotation.
- [annotationForCluster](map/annotationforcluster.md)
  A delegate method for modifying an annotation that represents a group of annotations that the framework combines into a cluster.
- [annotationsInMapRect(mapRect)](map/annotationsinmaprect.md)
  Returns the list of annotation objects within the specified map rectangle.
- [addAnnotation(annotation)](map/addannotation.md)
  Adds an annotation to the map.
- [addAnnotations(annotations)](map/addannotations.md)
  Adds an array of annotations to the map.
- [removeAnnotation(annotation)](map/removeannotation.md)
  Removes an annotation from the map.
- [removeAnnotations(annotations)](map/removeannotations.md)
  Removes multiple annotations from the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/map/annotations)*