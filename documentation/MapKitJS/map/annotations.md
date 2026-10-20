# annotations

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Instance Property

An array of all the annotations on the map.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
get annotations(): Annotation[];
set annotations(annotations: Annotation[]);
```

## Mentions

- [MapKit JS 5](../mapkit-js-5.md)

#### Discussion

You can set this property to a new (possibly empty) array of annotations, which updates all the annotations on the map.

## See Also

### Annotating the map
- [selectedAnnotation](./selectedannotation.md)
  The selected annotation.
- [annotationForCluster](./annotationforcluster.md)
  A delegate method for modifying an annotation that represents a group of annotations that the framework combines into a cluster.
- [annotationsInMapRect(mapRect)](./annotationsinmaprect.md)
  Returns the list of annotation objects within the specified map rectangle.
- [addAnnotation(annotation)](./addannotation.md)
  Adds an annotation to the map.
- [addAnnotations(annotations)](./addannotations.md)
  Adds an array of annotations to the map.
- [removeAnnotation(annotation)](./removeannotation.md)
  Removes an annotation from the map.
- [removeAnnotations(annotations)](./removeannotations.md)
  Removes multiple annotations from the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/map/annotations)*