# MapKitEventListener

**Framework**: MapKit JS  
**Kind**: typealias

A type alias that represents a function or an object that receives a MapKit event.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
type MapKitEventListener<T extends MapKitEvent = MapKitEvent> =
    | ((event: T) => void)
    | {
          handleEvent<T>(event: T): void;
      };
```

#### Discussion

You can specify the event listener as either a function or an object with a `handleEvent` method.

## See Also

- [class MapKitEvent](mapkitevent.md)
  A generic MapKit JS event object.
- [class MapKitEventTarget](mapkiteventtarget.md)
  An abstract class that defines the interface for objects that can dispatch events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkiteventlistener)*