# mapkit.Annotation.CollisionMode

**Framework**: MapKit JS  
**Kind**: enum

Constants that indicate whether an annotation collides and how to interpret the collision-frame rectangle of an annotation view.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
interface mapkit.Annotation.CollisionMode {
	const string Rectangle;
	const string Circle;
	const String None;
};
```

## Topics

### Collision modes
- [Rectangle](mapkit.annotation.collisionmode/rectangle.md)
  A constant indicating that the map should use a full collision rectangle for detecting collisions.
- [Circle](mapkit.annotation.collisionmode/circle.md)
  A constant indicating that the map should use a circle inscribed in the collision frame rectangle to determine collisions.
- [None](mapkit.annotation.collisionmode/none.md)
  A constant that indicates the annotation doesn’t collide with other annotations.

## See Also

- [Clustering annotations](clustering-annotations.md)
  Combine multiple annotations into a single clustered annotation.
- [mapkit.Annotation](mapkit.annotation.md)
  The base annotation object for creating custom annotations.
- [AnnotationCalloutDelegate](annotationcalloutdelegate.md)
  Methods for customizing the behavior and appearance of an annotation callout.
- [mapkit.PlaceAnnotation](mapkit.placeannotation.md)
  An annotation for a place.
- [mapkit.MapFeatureAnnotation](mapkit.mapfeatureannotation.md)
  An object that represents a map feature that the user selects.
- [mapkit.Annotation.DisplayPriority](mapkit.annotation.displaypriority.md)
  Constant values that provide a hint the map uses to prioritize displaying annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.annotation.collisionmode)*