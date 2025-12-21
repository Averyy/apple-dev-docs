# MapAnnotationSelectionEvent

**Framework**: MapKit JS  
**Kind**: class

An event object that the map object dispatches when someone selects or deselects an annotation.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
class MapAnnotationSelectionEvent extends MapKitEvent
```

#### Discussion

The [`Map`](map.md) dispatches a [`MapAnnotationSelectionEvent`](mapannotationselectionevent.md) when someone selects or deselects an annotation. The event type can be `select` or `deselect`.

## Topics

### Instance Properties
- [annotation](mapannotationselectionevent/annotation.md)
  The annotation that someone selected or deselected.

## Relationships

### Inherits From
- [MapKitEvent](mapkitevent.md)

## See Also

- [class MapEvent](mapevent.md)
  An object that represents a gesture the framework recognized on the map.
- [class MapAnnotationDragEvent](mapannotationdragevent.md)
  An event object that the map object dispatches when someone drags an annotation.
- [class MapOverlaySelectionEvent](mapoverlayselectionevent.md)
  An event object that the map view dispatches when someone selects or deselects an overlay.
- [class MapUserLocationChangeEvent](mapuserlocationchangeevent.md)
  An event that represents a change in a person’s location.
- [class MapUserLocationErrorEvent](mapuserlocationerrorevent.md)
  An event that indicates that MapKit JS is unable to acquire a person’s location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapannotationselectionevent)*