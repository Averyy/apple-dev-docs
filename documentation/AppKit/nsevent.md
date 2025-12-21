# NSEvent

**Framework**: AppKit  
**Kind**: class

An object that contains information about an input action, such as a mouse click or a key press.

**Availability**:
- macOS ?+

## Declaration

```swift
class NSEvent
```

#### Overview

AppKit reports events that occur in a window to the app that created the window. Events include mouse clicks, key presses, and other types of input to the system. An [`NSEvent`](nsevent.md) object contains pertinent information about each event, such as the event type and when the event occurred. The event type defines what other information is available in the event object. For example, a keyboard event contains information about the pressed keys.

Although you can create [`NSEvent`](nsevent.md) objects directly, you typically don’t. The system generates them automatically in response to input from the mouse, keyboard, trackpad, or other peripherals such as connected tablets. It enqueues those events in its event queue, and dequeues them when it’s ready to process them. The system delivers events to the most relevant [`NSResponder`](nsresponder.md) object, which might be the first responder or the object where the event occurred. For example, the system delivers mouse-click events to the view that contains the event location.

To handle events, add support to your app’s [`NSResponder`](nsresponder.md) objects. You can also use gesture recognizers to handle some events for you and execute your app’s code at appropriate times. For more information, see the [`NSResponder`](nsresponder.md) reference.

You can also monitor the events your app receives and modify or cancel some events as needed. Install a local monitor using the [`addLocalMonitorForEvents(matching:handler:)`](nsevent/addlocalmonitorforevents(matching:handler:).md) method to detect specific types of events and take action when your app receives them. Install a global monitor using the [`addGlobalMonitorForEvents(matching:handler:)`](nsevent/addglobalmonitorforevents(matching:handler:).md) method to monitor events systemwide, although without the ability to modify them.

## Topics

### Creating an event object
- [class func keyEvent(with: NSEvent.EventType, location: NSPoint, modifierFlags: NSEvent.ModifierFlags, timestamp: TimeInterval, windowNumber: Int, context: NSGraphicsContext?, characters: String, charactersIgnoringModifiers: String, isARepeat: Bool, keyCode: UInt16) -> NSEvent?](nsevent/keyevent(with:location:modifierflags:timestamp:windownumber:context:characters:charactersignoringmodifiers:isarepeat:keycode:).md)
  Creates and returns a new event object that describes a key event.
- [class func mouseEvent(with: NSEvent.EventType, location: NSPoint, modifierFlags: NSEvent.ModifierFlags, timestamp: TimeInterval, windowNumber: Int, context: NSGraphicsContext?, eventNumber: Int, clickCount: Int, pressure: Float) -> NSEvent?](nsevent/mouseevent(with:location:modifierflags:timestamp:windownumber:context:eventnumber:clickcount:pressure:).md)
  Creates and returns a new event object that describes a mouse-down, -up, -moved, or -dragged event.
- [class func enterExitEvent(with: NSEvent.EventType, location: NSPoint, modifierFlags: NSEvent.ModifierFlags, timestamp: TimeInterval, windowNumber: Int, context: NSGraphicsContext?, eventNumber: Int, trackingNumber: Int, userData: UnsafeMutableRawPointer?) -> NSEvent?](nsevent/enterexitevent(with:location:modifierflags:timestamp:windownumber:context:eventnumber:trackingnumber:userdata:).md)
  Creates and returns a new event object that describes a tracking-rectangle or cursor-update event.
- [class func otherEvent(with: NSEvent.EventType, location: NSPoint, modifierFlags: NSEvent.ModifierFlags, timestamp: TimeInterval, windowNumber: Int, context: NSGraphicsContext?, subtype: Int16, data1: Int, data2: Int) -> NSEvent?](nsevent/otherevent(with:location:modifierflags:timestamp:windownumber:context:subtype:data1:data2:).md)
  Creates and returns a new event object that describes a custom event.
- [init?(eventRef: UnsafeRawPointer)](nsevent/init(eventref:).md)
  Creates and returns a new event object for a Carbon event.
- [init?(cgEvent: CGEvent)](nsevent/init(cgevent:).md)
  Creates and returns an event object for a Core Graphics event.
### Getting the event type
- [var type: NSEvent.EventType](nsevent/type.md)
  The event’s type.
- [NSEvent.EventType](nsevent/eventtype.md)
  Constants for the types of events that responder objects can handle.
- [NSEvent.EventTypeMask](nsevent/eventtypemask.md)
  Constants that you use to filter out specific event types from the stream of incoming events.
- [var subtype: NSEvent.EventSubtype](nsevent/subtype.md)
  The event’s subtype.
- [NSEvent.EventSubtype](nsevent/eventsubtype.md)
  Subtypes for various types of events.
### Getting general event information
- [var locationInWindow: NSPoint](nsevent/locationinwindow.md)
  The event location in the base coordinate system of the associated window.
- [var timestamp: TimeInterval](nsevent/timestamp.md)
  The time when the event occurred in seconds since system startup.
- [var window: NSWindow?](nsevent/window.md)
  The window object associated with the event.
- [var windowNumber: Int](nsevent/windownumber.md)
  The identifier for the window device associated with the event.
- [var eventRef: UnsafeRawPointer?](nsevent/eventref.md)
  An opaque Carbon type associated with this event.
- [var cgEvent: CGEvent?](nsevent/cgevent.md)
  The Core Graphics event object corresponding to this event.
- [class let foreverDuration: TimeInterval](nsevent/foreverduration.md)
  The longest time duration possible.
### Getting modifier flags
- [var modifierFlags: NSEvent.ModifierFlags](nsevent/modifierflags-swift.property.md)
  An integer bit field that indicates the pressed modifier keys.
- [NSEvent.ModifierFlags](nsevent/modifierflags-swift.struct.md)
  Flags that represent key states in an event object.
- [class var modifierFlags: NSEvent.ModifierFlags](nsevent/modifierflags-swift.type.property.md)
  The currently pressed modifier keys.
### Getting key event information
- [var characters: String?](nsevent/characters.md)
  The characters associated with a key-up or key-down event.
- [var charactersIgnoringModifiers: String?](nsevent/charactersignoringmodifiers.md)
  The characters generated by a key event as if no modifier key (except for Shift) applies.
- [var keyCode: UInt16](nsevent/keycode.md)
  The virtual code for the key associated with the event.
- [func characters(byApplyingModifiers: NSEvent.ModifierFlags) -> String?](nsevent/characters(byapplyingmodifiers:).md)
  Returns the new characters that result if you apply the specified modifier keys to the event.
- [class var keyRepeatDelay: TimeInterval](nsevent/keyrepeatdelay.md)
  The number of seconds someone must hold down a key before the first key repeat event occurs.
- [class var keyRepeatInterval: TimeInterval](nsevent/keyrepeatinterval.md)
  The number of seconds someone must hold down a key to generate key-repeat events after the initial delay.
- [var specialKey: NSEvent.SpecialKey?](nsevent/specialkey-swift.property.md)
  The code associated with a function key or other special key.
- [Function-Key Unicode Values](function-key-unicode-values.md)
  Constants for reserved keyboard function keys that correspond to unicode characters.
- [NSEvent.SpecialKey](nsevent/specialkey-swift.struct.md)
  Constants for reserved function keys on the keyboard.
- [var isARepeat: Bool](nsevent/isarepeat.md)
  A Boolean value that indicates whether the key event is a repeat.
### Getting mouse event information
- [class var pressedMouseButtons: Int](nsevent/pressedmousebuttons.md)
  The indices of the currently pressed mouse buttons.
- [class var doubleClickInterval: TimeInterval](nsevent/doubleclickinterval.md)
  The maximum number of seconds in which a second mouse click must occur for an event to be a double-click event.
- [class var mouseLocation: NSPoint](nsevent/mouselocation.md)
  Reports the current mouse position in screen coordinates.
- [var buttonNumber: Int](nsevent/buttonnumber.md)
  The button number for a mouse event.
- [var clickCount: Int](nsevent/clickcount.md)
  The number of mouse clicks associated with a mouse-down or mouse-up event.
- [var associatedEventsMask: NSEvent.EventTypeMask](nsevent/associatedeventsmask.md)
  The associated events mask of a mouse event.
### Getting scroll wheel and flick events
- [var deltaX: CGFloat](nsevent/deltax.md)
  The x-coordinate change for scroll wheel, mouse-move, mouse-drag, and swipe events.
- [var deltaY: CGFloat](nsevent/deltay.md)
  The y-coordinate change for scroll wheel, mouse-move, mouse-drag, and swipe events.
- [var deltaZ: CGFloat](nsevent/deltaz.md)
  The z-coordinate change for a scroll wheel, mouse-move, or mouse-drag event.
- [var hasPreciseScrollingDeltas: Bool](nsevent/hasprecisescrollingdeltas.md)
  A Boolean value that indicates whether precise scrolling deltas are available.
- [var scrollingDeltaX: CGFloat](nsevent/scrollingdeltax.md)
  The scroll wheel’s horizontal delta.
- [var scrollingDeltaY: CGFloat](nsevent/scrollingdeltay.md)
  The scroll wheel’s vertical delta.
- [var momentumPhase: NSEvent.Phase](nsevent/momentumphase.md)
  The momentum phase for a scroll or flick gesture.
- [var isDirectionInvertedFromDevice: Bool](nsevent/isdirectioninvertedfromdevice.md)
  A Boolean value that indicates whether the user has changed the device inversion.
### Configuring swipe event behaviors
- [class var isSwipeTrackingFromScrollEventsEnabled: Bool](nsevent/isswipetrackingfromscrolleventsenabled.md)
  A Boolean value that indicates whether to track fluid swipe gestures using scroll events.
- [func trackSwipeEvent(options: NSEvent.SwipeTrackingOptions, dampenAmountThresholdMin: CGFloat, max: CGFloat, usingHandler: (CGFloat, NSEvent.Phase, Bool, UnsafeMutablePointer<ObjCBool>) -> Void)](nsevent/trackswipeevent(options:dampenamountthresholdmin:max:usinghandler:).md)
  Allows tracking and user interface feedback of scroll wheel events.
- [NSEvent.SwipeTrackingOptions](nsevent/swipetrackingoptions.md)
  Constants that specify swipe-tracking options.
### Getting gesture and touch information
- [var phase: NSEvent.Phase](nsevent/phase-swift.property.md)
  The phase of a gesture event, such as a magnify, scroll, or pressure change.
- [NSEvent.Phase](nsevent/phase-swift.struct.md)
  Constants that represent the possible phases during an event phase.
- [var magnification: CGFloat](nsevent/magnification.md)
  The amount of change to add to a magnification gesture.
- [func touches(matching: NSTouch.Phase, in: NSView?) -> Set<NSTouch>](nsevent/touches(matching:in:).md)
  Returns the touch objects associated with the specified phase.
- [func allTouches() -> Set<NSTouch>](nsevent/alltouches.md)
  Returns all touch objects associated with the event.
- [func touches(for: NSView) -> Set<NSTouch>](nsevent/touches(for:).md)
  Returns the touch objects from the event that belong to the specified view.
- [func coalescedTouches(for: NSTouch) -> [NSTouch]](nsevent/coalescedtouches(for:).md)
  Returns all of the touch objects associated with the specified main touch.
- [class var isMouseCoalescingEnabled: Bool](nsevent/ismousecoalescingenabled.md)
  A Boolean value that indicates whether the system coalesces mouse movement events.
- [NSEvent.GestureAxis](nsevent/gestureaxis.md)
  Constants that specify the direction of travel for a gesture.
### Getting pressure information
- [var pressure: Float](nsevent/pressure.md)
  A normalized value that indicates the degree of pressure applied to an appropriate input device.
- [var stage: Int](nsevent/stage.md)
  A value that indicates the stage of a pressure gesture event.
- [var stageTransition: CGFloat](nsevent/stagetransition.md)
  The transition value for the stage of a pressure gesture event.
- [var pressureBehavior: NSEvent.PressureBehavior](nsevent/pressurebehavior-swift.property.md)
  The behavior and progression for a pressure event.
- [NSEvent.PressureBehavior](nsevent/pressurebehavior-swift.enum.md)
  These constants describe the behavior and progression of a pressure gesture.
### Getting tablet proximity information
- [var capabilityMask: Int](nsevent/capabilitymask.md)
  A mask that indicates the capabilities of the tablet device that generated this event.
- [var deviceID: Int](nsevent/deviceid.md)
  A special identifier the system matches against tablet-pointer and tablet-proximity events.
- [var isEnteringProximity: Bool](nsevent/isenteringproximity.md)
  A Boolean value that indicates whether a pointing device is entering or leaving the proximity of its tablet.
- [var pointingDeviceID: Int](nsevent/pointingdeviceid.md)
  The index of the pointing device currently in proximity with the tablet.
- [var pointingDeviceSerialNumber: Int](nsevent/pointingdeviceserialnumber.md)
  The vendor-assigned serial number of a pointing device.
- [var pointingDeviceType: NSEvent.PointingDeviceType](nsevent/pointingdevicetype-swift.property.md)
  The kind of pointing device associated with this event.
- [NSEvent.PointingDeviceType](nsevent/pointingdevicetype-swift.enum.md)
  The pointing-device types for tablet-proximity events or mouse events with a proximity event subtype.
- [var systemTabletID: Int](nsevent/systemtabletid.md)
  The index of the tablet device connected to the system.
- [var tabletID: Int](nsevent/tabletid.md)
  The USB model identifier of the tablet device associated with this event.
- [var uniqueID: UInt64](nsevent/uniqueid.md)
  The unique identifier of the pointing device that generated this event.
- [var vendorID: Int](nsevent/vendorid.md)
  The vendor identifier of the tablet associated with the event.
- [var vendorPointingDeviceType: Int](nsevent/vendorpointingdevicetype.md)
  A coded bit field whose set bits indicate the type of pointing device (within a vendor selection) associated with the event.
### Getting tablet pointing information
- [var absoluteX: Int](nsevent/absolutex.md)
  The absolute x coordinate of a pointing device on its tablet at full tablet resolution.
- [var absoluteY: Int](nsevent/absolutey.md)
  The absolute y coordinate of a pointing device on its tablet at full tablet resolution.
- [var absoluteZ: Int](nsevent/absolutez.md)
  The absolute z coordinate of pointing device on its tablet at full tablet resolution.
- [var buttonMask: NSEvent.ButtonMask](nsevent/buttonmask-swift.property.md)
  A bit mask identifying the buttons pressed for a tablet event.
- [NSEvent.ButtonMask](nsevent/buttonmask-swift.struct.md)
  Constants you use to identify the activated tablet buttons in an event.
- [var rotation: Float](nsevent/rotation.md)
  The rotation in degrees of the tablet pointing device associated with this event.
- [var tangentialPressure: Float](nsevent/tangentialpressure.md)
  The tangential pressure on the device that generated this event.
- [var tilt: NSPoint](nsevent/tilt.md)
  The scaled tilt values of the pointing device that generated this event.
- [var vendorDefined: Any](nsevent/vendordefined.md)
  An array of three vendor-defined number objects associated with a pointing-type event.
### Getting tracking area information
- [var eventNumber: Int](nsevent/eventnumber.md)
  The counter value of the latest mouse or tracking-rectangle event object.
- [var trackingNumber: Int](nsevent/trackingnumber.md)
  The identifier of a mouse-tracking event.
- [var trackingArea: NSTrackingArea?](nsevent/trackingarea.md)
  The tracking area for the event.
- [var userData: UnsafeMutableRawPointer?](nsevent/userdata.md)
  The data associated with a mouse-tracking event.
### Getting custom event information
- [var data1: Int](nsevent/data1.md)
  Additional data associated with this event.
- [var data2: Int](nsevent/data2.md)
  Additional data associated with this event.
### Requesting and stopping periodic events
- [class func startPeriodicEvents(afterDelay: TimeInterval, withPeriod: TimeInterval)](nsevent/startperiodicevents(afterdelay:withperiod:).md)
  Begins generating periodic events for the current thread.
- [class func stopPeriodicEvents()](nsevent/stopperiodicevents.md)
  Stops generating periodic events for the current thread and discards any periodic events remaining in the queue.
### Monitoring app events
- [class func addGlobalMonitorForEvents(matching: NSEvent.EventTypeMask, handler: (NSEvent) -> Void) -> Any?](nsevent/addglobalmonitorforevents(matching:handler:).md)
  Installs an event monitor that receives copies of events the system posts to other applications.
- [class func addLocalMonitorForEvents(matching: NSEvent.EventTypeMask, handler: (NSEvent) -> NSEvent?) -> Any?](nsevent/addlocalmonitorforevents(matching:handler:).md)
  Installs an event monitor that receives copies of events the system posts to this app prior to their dispatch.
- [class func removeMonitor(Any)](nsevent/removemonitor(_:).md)
  Removes the specified event monitor.
### Converting a mouse event’s position into a SpriteKit node’s coordinate space
- [func location(in: SKNode) -> CGPoint](nsevent/location(in:).md)
  Returns the location of the receiver in the coordinate system of the given node.
### Deprecated
- [var context: NSGraphicsContext?](nsevent/context.md)
  The display graphics context for this event.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSTouch](nstouch.md)
  A snapshot of a particular touch at an instant in time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent)*