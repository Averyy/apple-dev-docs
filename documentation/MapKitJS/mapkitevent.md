# MapKitEvent

**Framework**: MapKit JS  
**Kind**: class

A generic MapKit JS event object.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
class MapKitEvent
```

#### Discussion

The event object implements similar interfaces as the DOM `Event`, but you shouldn’t mix them.

## Topics

### Instance Properties
- [defaultPrevented](mapkitevent/defaultprevented.md)
  A Boolean value that indicates whether the app canceled the event.
- [target](mapkitevent/target.md)
  The object that dispatched the event.
- [type](mapkitevent/type.md)
  A string that represents the type of the event.
### Instance Methods
- [preventDefault()](mapkitevent/preventdefault.md)
  Cancels the event if it’s cancelable, without stopping further propagation of the event.
- [stopPropagation()](mapkitevent/stoppropagation.md)
  Stops further propagation of the event.

## Relationships

### Inherited By
- [AnnotationDragEvent](annotationdragevent.md)
- [MapAnnotationDragEvent](mapannotationdragevent.md)
- [MapAnnotationSelectionEvent](mapannotationselectionevent.md)
- [MapEvent](mapevent.md)
- [MapKitConfigurationChangeEvent](mapkitconfigurationchangeevent.md)
- [MapKitConfigurationErrorEvent](mapkitconfigurationerrorevent.md)
- [MapKitLibraryLoadEvent](mapkitlibraryloadevent.md)
- [MapOverlaySelectionEvent](mapoverlayselectionevent.md)
- [MapUserLocationChangeEvent](mapuserlocationchangeevent.md)
- [MapUserLocationErrorEvent](mapuserlocationerrorevent.md)
- [TileOverlayErrorEvent](tileoverlayerrorevent.md)

## See Also

- [type MapKitEventListener](mapkiteventlistener.md)
  A type alias that represents a function or an object that receives a MapKit event.
- [class MapKitEventTarget](mapkiteventtarget.md)
  An abstract class that defines the interface for objects that can dispatch events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkitevent)*