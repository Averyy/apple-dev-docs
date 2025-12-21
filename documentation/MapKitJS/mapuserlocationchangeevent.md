# MapUserLocationChangeEvent

**Framework**: MapKit JS  
**Kind**: class

An event that represents a change in a person’s location.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
class MapUserLocationChangeEvent extends MapKitEvent
```

#### Discussion

MapKit JS sends this event when [`showsUserLocation`](map/showsuserlocation.md) is true and the map acquires a person’s location, or after an automatic update.

## Topics

### Instance Properties
- [coordinate](mapuserlocationchangeevent/coordinate.md)
  The coordinate of a person’s location.
- [floorLevel](mapuserlocationchangeevent/floorlevel.md)
  The current floor the user is on.
- [timestamp](mapuserlocationchangeevent/timestamp.md)
  The timestamp that contains the time corresponding to the location acquisition.

## Relationships

### Inherits From
- [MapKitEvent](mapkitevent.md)

## See Also

- [class MapEvent](mapevent.md)
  An object that represents a gesture the framework recognized on the map.
- [class MapAnnotationDragEvent](mapannotationdragevent.md)
  An event object that the map object dispatches when someone drags an annotation.
- [class MapAnnotationSelectionEvent](mapannotationselectionevent.md)
  An event object that the map object dispatches when someone selects or deselects an annotation.
- [class MapOverlaySelectionEvent](mapoverlayselectionevent.md)
  An event object that the map view dispatches when someone selects or deselects an overlay.
- [class MapUserLocationErrorEvent](mapuserlocationerrorevent.md)
  An event that indicates that MapKit JS is unable to acquire a person’s location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapuserlocationchangeevent)*