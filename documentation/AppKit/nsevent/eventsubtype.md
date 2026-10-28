# NSEvent.EventSubtype

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Subtypes for various types of events.

**Availability**:
- macOS

## Declaration

```swift
enum EventSubtype
```

```c
enum NSEventSubtype : short;
```

## Overview

The event subtype contains one of these constants only when the event’s [`type`](./type.md) property contains [`NSAppKitDefined`](../nsappkitdefined.md), [`NSSystemDefined`](../nssystemdefined.md), or [`NSApplicationDefined`](../nsapplicationdefined.md) or a mouse-related event type.

## Topics

### Getting AppKit Event Subtypes
- [NSEvent.EventSubtype.applicationActivated](./eventsubtype/applicationactivated.md)
  An app-activation event occurred.
- [NSEvent.EventSubtype.applicationDeactivated](./eventsubtype/applicationdeactivated.md)
  An app-deactivation event occurred.
- [NSEvent.EventSubtype.screenChanged](./eventsubtype/screenchanged.md)
  An event that indicates a window changed screens.
- [NSEvent.EventSubtype.windowExposed](./eventsubtype/windowexposed.md)
  An event that indicates a window’s contents are visible again.
- [NSEvent.EventSubtype.windowMoved](./eventsubtype/windowmoved.md)
  An event that indicates a window moved.
### Getting System Event Subtypes
- [static var powerOff: NSEvent.EventSubtype](./eventsubtype/poweroff.md)
  An event that indicates a system shutdown or restart operation is in progress.
- [static var powerOff: NSEvent.EventSubtype](./eventsubtype/poweroff.md)
  An event that indicates a system shutdown or restart operation is in progress.
### Getting Other Subtypes
- [static var mouseEvent: NSEvent.EventSubtype](./eventsubtype/mouseevent.md)
  A mouse event occurred.
- [static var tabletPoint: NSEvent.EventSubtype](./eventsubtype/tabletpoint.md)
  A tablet-pointer event occurred.
- [static var tabletProximity: NSEvent.EventSubtype](./eventsubtype/tabletproximity.md)
  A tablet-proximity event occurred.
- [NSEvent.EventSubtype.touch](./eventsubtype/touch.md)
  A touch event occurred.
### Deprecated
- [Deprecated symbols](../eventsubtype-deprecated-symbols.md)
  Review symbols that are no longer in active development, and their recommended replacements.
### Initializers
- [init?(rawValue: Int16)](./eventsubtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the event type
- [var type: NSEvent.EventType](./type.md)
  The event’s type.
- [NSEvent.EventType](./eventtype.md)
  Constants for the types of events that responder objects can handle.
- [NSEvent.EventTypeMask](./eventtypemask.md)
  Constants that you use to filter out specific event types from the stream of incoming events.
- [var subtype: NSEvent.EventSubtype](./subtype.md)
  The event’s subtype.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/eventsubtype)*