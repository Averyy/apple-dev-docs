# annotationsInMapRect(mapRect)

**Framework**: MapKit JS  
**Kind**: method  
**Role**: Instance Method

Returns the list of annotation objects within the specified map rectangle.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
annotationsInMapRect(mapRect: MapRectData): Annotation[];
```

## Mentions

- [MapKit JS 5](../mapkit-js-5.md)

## Return Value

Returns an array of annotations that fall inside `mapRect`.

## Parameters

- `mapRect`: The portion of the map in which to look for annotations.

## See Also

### Annotating the map
- [annotations](./annotations.md)
  An array of all the annotations on the map.
- [selectedAnnotation](./selectedannotation.md)
  The selected annotation.
- [annotationForCluster](./annotationforcluster.md)
  A delegate method for modifying an annotation that represents a group of annotations that the framework combines into a cluster.
- [addAnnotation(annotation)](./addannotation.md)
  Adds an annotation to the map.
- [addAnnotations(annotations)](./addannotations.md)
  Adds an array of annotations to the map.
- [removeAnnotation(annotation)](./removeannotation.md)
  Removes an annotation from the map.
- [removeAnnotations(annotations)](./removeannotations.md)
  Removes multiple annotations from the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/map/annotationsinmaprect)*