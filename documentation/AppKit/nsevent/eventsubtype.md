# NSEvent.EventSubtype

**Framework**: AppKit  
**Kind**: enum

Subtypes for various types of events.

**Availability**:
- macOS ?+

## Declaration

```swift
enum EventSubtype
```

#### Overview

The event subtype contains one of these constants only when the event’s [`type`](nsevent/type.md) property contains [`NSAppKitDefined`](nsappkitdefined.md), [`NSSystemDefined`](nssystemdefined.md), or [`NSApplicationDefined`](nsapplicationdefined.md) or a mouse-related event type.

## Topics

### Getting AppKit Event Subtypes
- [NSEvent.EventSubtype.applicationActivated](nsevent/eventsubtype/applicationactivated.md)
  An app-activation event occurred.
- [NSEvent.EventSubtype.applicationDeactivated](nsevent/eventsubtype/applicationdeactivated.md)
  An app-deactivation event occurred.
- [NSEvent.EventSubtype.screenChanged](nsevent/eventsubtype/screenchanged.md)
  An event that indicates a window changed screens.
- [NSEvent.EventSubtype.windowExposed](nsevent/eventsubtype/windowexposed.md)
  An event that indicates a window’s contents are visible again.
- [NSEvent.EventSubtype.windowMoved](nsevent/eventsubtype/windowmoved.md)
  An event that indicates a window moved.
### Getting System Event Subtypes
- [static var powerOff: NSEvent.EventSubtype](nsevent/eventsubtype/poweroff.md)
  An event that indicates a system shutdown or restart operation is in progress.
- [static var powerOff: NSEvent.EventSubtype](nsevent/eventsubtype/poweroff.md)
  An event that indicates a system shutdown or restart operation is in progress.
### Getting Other Subtypes
- [static var mouseEvent: NSEvent.EventSubtype](nsevent/eventsubtype/mouseevent.md)
  A mouse event occurred.
- [static var tabletPoint: NSEvent.EventSubtype](nsevent/eventsubtype/tabletpoint.md)
  A tablet-pointer event occurred.
- [static var tabletProximity: NSEvent.EventSubtype](nsevent/eventsubtype/tabletproximity.md)
  A tablet-proximity event occurred.
- [NSEvent.EventSubtype.touch](nsevent/eventsubtype/touch.md)
  A touch event occurred.
### Initializers
- [init?(rawValue: Int16)](nsevent/eventsubtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var type: NSEvent.EventType](nsevent/type.md)
  The event’s type.
- [NSEvent.EventType](nsevent/eventtype.md)
  Constants for the types of events that responder objects can handle.
- [NSEvent.EventTypeMask](nsevent/eventtypemask.md)
  Constants that you use to filter out specific event types from the stream of incoming events.
- [var subtype: NSEvent.EventSubtype](nsevent/subtype.md)
  The event’s subtype.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/eventsubtype)*