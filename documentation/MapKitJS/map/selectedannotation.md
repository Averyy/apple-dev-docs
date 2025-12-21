# selectedAnnotation

**Framework**: MapKit JS  
**Kind**: property

The selected annotation.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
get selectedAnnotation(): Annotation | null;
set selectedAnnotation(annotation: Annotation | null);
```

#### Discussion

The value of [`selectedAnnotation`](map/selectedannotation.md) is either a [`Annotation`](annotation.md) object, if the user selects one, or `null` if there aren’t any selected annotations.

An annotation is in a selected state if its [`selected`](annotation/selected.md) property is `true`. To deselect all annotations, set this property to `null`.

To select an annotation that’s already part of the map, set this property to the desired annotation.

When MapKit JS removes the selected annotation from the map (as an effect of [`removeAnnotation(annotation)`](map/removeannotation.md), [`removeAnnotations(annotations)`](map/removeannotations.md), or setting a new set of annotations with the [`annotations`](map/annotations.md) property), MapKit JS deselects it before removing it.

## See Also

- [annotations](map/annotations.md)
  An array of all the annotations on the map.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/map/selectedannotation)*