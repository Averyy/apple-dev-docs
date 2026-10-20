# NSEvent.EventTypeMask

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants that you use to filter out specific event types from the stream of incoming events.

**Availability**:
- macOS

## Declaration

```swift
struct EventTypeMask
```

```c
enum NSEventMask : unsigned long long;
```

#### Overview

Pass these constants to the [`NSCell`](../nscell.md) method [`sendAction(on:)`](../nscell/sendaction%28on%29.md) to specify when an [`NSCell`](../nscell.md) object should send its action message.

## Topics

### Getting Any Event
- [static var any: NSEvent.EventTypeMask](./eventtypemask/any.md)
  A mask that matches any type of event.
### Getting Mouse-Related Events
- [static var leftMouseDown: NSEvent.EventTypeMask](./eventtypemask/leftmousedown.md)
  A mask for left mouse-down events.
- [static var leftMouseDragged: NSEvent.EventTypeMask](./eventtypemask/leftmousedragged.md)
  A mask for left mouse-dragged events.
- [static var leftMouseUp: NSEvent.EventTypeMask](./eventtypemask/leftmouseup.md)
  A mask for left mouse-up events.
- [static var rightMouseDown: NSEvent.EventTypeMask](./eventtypemask/rightmousedown.md)
  A mask for right mouse-down events.
- [static var rightMouseDragged: NSEvent.EventTypeMask](./eventtypemask/rightmousedragged.md)
  A mask for right mouse-dragged events.
- [static var rightMouseUp: NSEvent.EventTypeMask](./eventtypemask/rightmouseup.md)
  A mask for right mouse-up events.
- [static var otherMouseDown: NSEvent.EventTypeMask](./eventtypemask/othermousedown.md)
  A mask for tertiary mouse-down events.
- [static var otherMouseDragged: NSEvent.EventTypeMask](./eventtypemask/othermousedragged.md)
  A mask for tertiary mouse-dragged events.
- [static var otherMouseUp: NSEvent.EventTypeMask](./eventtypemask/othermouseup.md)
  A mask for tertiary mouse-up events.
- [static var mouseEntered: NSEvent.EventTypeMask](./eventtypemask/mouseentered.md)
  A mask for mouse-entered events.
- [static var mouseMoved: NSEvent.EventTypeMask](./eventtypemask/mousemoved.md)
  A mask for mouse-moved events.
- [static var mouseExited: NSEvent.EventTypeMask](./eventtypemask/mouseexited.md)
  A mask for mouse-exited events.
### Getting Keyboard Events
- [static var keyDown: NSEvent.EventTypeMask](./eventtypemask/keydown.md)
  A mask for key-down events.
- [static var keyUp: NSEvent.EventTypeMask](./eventtypemask/keyup.md)
  A mask for key-up events.
### Getting Touch Events
- [static var magnify: NSEvent.EventTypeMask](./eventtypemask/magnify.md)
  A mask for magnify-gesture events.
- [static var smartMagnify: NSEvent.EventTypeMask](./eventtypemask/smartmagnify.md)
  A mask for smart-zoom gesture events.
- [static var swipe: NSEvent.EventTypeMask](./eventtypemask/swipe.md)
  A mask for swipe-gesture events.
- [static var rotate: NSEvent.EventTypeMask](./eventtypemask/rotate.md)
  A mask for rotate-gesture events.
- [static var gesture: NSEvent.EventTypeMask](./eventtypemask/gesture.md)
  A mask for generic gesture events.
- [static var directTouch: NSEvent.EventTypeMask](./eventtypemask/directtouch.md)
  A mask for touch events.
- [static var tabletPoint: NSEvent.EventTypeMask](./eventtypemask/tabletpoint.md)
  A mask for tablet-point events.
- [static var tabletProximity: NSEvent.EventTypeMask](./eventtypemask/tabletproximity.md)
  A mask for tablet-proximity events.
- [static var pressure: NSEvent.EventTypeMask](./eventtypemask/pressure.md)
  A mask for pressure-change events.
### Getting Input Events
- [static var scrollWheel: NSEvent.EventTypeMask](./eventtypemask/scrollwheel.md)
  A mask for scroll-wheel events.
- [static var changeMode: NSEvent.EventTypeMask](./eventtypemask/changemode.md)
  A mask for change-mode events.
### Getting System Events
- [static var appKitDefined: NSEvent.EventTypeMask](./eventtypemask/appkitdefined.md)
  A mask for AppKit–defined events.
- [static var applicationDefined: NSEvent.EventTypeMask](./eventtypemask/applicationdefined.md)
  A mask for app-defined events.
- [static var cursorUpdate: NSEvent.EventTypeMask](./eventtypemask/cursorupdate.md)
  A mask for cursor-update events.
- [static var flagsChanged: NSEvent.EventTypeMask](./eventtypemask/flagschanged.md)
  A mask for flags-changed events.
- [static var periodic: NSEvent.EventTypeMask](./eventtypemask/periodic.md)
  A mask for periodic events.
- [static var systemDefined: NSEvent.EventTypeMask](./eventtypemask/systemdefined.md)
  A mask for system-defined events.
### Creating an Event Mask
- [init(rawValue: UInt64)](./eventtypemask/init%28rawvalue%29.md)
- [init(type: NSEvent.EventType)](./eventtypemask/init%28type%29.md)
  Returns the event mask for the specified type.
### Deprecated
- [Deprecated symbols](../eventtypemask-deprecated-symbols.md)
  Review symbols that are no longer in active development, and their recommended replacements.
### Type Properties
- [static var mouseCancelled: NSEvent.EventTypeMask](./eventtypemask/mousecancelled.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Constants
- [NSEvent.ButtonMask](./buttonmask-swift.struct.md)
  Constants you use to identify the activated tablet buttons in an event.
- [NSEvent.ModifierFlags](./modifierflags-swift.struct.md)
  Flags that represent key states in an event object.
- [NSEvent.Phase](./phase-swift.struct.md)
  Constants that represent the possible phases during an event phase.
- [NSEvent.SwipeTrackingOptions](./swipetrackingoptions.md)
  Constants that specify swipe-tracking options.
- [init(type: NSEvent.EventType)](./eventtypemask/init%28type%29.md)
  Returns the event mask for the specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/eventtypemask)*