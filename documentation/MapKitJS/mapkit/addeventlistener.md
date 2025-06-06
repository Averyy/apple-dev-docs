# addEventListener

**Framework**: MapKit JS  
**Kind**: method

Subscribes a listener function to an event type.

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

## Mentions

- [Adding interactivity to overlays](adding-interactivity-to-overlays.md)

## Parameters

- `type`: The type of event (for example,  ).
- `listener`: The callback function to invoke. MapKit JS passes   an   as its sole argument.
- `thisObject`: An object MapKit JS sets as the   keyword on the   function.

## See Also

- [Handling initialization events](handling-initialization-events.md)
  Respond to events that trigger when MapKit JS initializes.
- [init](mapkit/init.md)
  Initializes MapKit JS by providing an authorization callback function and optional language.
- [MapKitInitOptions](mapkitinitoptions.md)
  Initialization options for MapKit JS.
- [Libraries](mapkit/libraries.md)
  The list of available libraries.
- [loadedLibraries](mapkit/loadedlibraries.md)
  A string that describes the list of loaded libraries.
- [load](mapkit/load.md)
  Tells MapKit JS which libraries to load.
- [removeEventListener](mapkit/removeeventlistener.md)
  Unsubscribes a listener function from an event type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit/addeventlistener)*