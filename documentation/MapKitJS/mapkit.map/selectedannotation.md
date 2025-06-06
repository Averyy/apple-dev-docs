# selectedAnnotation

**Framework**: MapKit JS  
**Kind**: property

The selected annotation.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute mapkit.Annotation selectedAnnotation;
```

#### Discussion

The value of [`selectedAnnotation`](mapkit.map/selectedannotation.md) is either a [`mapkit.Annotation`](mapkit.annotation.md) object, if the user selects one, or `null` if there aren’t any selected annotations.

An annotation is in a selected state if its [`selected`](mapkit.annotation/selected.md) property is `true`. To deselect all annotations, set this attribute to `null`.

To select an annotation that’s already part of the map, set this attribute to the desired annotation.

When MapKit JS removes the selected annotation from the map (as an effect of [`removeAnnotation`](mapkit.map/removeannotation.md), [`removeAnnotations`](mapkit.map/removeannotations.md), or setting a new set of annotations with the [`annotations`](mapkit.map/annotations.md) property), MapKit JS deselects it before removing it.

## See Also

- [annotations](mapkit.map/annotations.md)
  An array of all the annotations on the map.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.map/selectedannotation)*