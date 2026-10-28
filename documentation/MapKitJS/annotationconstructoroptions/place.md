# place

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Interface Property

An object that allows a custom annotation to potentially supersede a point of interest at the same map coordinates.

**Availability**:
- MapKit JS 5.76.76+

## Declaration

```
place?: Place | SearchAutocompleteResult;
```

## Discussion

By using a [`Place`](../place.md) object as an argument to the [`AnnotationConstructorOptions`](../annotationconstructoroptions.md), you can, depending on the exact coordinates and other rendering computations, supersede an Apple-provided item on the map. This can reduce potential visual clutter of two icons representing the same place on a single map.

You can also use a `Place` as the first argument when creating a [`Annotation`](../annotation.md), rather than using a [`Coordinate`](../coordinate.md) to achieve the same effect.

MapKit JS also supports this capability for the initializer and constructor options for [`ImageAnnotation`](../imageannotation.md) and [`MarkerAnnotation`](../markerannotation.md).

## See Also

### Creating interaction behavior
- [animates](./animates.md)
  A Boolean value that determines whether the map animates the annotation.
- [draggable](./draggable.md)
  A Boolean value that determines whether the user can drag the annotation.
- [enabled](./enabled.md)
  A Boolean value that determines whether the annotation responds to user interaction.
- [selected](./selected.md)
  A Boolean value that determines whether the map displays the annotation in a selected state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/annotationconstructoroptions/place)*