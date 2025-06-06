# Handling map events

**Framework**: MapKit JS

Register an event lister for events that a map object dispatches.

#### Overview

MapKit JS uses events that developers can implement to hook into points in the life cycle of the map, as well as user interactions. Your code can respond to events by registering an event listener.

Events have a `target` property. The `target` of an event is the object dispatching that event. When you add an event listener to a map, the target is the map itself. The `select` and `deselect` events have an annotation or overlay property that reports the selected or deselected item. The `single-tap`, `double-tap`, and `long-press` events have `pointOnPage` and `domEvents` properties that provide more data about the user interactions.

Event listeners receive a single argument that is an event object. The event objects are similar to native event objects, though calls to `event.preventDefault()` or `event.stopPropagation()` don’t halt some actions that trigger these events. Scrolling, zooming, and panning, as well as zooming or rotating after a long press, provide methods to halt or prevent interaction.

##### Respond to Map Display Events

MapKit JS sends events that allow you to respond to changes in the map display and a person’s interactions with the map and its controls.

##### Respond to Annotation and Overlay Events

MapKit JS sends these events when a person’s interacts with the annotations and overlays you place on the map, use these to respond to these interactions by updating the map, or providing more informationation about the overlay or annotation the person interacts with.

##### Respond to User Location Events

MapKit JS sends these events that indicate changes in a person’s location. Use these events to adjust what the map displays or to trigger other responses in your app.

Because this feature implements the geolocation API for HTML 5, the error codes mirror that API’s error codes with one additional MapKit JS-specific error code:

`Error.PERMISSION_DENIED (1)` — The user refuses permission to obtain location information.

`Error.POSITION_UNAVAILABLE (2)` — The geolocation API returns an error.

`Error.TIMEOUT (3)` — The operation times out without acquiring the location.

`Error.MAPKIT_NOT_INITIALIZED (4)` — The system hasn’t initialized MapKit JS.

##### Respond to Map Interaction Events

MapKit JS sends these events when a person taps or presses on the map view. Use these events to adjust the map view, respond to the deselecting of overlays, or dragging or deselecting annotations.

The event object that map interaction events return has the following two properties:

## See Also

- [addEventListener](mapkit.map/addeventlistener.md)
  Adds an event listener to handle events that user interactions and the framework trigger.
- [removeEventListener](mapkit.map/removeeventlistener.md)
  Removes an event listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/handling-map-events)*