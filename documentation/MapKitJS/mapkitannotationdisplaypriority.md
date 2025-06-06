# mapkit.Annotation.DisplayPriority

**Framework**: MapKit JS  
**Kind**: enum

Constant values that provide a hint the map uses to prioritize displaying annotations.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
interface mapkit.Annotation.DisplayPriority {
	const number Low;
	const number High;
	const number Required;
};
```

## Topics

### Display priority values
- [High](mapkit.annotation.displaypriority/high.md)
  A high display priority, with a preset value of 750 out of 1000.
- [Low](mapkit.annotation.displaypriority/low.md)
  A low display priority, with a preset value of 250 out of 1000.
- [Required](mapkit.annotation.displaypriority/required.md)
  The highest display priority, with a preset value of 1000 out of 1000.

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
- [mapkit.Annotation.CollisionMode](mapkit.annotation.collisionmode.md)
  Constants that indicate whether an annotation collides and how to interpret the collision-frame rectangle of an annotation view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.annotation.displaypriority)*