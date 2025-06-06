# mapkit.PlaceAnnotation

**Framework**: MapKit JS  
**Kind**: init

Creates a new place annotation.

**Availability**:
- MapKit JS 5.78.1+

## Declaration

```swift
new mapkit.PlaceAnnotation(
	mapkit.Coordinate|Place location,
	optional MarkerAnnotationConstructorOptions options
);
```

#### Discussion

You’re required to provide a [`Place`](place.md) object, either by passing it as the first argument or setting [`place`](annotationconstructoroptions/place.md). If you don’t provide the required object, the call throws an error.

## Relationships

### Inherits From
- [mapkit.MapFeatureAnnotation](mapkit.mapfeatureannotation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.placeannotation/mapkit.placeannotation)*