# NSEvent.EventType

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants for the types of events that responder objects can handle.

**Availability**:
- macOS

## Declaration

```swift
enum EventType
```

```c
enum NSEventType : NSUInteger;
```

#### Overview

These constants appear in the event’s [`type`](./type.md) property. You also use them when you construct new events.

## Topics

### Getting Mouse-Related Event Types
- [NSEvent.EventType.leftMouseDown](./eventtype/leftmousedown.md)
  The user pressed the left mouse button.
- [NSEvent.EventType.leftMouseDragged](./eventtype/leftmousedragged.md)
  The user moved the mouse while holding down the left mouse button.
- [NSEvent.EventType.leftMouseUp](./eventtype/leftmouseup.md)
  The user released the left mouse button.
- [NSEvent.EventType.rightMouseDown](./eventtype/rightmousedown.md)
  The user pressed the right mouse button.
- [NSEvent.EventType.rightMouseUp](./eventtype/rightmouseup.md)
  The user released the right mouse button.
- [NSEvent.EventType.rightMouseDragged](./eventtype/rightmousedragged.md)
  The user moved the mouse while holding down the right mouse button.
- [NSEvent.EventType.otherMouseDown](./eventtype/othermousedown.md)
  The user pressed a tertiary mouse button.
- [NSEvent.EventType.otherMouseDragged](./eventtype/othermousedragged.md)
  The user moved the mouse while holding down a tertiary mouse button.
- [NSEvent.EventType.otherMouseUp](./eventtype/othermouseup.md)
  The user released a tertiary mouse button.
- [NSEvent.EventType.mouseMoved](./eventtype/mousemoved.md)
  The user moved the mouse in a way that caused the cursor to move onscreen.
- [NSEvent.EventType.mouseEntered](./eventtype/mouseentered.md)
  The cursor entered a well-defined area, such as a view.
- [NSEvent.EventType.mouseExited](./eventtype/mouseexited.md)
  The cursor exited a well-defined area, such as a view.
### Getting Keyboard Event Types
- [NSEvent.EventType.keyDown](./eventtype/keydown.md)
  The user pressed a key on the keyboard.
- [NSEvent.EventType.keyUp](./eventtype/keyup.md)
  The user released a key on the keyboard.
### Getting Touch-Based Events
- [NSEvent.EventType.magnify](./eventtype/magnify.md)
  The user performed a pinch-open or pinch-close gesture.
- [NSEvent.EventType.smartMagnify](./eventtype/smartmagnify.md)
  The user performed a smart-zoom gesture.
- [NSEvent.EventType.swipe](./eventtype/swipe.md)
  The user performed a swipe gesture.
- [NSEvent.EventType.rotate](./eventtype/rotate.md)
  The user performed a rotate gesture.
- [NSEvent.EventType.gesture](./eventtype/gesture.md)
  The user performed a nonspecific type of gesture.
- [NSEvent.EventType.directTouch](./eventtype/directtouch.md)
  The user touched a portion of the touch bar.
- [NSEvent.EventType.tabletPoint](./eventtype/tabletpoint.md)
  The user touched a point on a tablet.
- [NSEvent.EventType.tabletProximity](./eventtype/tabletproximity.md)
  A pointing device is near, but not touching, the associated tablet.
- [NSEvent.EventType.pressure](./eventtype/pressure.md)
  An event that reports a change in pressure on a pressure-sensitive device.
### Getting Other Input Types
- [NSEvent.EventType.scrollWheel](./eventtype/scrollwheel.md)
  The scroll wheel position changed.
- [NSEvent.EventType.changeMode](./eventtype/changemode.md)
  The user changed the mode of a connected device.
### Getting System Event Types
- [NSEvent.EventType.appKitDefined](./eventtype/appkitdefined.md)
  An AppKit-related event occurred.
- [NSEvent.EventType.applicationDefined](./eventtype/applicationdefined.md)
  An app-defined event occurred.
- [NSEvent.EventType.cursorUpdate](./eventtype/cursorupdate.md)
  An event that updates the cursor.
- [NSEvent.EventType.flagsChanged](./eventtype/flagschanged.md)
  The event flags changed.
- [NSEvent.EventType.periodic](./eventtype/periodic.md)
  An event that provides execution time to periodic tasks.
- [NSEvent.EventType.quickLook](./eventtype/quicklook.md)
  An event that initiates a Quick Look request.
- [NSEvent.EventType.systemDefined](./eventtype/systemdefined.md)
  A system-related event occurred.
### Deprecated
- [Deprecated symbols](../eventtype-deprecated-symbols.md)
  Review symbols that are no longer in active development, and their recommended replacements.
### Enumeration Cases
- [NSEvent.EventType.mouseCancelled](./eventtype/mousecancelled.md)
### Initializers
- [init?(rawValue: UInt)](./eventtype/init%28rawvalue%29.md)

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
- [NSEvent.EventTypeMask](./eventtypemask.md)
  Constants that you use to filter out specific event types from the stream of incoming events.
- [var subtype: NSEvent.EventSubtype](./subtype.md)
  The event’s subtype.
- [NSEvent.EventSubtype](./eventsubtype.md)
  Subtypes for various types of events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/eventtype)*