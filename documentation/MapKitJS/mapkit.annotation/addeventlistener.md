# addEventListener

**Framework**: MapKit JS  
**Kind**: method

Adds an event listener to handle events that user interactions with annotations trigger.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
void addEventListener(
	string type,
	function listener,
	optional Object thisObject
);
```

#### Return Value

This method doesn’t return a value.

#### Discussion

Adds `listener` as a callback for an event of type `type`. Throws an error if `type` is invalid.

## Parameters

- `type`: The event type of interest (such as  ).
- `listener`: The callback function to invoke. MapKit JS passes   an annotation event as its sole argument.
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
- [removeEventListener](mapkit.annotation/removeeventlistener.md)
  Removes an event listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.annotation/addeventlistener)*