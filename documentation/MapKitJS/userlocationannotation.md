# UserLocationAnnotation

**Framework**: MapKit JS  
**Kind**: class

An annotation that represents someone’s location.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
class UserLocationAnnotation extends Annotation
```

#### Discussion

The framework automatically adds a person’s location annotation to the map view when the map view’s [`showsUserLocation`](map/showsuserlocation.md) property is set to `true`.

## Topics

### Instance Properties
- [coordinate](userlocationannotation/coordinate.md)
  The coordinate of the annotation, that represents a person’s location on the map.
- [draggable](userlocationannotation/draggable.md)
  A Boolean value that indicates whether someone can drag the the user location annotation.
- [size](userlocationannotation/size.md)
  The size of the user location annotation.

## Relationships

### Inherits From
- [Annotation](annotation.md)

## See Also

- [Clustering annotations](clustering-annotations.md)
  Combine multiple annotations into a single clustered annotation.
- [class Annotation](annotation.md)
  The base annotation object for creating custom annotations.
- [class ImageAnnotation](imageannotation.md)
  A customized annotation with image resources that you provide.
- [class MarkerAnnotation](markerannotation.md)
  An annotation that displays a balloon-shaped marker at the designated location.
- [class PlaceAnnotation](placeannotation.md)
  An annotation for a place.
- [class MapFeatureAnnotation](mapfeatureannotation.md)
  An object that represents a map feature that the user selects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/userlocationannotation)*