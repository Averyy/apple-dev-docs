# MapAnnotationDragEvent

**Framework**: MapKit JS  
**Kind**: class

An event object that the map object dispatches when someone drags an annotation.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
class MapAnnotationDragEvent extends MapKitEvent
```

#### Discussion

The [`Map`](map.md) dispatches a [`MapAnnotationDragEvent`](mapannotationdragevent.md) when someone dragging an annotation. The event type can be `drag-start`, `dragging`, or `drag-end`.

## Topics

### Instance Properties
- [annotation](mapannotationdragevent/annotation.md)
  The annotation that a person dragged.
- [coordinate](mapannotationdragevent/coordinate.md)
  The coordinate of the annotation while someone is dragging it.

## Relationships

### Inherits From
- [MapKitEvent](mapkitevent.md)

## See Also

- [class MapEvent](mapevent.md)
  An object that represents a gesture the framework recognized on the map.
- [class MapAnnotationSelectionEvent](mapannotationselectionevent.md)
  An event object that the map object dispatches when someone selects or deselects an annotation.
- [class MapOverlaySelectionEvent](mapoverlayselectionevent.md)
  An event object that the map view dispatches when someone selects or deselects an overlay.
- [class MapUserLocationChangeEvent](mapuserlocationchangeevent.md)
  An event that represents a change in a person’s location.
- [class MapUserLocationErrorEvent](mapuserlocationerrorevent.md)
  An event that indicates that MapKit JS is unable to acquire a person’s location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapannotationdragevent)*