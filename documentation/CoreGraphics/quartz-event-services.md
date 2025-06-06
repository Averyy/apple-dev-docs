# Quartz Event Services

**Framework**: Core Graphics

Provides features for managing —filters for observing and altering the stream of low-level user input events in macOS.

#### Overview

Event taps make it possible to monitor and filter input events from several points within the system, prior to their delivery to a foreground application. Event taps complement and extend the capabilities of the Carbon event monitor mechanism, which allows an application to observe input events delivered to other processes.

Event taps are designed to serve as a Section 508 enabling technology. For example, consider a software system to assist a person with language impairments, designed to perform keyboard filtering with spoken review. Such a system could use an event tap to monitor all keystrokes, perform dictionary checks and matches, and recite the assembled word back to the user on detection of a word break in the input stream. If acceptable to the user, as indicated by an additional input keystroke or other gesture, the events would be posted into the system for delivery to the foreground application.

Introduced in OS X version 10.4, event taps provide functionality similar to the Win32 functions `SetWinEventHook` when used to establish an out-of-context event hook, and `SendInput`. Quartz Event Services also includes an older set of event-related functions declared in the file `CGRemoteOperation.h`. These functions are still supported, but they are not recommended for new development.

## Topics

### Working With Events
- [class var typeID: CFTypeID](cgevent/typeid.md)
  Returns the type identifier for the opaque type `CGEventRef`.
- [init?(source: CGEventSource?)](cgevent/init(source:).md)
  Returns a new Quartz event.
- [init?(withDataAllocator: CFAllocator?, data: CFData?)](cgevent/init(withdataallocator:data:).md)
  Returns a Quartz event created from a flattened data representation of the event.
- [init?(mouseEventSource: CGEventSource?, mouseType: CGEventType, mouseCursorPosition: CGPoint, mouseButton: CGMouseButton)](cgevent/init(mouseeventsource:mousetype:mousecursorposition:mousebutton:).md)
  Returns a new Quartz mouse event.
- [init?(keyboardEventSource: CGEventSource?, virtualKey: CGKeyCode, keyDown: Bool)](cgevent/init(keyboardeventsource:virtualkey:keydown:).md)
  Returns a new Quartz keyboard event.
- [func copy() -> CGEvent?](cgevent/copy.md)
  Returns a copy of an existing Quartz event.
- [init?(event: CGEvent?)](cgeventsource/init(event:).md)
  Returns a Quartz event source created from an existing Quartz event.
- [func setSource(CGEventSource?)](cgevent/setsource(_:).md)
  Sets the event source of a Quartz event.
- [var type: CGEventType](cgevent/type.md)
  Returns the event type of a Quartz event (left mouse down, for example).
- [var timestamp: CGEventTimestamp](cgevent/timestamp.md)
  Returns the timestamp of a Quartz event.
- [var location: CGPoint](cgevent/location.md)
  Returns the location of a Quartz mouse event.
- [var unflippedLocation: CGPoint](cgevent/unflippedlocation.md)
  Returns the location of a Quartz mouse event.
- [var flags: CGEventFlags](cgevent/flags.md)
  Returns the event flags of a Quartz event.
- [func keyboardGetUnicodeString(maxStringLength: Int, actualStringLength: UnsafeMutablePointer<Int>?, unicodeString: UnsafeMutablePointer<UniChar>?)](cgevent/keyboardgetunicodestring(maxstringlength:actualstringlength:unicodestring:).md)
  Returns the Unicode string associated with a Quartz keyboard event.
- [func keyboardSetUnicodeString(stringLength: Int, unicodeString: UnsafePointer<UniChar>?)](cgevent/keyboardsetunicodestring(stringlength:unicodestring:).md)
  Sets the Unicode string associated with a Quartz keyboard event.
- [func getIntegerValueField(CGEventField) -> Int64](cgevent/getintegervaluefield(_:).md)
  Returns the integer value of a field in a Quartz event.
- [func setIntegerValueField(CGEventField, value: Int64)](cgevent/setintegervaluefield(_:value:).md)
  Sets the integer value of a field in a Quartz event.
- [func getDoubleValueField(CGEventField) -> Double](cgevent/getdoublevaluefield(_:).md)
  Returns the floating-point value of a field in a Quartz event.
- [func setDoubleValueField(CGEventField, value: Double)](cgevent/setdoublevaluefield(_:value:).md)
  Sets the floating-point value of a field in a Quartz event.
### Working With Event Taps
- [class func tapCreate(tap: CGEventTapLocation, place: CGEventTapPlacement, options: CGEventTapOptions, eventsOfInterest: CGEventMask, callback: CGEventTapCallBack, userInfo: UnsafeMutableRawPointer?) -> CFMachPort?](cgevent/tapcreate(tap:place:options:eventsofinterest:callback:userinfo:).md)
  Creates an event tap.
- [class func tapCreateForPSN(processSerialNumber: UnsafeMutableRawPointer, place: CGEventTapPlacement, options: CGEventTapOptions, eventsOfInterest: CGEventMask, callback: CGEventTapCallBack, userInfo: UnsafeMutableRawPointer?) -> CFMachPort?](cgevent/tapcreateforpsn(processserialnumber:place:options:eventsofinterest:callback:userinfo:).md)
  Creates an event tap for a specified process.
- [class func tapEnable(tap: CFMachPort, enable: Bool)](cgevent/tapenable(tap:enable:).md)
  Enables or disables an event tap.
- [class func tapIsEnabled(tap: CFMachPort) -> Bool](cgevent/tapisenabled(tap:).md)
  Returns a Boolean value indicating whether an event tap is enabled.
- [func tapPostEvent(CGEventTapProxy?)](cgevent/tappostevent(_:).md)
  Posts a Quartz event from an event tap into the event stream.
- [func post(tap: CGEventTapLocation)](cgevent/post(tap:).md)
  Posts a Quartz event into the event stream at a specified location.
- [func postToPSN(processSerialNumber: UnsafeMutableRawPointer?)](cgevent/posttopsn(processserialnumber:).md)
  Posts a Quartz event into the event stream for a specific application.
- [func CGGetEventTapList(UInt32, UnsafeMutablePointer<CGEventTapInformation>?, UnsafeMutablePointer<UInt32>?) -> CGError](cggeteventtaplist(_:_:_:).md)
  Gets a list of currently installed event taps.
### Working With Event Sources
- [class var typeID: CFTypeID](cgeventsource/typeid.md)
  Returns the type identifier for the opaque type `CGEventSourceRef`.
- [init?(stateID: CGEventSourceStateID)](cgeventsource/init(stateid:).md)
  Returns a Quartz event source created with a specified source state.
- [var keyboardType: CGEventSourceKeyboardType](cgeventsource/keyboardtype.md)
  Returns the keyboard type to be used with a Quartz event source.
- [var sourceStateID: CGEventSourceStateID](cgeventsource/sourcestateid.md)
  Returns the source state associated with a Quartz event source.
- [class func buttonState(CGEventSourceStateID, button: CGMouseButton) -> Bool](cgeventsource/buttonstate(_:button:).md)
  Returns a Boolean value indicating the current button state of a Quartz event source.
- [class func keyState(CGEventSourceStateID, key: CGKeyCode) -> Bool](cgeventsource/keystate(_:key:).md)
  Returns a Boolean value indicating the current keyboard state of a Quartz event source.
- [class func flagsState(CGEventSourceStateID) -> CGEventFlags](cgeventsource/flagsstate(_:).md)
  Returns the current flags of a Quartz event source.
- [class func secondsSinceLastEventType(CGEventSourceStateID, eventType: CGEventType) -> CFTimeInterval](cgeventsource/secondssincelasteventtype(_:eventtype:).md)
  Returns the elapsed time since the last event for a Quartz event source.
- [class func counterForEventType(CGEventSourceStateID, eventType: CGEventType) -> UInt32](cgeventsource/counterforeventtype(_:eventtype:).md)
  Returns a count of events of a given type seen since the window server started.
- [var userData: Int64](cgeventsource/userdata.md)
  Returns the 64-bit user-specified data for a Quartz event source.
- [func getLocalEventsFilterDuringSuppressionState(CGEventSuppressionState) -> CGEventFilterMask](cgeventsource/getlocaleventsfilterduringsuppressionstate(_:).md)
  Returns the mask that indicates which classes of local hardware events are enabled during event suppression.
- [func setLocalEventsFilterDuringSuppressionState(CGEventFilterMask, state: CGEventSuppressionState)](cgeventsource/setlocaleventsfilterduringsuppressionstate(_:state:).md)
  Sets the mask that indicates which classes of local hardware events are enabled during event suppression.
- [var localEventsSuppressionInterval: CFTimeInterval](cgeventsource/localeventssuppressioninterval.md)
  Returns the interval that local hardware events may be suppressed following the posting of a Quartz event.
- [var pixelsPerLine: Double](cgeventsource/pixelsperline.md)
  Gets the scale of pixels per line in a scrolling event source.
### Callbacks
- [typealias CGEventTapCallBack](cgeventtapcallback.md)
  A client-supplied callback function that’s invoked whenever an associated event tap receives a Quartz event.
### Data Types
- [typealias CGButtonCount](cgbuttoncount.md)
  Represents the number of buttons being set in a synthetic mouse event.
- [typealias CGCharCode](cgcharcode.md)
  Represents a character generated by pressing one or more keys on a keyboard.
- [typealias CGEventMask](cgeventmask.md)
  Defines a mask that identifies the set of Quartz events to be observed in an event tap.
- [class CGEvent](cgevent.md)
  Defines an opaque type that represents a low-level hardware event.
- [typealias CGEventSourceKeyboardType](cgeventsourcekeyboardtype.md)
  Defines a code that represents the type of keyboard used with a specified event source.
- [class CGEventSource](cgeventsource.md)
  Defines an opaque type that represents the source of a Quartz event.
- [typealias CGEventTapInformation](cgeventtapinformation.md)
  Defines the structure used to report information about event taps.
- [typealias CGEventTapProxy](cgeventtapproxy.md)
  Defines an opaque type that represents state within the client application that’s associated with an event tap.
- [typealias CGEventTimestamp](cgeventtimestamp.md)
  Defines the elapsed time in nanoseconds since startup that a Quartz event occurred.
- [typealias CGKeyCode](cgkeycode.md)
  Represents the virtual key codes used in keyboard events.
- [typealias CGWheelCount](cgwheelcount.md)
  Represents the number of wheels being set in a scroll wheel event.
### Constants
- [enum CGEventField](cgeventfield.md)
  Constants used as keys to access specialized fields in low-level events.
- [struct CGEventFilterMask](cgeventfiltermask.md)
  Specify masks for classes of low-level events that can be filtered during event suppression states.
- [struct CGEventFlags](cgeventflags.md)
  Constants that indicate the modifier key state at the time an event is created, as well as other event-related states.
- [enum CGEventSourceStateID](cgeventsourcestateid.md)
  Constants that specify the possible source states of an event source.
- [Event Source Token](event-source-token.md)
  Specifies any input event type.
- [enum CGEventSuppressionState](cgeventsuppressionstate.md)
  Specify the event suppression states that can occur after posting an event.
- [enum CGEventTapLocation](cgeventtaplocation.md)
  Constants that specify possible tapping points for events.
- [enum CGEventTapOptions](cgeventtapoptions.md)
  Constants that specify whether a new event tap is an active filter or a passive listener.
- [enum CGEventTapPlacement](cgeventtapplacement.md)
  Constants that specify where a new event tap is inserted into the list of active event taps.
- [enum CGEventType](cgeventtype.md)
  Constants that specify the different types of input events.
- [Event Type Mask](event-type-mask.md)
  Specifies an event mask that represents all event types.
- [enum CGMouseButton](cgmousebutton.md)
  Constants that specify buttons on a one, two, or three-button mouse.
- [enum CGEventMouseSubtype](cgeventmousesubtype.md)
  Constants used with the [`CGEventField.mouseEventSubtype`](cgeventfield/mouseeventsubtype.md) event field.
- [enum CGScrollEventUnit](cgscrolleventunit.md)
  Constants that specify the unit of measurement for a scrolling event.
### Deprecated Functions
- [func CGPostKeyboardEvent(CGCharCode, CGKeyCode, boolean_t) -> CGError](cgpostkeyboardevent(_:_:_:).md)
  Synthesizes a low-level keyboard event on the local machine.
- [func CGEnableEventStateCombining(boolean_t) -> CGError](cgenableeventstatecombining(_:).md)
  Enables or disables the merging of actual key and mouse state with the application-specified state in a synthetic event.
- [func CGInhibitLocalEvents(boolean_t) -> CGError](cginhibitlocalevents(_:).md)
  Turns off local hardware events in the current session.
- [func CGSetLocalEventsFilterDuringSuppressionState(CGEventFilterMask, CGEventSuppressionState) -> CGError](cgsetlocaleventsfilterduringsuppressionstate(_:_:).md)
  Filters local hardware events from the keyboard and mouse during the short interval after a synthetic event is posted.
- [func CGSetLocalEventsSuppressionInterval(CFTimeInterval) -> CGError](cgsetlocaleventssuppressioninterval(_:).md)
  Sets the time interval in seconds that local hardware events are suppressed after posting a synthetic event.

## See Also

- [Quartz Display Services](quartz-display-services.md)
  Provides direct access to features in the macOS window server for configuring and controlling display hardware.
- [Quartz Window Services](quartz-window-services.md)
  Provides information about the windows managed by the macOS window server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/quartz-event-services)*