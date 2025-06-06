# mapkit.Annotation

**Framework**: MapKit JS  
**Kind**: init

Creates a new annotation given its location and initialization options.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
new mapkit.Annotation(
	mapkit.Coordinate|Place location,
	function factory,
	optional AnnotationConstructorOptions options
);
```

#### Return Value

A [`mapkit.Annotation`](mapkit.annotation/mapkit.annotation.md) instance.

#### Discussion

The `factory` function returns a DOM element to represent the annotation. It can be a single element or a containing element with subelements. MapKit JS calls this function with the following two arguments:

- `coordinate` ([`mapkit.Coordinate`](mapkit.coordinate.md)) — The annotation’s coordinate.
- `options` ([`AnnotationConstructorOptions`](annotationconstructoroptions.md)) — You can use options you pass to the annotation constructor to add context to the custom annotation.

The `options` include `title` and `subtitle`, which appear in a callout if they’re present.

## Parameters

- `location`: The coordinate where the annotation appears.
- `factory`: A factory function that returns a DOM element that represents the annotation.
- `options`: A hash of properties MapKit JS uses to initialize the annotation.

## Relationships

### Inherits From
- [mapkit.ImageAnnotation](mapkit.imageannotation.md)
- [mapkit.MarkerAnnotation](mapkit.markerannotation.md)

## See Also

- [AnnotationConstructorOptions](annotationconstructoroptions.md)
  An object that contains options for creating annotation features.
- [mapkit.Annotation.CollisionMode](mapkit.annotation.collisionmode.md)
  Constants that indicate whether an annotation collides and how to interpret the collision-frame rectangle of an annotation view.
- [mapkit.Annotation.DisplayPriority](mapkit.annotation.displaypriority.md)
  Constant values that provide a hint the map uses to prioritize displaying annotations.
- [addEventListener](mapkit.annotation/addeventlistener.md)
  Adds an event listener to handle events that user interactions with annotations trigger.
- [removeEventListener](mapkit.annotation/removeeventlistener.md)
  Removes an event listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.annotation/mapkit.annotation)*