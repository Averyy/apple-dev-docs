# Handling map events

**Framework**: MapKit JS

Register an event lister for events that a map object dispatches.

#### Overview

MapKit JS uses events that developers can implement to hook into points in the life cycle of the map, as well as user interactions. Your code can respond to events by registering an event listener.

Events have a `target` property. The `target` of an event is the object dispatching that event. When you add an event listener to a map, the target is the map itself. The `select` and `deselect` events have an annotation or overlay property that reports the selected or deselected item. The `single-tap`, `double-tap`, and `long-press` events have `pointOnPage` and `domEvents` properties that provide more data about the user interactions.

Event listeners receive a single argument that is an event object. The event objects are similar to native event objects, though calls to `event.preventDefault()` or `event.stopPropagation()` don’t halt some actions that trigger these events. Scrolling, zooming, and panning, as well as zooming or rotating after a long press, provide methods to halt or prevent interaction.

##### Respond to Map Display Events

MapKit JS sends the following [`MapKitEvent`](mapkitevent.md) events that allow you to respond to changes in the map display and a person’s interactions with the map and its controls.

##### Respond to Annotation and Overlay Events

MapKit JS sends [`MapAnnotationSelectionEvent`](mapannotationselectionevent.md),[`MapOverlaySelectionEvent`](mapoverlayselectionevent.md), and [`MapAnnotationDragEvent`](mapannotationdragevent.md) events when a person interacts with the annotations and overlays you place on the map. Respond to these interactions by updating the map or providing more information about the overlay or annotation the person interacts with.

##### Respond to User Location Events

MapKit JS sends [`MapUserLocationChangeEvent`](mapuserlocationchangeevent.md) or [`MapUserLocationErrorEvent`](mapuserlocationerrorevent.md) events to indicate changes in a person’s location. Use these events to adjust what the map displays or to trigger other responses in your app.

##### Respond to Map Interaction Events

MapKit JS sends [`MapEvent`](mapevent.md) events when someone taps or presses on the map view. Use these events to adjust the map view, respond to the deselecting of overlays, or drag or deselect annotations.

## Topics

### Map events
- [class MapEvent](mapevent.md)
  An object that represents a gesture the framework recognized on the map.
- [class MapAnnotationDragEvent](mapannotationdragevent.md)
  An event object that the map object dispatches when someone drags an annotation.
- [class MapAnnotationSelectionEvent](mapannotationselectionevent.md)
  An event object that the map object dispatches when someone selects or deselects an annotation.
- [class MapOverlaySelectionEvent](mapoverlayselectionevent.md)
  An event object that the map view dispatches when someone selects or deselects an overlay.
- [class MapUserLocationChangeEvent](mapuserlocationchangeevent.md)
  An event that represents a change in a person’s location.
- [class MapUserLocationErrorEvent](mapuserlocationerrorevent.md)
  An event that indicates that MapKit JS is unable to acquire a person’s location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/handling-map-events)*