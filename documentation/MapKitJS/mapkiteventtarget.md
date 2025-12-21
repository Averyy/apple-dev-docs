# MapKitEventTarget

**Framework**: MapKit JS  
**Kind**: class

An abstract class that defines the interface for objects that can dispatch events.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
class MapKitEventTarget
```

#### Discussion

[`MapKitEventTarget`](mapkiteventtarget.md) is the base class for all objects that can dispatch events. [`MapKitEventTarget`](mapkiteventtarget.md) offers an interface that’s similar to the DOM `EventTarget` interface, but with different semantics. Don’t mix them.

## Topics

### Instance Methods
- [addEventListener(eventType, listener, thisObject)](mapkiteventtarget/addeventlistener.md)
  Subscribes a listener function to an event type.
- [dispatchEvent(event)](mapkiteventtarget/dispatchevent.md)
  Dispatches an event to registered listeners.
- [removeEventListener(eventType, listener, thisObject)](mapkiteventtarget/removeeventlistener.md)
  Unsubscribes a listener function from an event type.

## Relationships

### Inherited By
- [Annotation](annotation.md)
- [Map](map.md)
- [Overlay](overlay.md)
- [TileOverlay](tileoverlay.md)
- [mapkit](mapkit.md)

## See Also

- [class MapKitEvent](mapkitevent.md)
  A generic MapKit JS event object.
- [type MapKitEventListener](mapkiteventlistener.md)
  A type alias that represents a function or an object that receives a MapKit event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkiteventtarget)*