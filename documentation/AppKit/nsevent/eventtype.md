# NSEvent.EventType

**Framework**: AppKit  
**Kind**: enum

Constants for the types of events that responder objects can handle.

**Availability**:
- macOS ?+

## Declaration

```swift
enum EventType
```

#### Overview

These constants appear in the event’s [`type`](nsevent/type.md) property. You also use them when you construct new events.

## Topics

### Getting Mouse-Related Event Types
- [NSEvent.EventType.leftMouseDown](nsevent/eventtype/leftmousedown.md)
  The user pressed the left mouse button.
- [NSEvent.EventType.leftMouseDragged](nsevent/eventtype/leftmousedragged.md)
  The user moved the mouse while holding down the left mouse button.
- [NSEvent.EventType.leftMouseUp](nsevent/eventtype/leftmouseup.md)
  The user released the left mouse button.
- [NSEvent.EventType.rightMouseDown](nsevent/eventtype/rightmousedown.md)
  The user pressed the right mouse button.
- [NSEvent.EventType.rightMouseUp](nsevent/eventtype/rightmouseup.md)
  The user released the right mouse button.
- [NSEvent.EventType.rightMouseDragged](nsevent/eventtype/rightmousedragged.md)
  The user moved the mouse while holding down the right mouse button.
- [NSEvent.EventType.otherMouseDown](nsevent/eventtype/othermousedown.md)
  The user pressed a tertiary mouse button.
- [NSEvent.EventType.otherMouseDragged](nsevent/eventtype/othermousedragged.md)
  The user moved the mouse while holding down a tertiary mouse button.
- [NSEvent.EventType.otherMouseUp](nsevent/eventtype/othermouseup.md)
  The user released a tertiary mouse button.
- [NSEvent.EventType.mouseMoved](nsevent/eventtype/mousemoved.md)
  The user moved the mouse in a way that caused the cursor to move onscreen.
- [NSEvent.EventType.mouseEntered](nsevent/eventtype/mouseentered.md)
  The cursor entered a well-defined area, such as a view.
- [NSEvent.EventType.mouseExited](nsevent/eventtype/mouseexited.md)
  The cursor exited a well-defined area, such as a view.
### Getting Keyboard Event Types
- [NSEvent.EventType.keyDown](nsevent/eventtype/keydown.md)
  The user pressed a key on the keyboard.
- [NSEvent.EventType.keyUp](nsevent/eventtype/keyup.md)
  The user released a key on the keyboard.
### Getting Touch-Based Events
- [NSEvent.EventType.beginGesture](nsevent/eventtype/begingesture.md)
  An event marking the beginning of a gesture.
- [NSEvent.EventType.endGesture](nsevent/eventtype/endgesture.md)
  An event that marks the end of a gesture.
- [NSEvent.EventType.magnify](nsevent/eventtype/magnify.md)
  The user performed a pinch-open or pinch-close gesture.
- [NSEvent.EventType.smartMagnify](nsevent/eventtype/smartmagnify.md)
  The user performed a smart-zoom gesture.
- [NSEvent.EventType.swipe](nsevent/eventtype/swipe.md)
  The user performed a swipe gesture.
- [NSEvent.EventType.rotate](nsevent/eventtype/rotate.md)
  The user performed a rotate gesture.
- [NSEvent.EventType.gesture](nsevent/eventtype/gesture.md)
  The user performed a nonspecific type of gesture.
- [NSEvent.EventType.directTouch](nsevent/eventtype/directtouch.md)
  The user touched a portion of the touch bar.
- [NSEvent.EventType.tabletPoint](nsevent/eventtype/tabletpoint.md)
  The user touched a point on a tablet.
- [NSEvent.EventType.tabletProximity](nsevent/eventtype/tabletproximity.md)
  A pointing device is near, but not touching, the associated tablet.
- [NSEvent.EventType.pressure](nsevent/eventtype/pressure.md)
  An event that reports a change in pressure on a pressure-sensitive device.
### Getting Other Input Types
- [NSEvent.EventType.scrollWheel](nsevent/eventtype/scrollwheel.md)
  The scroll wheel position changed.
- [NSEvent.EventType.changeMode](nsevent/eventtype/changemode.md)
  The user changed the mode of a connected device.
### Getting System Event Types
- [NSEvent.EventType.appKitDefined](nsevent/eventtype/appkitdefined.md)
  An AppKit-related event occurred.
- [NSEvent.EventType.applicationDefined](nsevent/eventtype/applicationdefined.md)
  An app-defined event occurred.
- [NSEvent.EventType.cursorUpdate](nsevent/eventtype/cursorupdate.md)
  An event that updates the cursor.
- [NSEvent.EventType.flagsChanged](nsevent/eventtype/flagschanged.md)
  The event flags changed.
- [NSEvent.EventType.periodic](nsevent/eventtype/periodic.md)
  An event that provides execution time to periodic tasks.
- [NSEvent.EventType.quickLook](nsevent/eventtype/quicklook.md)
  An event that initiates a Quick Look request.
- [NSEvent.EventType.systemDefined](nsevent/eventtype/systemdefined.md)
  A system-related event occurred.
### Enumeration Cases
- [NSEvent.EventType.mouseCancelled](nsevent/eventtype/mousecancelled.md)
### Initializers
- [init?(rawValue: UInt)](nsevent/eventtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var type: NSEvent.EventType](nsevent/type.md)
  The event’s type.
- [NSEvent.EventTypeMask](nsevent/eventtypemask.md)
  Constants that you use to filter out specific event types from the stream of incoming events.
- [var subtype: NSEvent.EventSubtype](nsevent/subtype.md)
  The event’s subtype.
- [NSEvent.EventSubtype](nsevent/eventsubtype.md)
  Subtypes for various types of events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/eventtype)*