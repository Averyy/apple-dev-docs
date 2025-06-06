# NSEvent.EventTypeMask

**Framework**: AppKit  
**Kind**: struct

Constants that you use to filter out specific event types from the stream of incoming events.

**Availability**:
- macOS ?+

## Declaration

```swift
struct EventTypeMask
```

#### Overview

Pass these constants to the [`NSCell`](nscell.md) method [`sendAction(on:)`](nscell/sendaction(on:).md) to specify when an [`NSCell`](nscell.md) object should send its action message.

## Topics

### Getting Any Event
- [static var any: NSEvent.EventTypeMask](nsevent/eventtypemask/any.md)
  A mask that matches any type of event.
### Getting Mouse-Related Events
- [static var leftMouseDown: NSEvent.EventTypeMask](nsevent/eventtypemask/leftmousedown.md)
  A mask for left mouse-down events.
- [static var leftMouseDragged: NSEvent.EventTypeMask](nsevent/eventtypemask/leftmousedragged.md)
  A mask for left mouse-dragged events.
- [static var leftMouseUp: NSEvent.EventTypeMask](nsevent/eventtypemask/leftmouseup.md)
  A mask for left mouse-up events.
- [static var rightMouseDown: NSEvent.EventTypeMask](nsevent/eventtypemask/rightmousedown.md)
  A mask for right mouse-down events.
- [static var rightMouseDragged: NSEvent.EventTypeMask](nsevent/eventtypemask/rightmousedragged.md)
  A mask for right mouse-dragged events.
- [static var rightMouseUp: NSEvent.EventTypeMask](nsevent/eventtypemask/rightmouseup.md)
  A mask for right mouse-up events.
- [static var otherMouseDown: NSEvent.EventTypeMask](nsevent/eventtypemask/othermousedown.md)
  A mask for tertiary mouse-down events.
- [static var otherMouseDragged: NSEvent.EventTypeMask](nsevent/eventtypemask/othermousedragged.md)
  A mask for tertiary mouse-dragged events.
- [static var otherMouseUp: NSEvent.EventTypeMask](nsevent/eventtypemask/othermouseup.md)
  A mask for tertiary mouse-up events.
- [static var mouseEntered: NSEvent.EventTypeMask](nsevent/eventtypemask/mouseentered.md)
  A mask for mouse-entered events.
- [static var mouseMoved: NSEvent.EventTypeMask](nsevent/eventtypemask/mousemoved.md)
  A mask for mouse-moved events.
- [static var mouseExited: NSEvent.EventTypeMask](nsevent/eventtypemask/mouseexited.md)
  A mask for mouse-exited events.
### Getting Keyboard Events
- [static var keyDown: NSEvent.EventTypeMask](nsevent/eventtypemask/keydown.md)
  A mask for key-down events.
- [static var keyUp: NSEvent.EventTypeMask](nsevent/eventtypemask/keyup.md)
  A mask for key-up events.
### Getting Touch Events
- [static var beginGesture: NSEvent.EventTypeMask](nsevent/eventtypemask/begingesture.md)
  A mask for begin-gesture events.
- [static var endGesture: NSEvent.EventTypeMask](nsevent/eventtypemask/endgesture.md)
  A mask for end-gesture events.
- [static var magnify: NSEvent.EventTypeMask](nsevent/eventtypemask/magnify.md)
  A mask for magnify-gesture events.
- [static var smartMagnify: NSEvent.EventTypeMask](nsevent/eventtypemask/smartmagnify.md)
  A mask for smart-zoom gesture events.
- [static var swipe: NSEvent.EventTypeMask](nsevent/eventtypemask/swipe.md)
  A mask for swipe-gesture events.
- [static var rotate: NSEvent.EventTypeMask](nsevent/eventtypemask/rotate.md)
  A mask for rotate-gesture events.
- [static var gesture: NSEvent.EventTypeMask](nsevent/eventtypemask/gesture.md)
  A mask for generic gesture events.
- [static var directTouch: NSEvent.EventTypeMask](nsevent/eventtypemask/directtouch.md)
  A mask for touch events.
- [static var tabletPoint: NSEvent.EventTypeMask](nsevent/eventtypemask/tabletpoint.md)
  A mask for tablet-point events.
- [static var tabletProximity: NSEvent.EventTypeMask](nsevent/eventtypemask/tabletproximity.md)
  A mask for tablet-proximity events.
- [static var pressure: NSEvent.EventTypeMask](nsevent/eventtypemask/pressure.md)
  A mask for pressure-change events.
### Getting Input Events
- [static var scrollWheel: NSEvent.EventTypeMask](nsevent/eventtypemask/scrollwheel.md)
  A mask for scroll-wheel events.
- [static var changeMode: NSEvent.EventTypeMask](nsevent/eventtypemask/changemode.md)
  A mask for change-mode events.
### Getting System Events
- [static var appKitDefined: NSEvent.EventTypeMask](nsevent/eventtypemask/appkitdefined.md)
  A mask for AppKit–defined events.
- [static var applicationDefined: NSEvent.EventTypeMask](nsevent/eventtypemask/applicationdefined.md)
  A mask for app-defined events.
- [static var cursorUpdate: NSEvent.EventTypeMask](nsevent/eventtypemask/cursorupdate.md)
  A mask for cursor-update events.
- [static var flagsChanged: NSEvent.EventTypeMask](nsevent/eventtypemask/flagschanged.md)
  A mask for flags-changed events.
- [static var periodic: NSEvent.EventTypeMask](nsevent/eventtypemask/periodic.md)
  A mask for periodic events.
- [static var systemDefined: NSEvent.EventTypeMask](nsevent/eventtypemask/systemdefined.md)
  A mask for system-defined events.
### Creating an Event Mask
- [init(rawValue: UInt64)](nsevent/eventtypemask/init(rawvalue:).md)
- [init(type: NSEvent.EventType)](nsevent/eventtypemask/init(type:).md)
  Returns the event mask for the specified type.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [NSEvent.ButtonMask](nsevent/buttonmask-swift.struct.md)
  Constants you use to identify the activated tablet buttons in an event.
- [NSEvent.ModifierFlags](nsevent/modifierflags-swift.struct.md)
  Flags that represent key states in an event object.
- [NSEvent.Phase](nsevent/phase-swift.struct.md)
  Constants that represent the possible phases during an event phase.
- [NSEvent.SwipeTrackingOptions](nsevent/swipetrackingoptions.md)
  Constants that specify swipe-tracking options.
- [init(type: NSEvent.EventType)](nsevent/eventtypemask/init(type:).md)
  Returns the event mask for the specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/eventtypemask)*