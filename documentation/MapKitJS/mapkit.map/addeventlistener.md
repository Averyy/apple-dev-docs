# addEventListener

**Framework**: MapKit JS  
**Kind**: method

Adds an event listener to handle events that user interactions and the framework trigger.

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

[`addEventListener`](mapkit.map/addeventlistener.md) adds `listener` as a callback when an event of type `type` occurs. It throws an error if `type` is invalid. See [`Handling map events`](handling-map-events.md) for a list of event types.

The following is an example of adding an event listener for a region change:

```javascript
map.addEventListener("region-change-start", function(event) {
    console.log("Region Change Started");
});
```

## Parameters

- `type`: The event type of interest (such as “ ).
- `listener`: The callback function that MapKit invokes. MapKit JS passes   to a   event as its sole argument.
- `thisObject`: An object MapKit JS sets as the   keyword on the   function.

## See Also

- [Handling map events](handling-map-events.md)
  Register an event lister for events that a map object dispatches.
- [removeEventListener](mapkit.map/removeeventlistener.md)
  Removes an event listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.map/addeventlistener)*