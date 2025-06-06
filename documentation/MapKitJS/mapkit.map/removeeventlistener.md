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

This method does not return a value.

#### Discussion

[`removeEventListener`](mapkit.map/removeeventlistener.md) removes `listener` as a callback for the specified event type. See [`Handling map events`](handling-map-events.md) for a list of event types.

## Parameters

- `type`: The type of event to remove.
- `listener`: The callback function removed.
- `thisObject`: An object set as   keyword on the   function.

## See Also

- [Handling map events](handling-map-events.md)
  Register an event lister for events that a map object dispatches.
- [addEventListener](mapkit.map/addeventlistener.md)
  Adds an event listener to handle events that user interactions and the framework trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.map/removeeventlistener)*