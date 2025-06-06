# removeEventListener

**Framework**: MapKit JS  
**Kind**: method

Removes an event listener.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
void removeEventListener(
	string type,
	function listener,
	optional Object thisObject
);
```

#### Return Value

This method doesn’t return a value.

#### Discussion

Removes `listener` as a callback for an event of `type`.

## Parameters

- `type`: The event type of interest (such as  ).
- `listener`: The callback function to remove.
- `thisObject`: An object MapKit JS sets as the   keyword on the   function.

## See Also

- [mapkit.Annotation](mapkit.annotation/mapkit.annotation.md)
  Creates a new annotation given its location and initialization options.
- [AnnotationConstructorOptions](annotationconstructoroptions.md)
  An object that contains options for creating annotation features.
- [mapkit.Annotation.CollisionMode](mapkit.annotation.collisionmode.md)
  Constants that indicate whether an annotation collides and how to interpret the collision-frame rectangle of an annotation view.
- [mapkit.Annotation.DisplayPriority](mapkit.annotation.displaypriority.md)
  Constant values that provide a hint the map uses to prioritize displaying annotations.
- [addEventListener](mapkit.annotation/addeventlistener.md)
  Adds an event listener to handle events that user interactions with annotations trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.annotation/removeeventlistener)*