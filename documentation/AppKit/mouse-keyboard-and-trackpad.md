# Mouse, Keyboard, and Trackpad

**Framework**: AppKit

Handle events related to mouse, keyboard, and trackpad input.

#### Overview

The [`NSResponder`](nsresponder.md) class defines the responder chain, an ordered list of objects that respond to user events. When the user clicks the mouse button, taps on the trackpad, or presses a key, an event is generated and passed up the responder chain in search of an object that can respond to it. Any object that handles events must inherit from the [`NSResponder`](nsresponder.md) class. The core AppKit classes, [`NSApplication`](nsapplication.md), [`NSWindow`](nswindow.md), and [`NSView`](nsview.md), inherit from [`NSResponder`](nsresponder.md).

An [`NSApplication`](nsapplication.md) object maintains a list of [`NSWindow`](nswindow.md) objects—one for each window belonging to the app—and each [`NSWindow`](nswindow.md) object maintains a hierarchy of [`NSView`](nsview.md) objects. This view hierarchy is used for both drawing the user interface and for handling events.

An [`NSWindow`](nswindow.md) object handles window-level events and distributes other events to its views. An [`NSWindow`](nswindow.md) object also has a delegate allowing you to customize its behavior.

## Topics

### Responder Objects
- [class NSResponder](nsresponder.md)
  An abstract class that forms the basis of event and command processing in AppKit.
### Mouse, Keyboard, and Touch Events
- [class NSEvent](nsevent.md)
  An object that contains information about an input action, such as a mouse click or a key press.
- [class NSTouch](nstouch.md)
  A snapshot of a particular touch at an instant in time.
### Trackpad
- [class NSPressureConfiguration](nspressureconfiguration.md)
  An encapsulation of the behavior and progression of a Force Touch trackpad as it responds to specific events.
- [class NSHapticFeedbackManager](nshapticfeedbackmanager.md)
  An object that provides access to the haptic feedback management attributes on a system with a Force Touch trackpad.
### Constants
- [NSEvent.EventTypeMask](nsevent/eventtypemask.md)
  Constants that you use to filter out specific event types from the stream of incoming events.
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

## See Also

- [Menus, Cursors, and the Dock](menus-cursors-and-the-dock.md)
  Implement menus and cursors to facilitate interactions with your app, and use your app’s Dock tile to convey updated information.
- [Gestures](gestures.md)
  Encapsulate your app’s event-handling logic in gesture recognizers so that you can reuse that code throughout your app.
- [Touch Bar](touch-bar.md)
  Display interactive content and controls in the Touch Bar.
- [Drag and Drop](drag-and-drop.md)
  Support the direct manipulation of your app’s content using drag and drop.
- [Accessibility for AppKit](accessibility-for-appkit.md)
  Make your AppKit apps accessible to everyone who uses macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/mouse-keyboard-and-trackpad)*