# MapEvent

**Framework**: MapKit JS  
**Kind**: class

An object that represents a gesture the framework recognized on the map.

**Availability**:
- MapKit JS 5.18+

## Declaration

```swift
class MapEvent extends MapKitEvent
```

## Topics

### Instance Properties
- [domEvents](mapevent/domevents.md)
  An array of DOM event objects that list the low-level events that led to the recognized gesture.
- [pointOnPage](mapevent/pointonpage.md)
  A DOM point with the coordinate of the event on the page.

## Relationships

### Inherits From
- [MapKitEvent](mapkitevent.md)

## See Also

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

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapevent)*