# CGEvent

**Framework**: Core Graphics  
**Kind**: class  
**Role**: Class

Defines an opaque type that represents a low-level hardware event.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
class CGEvent
```

```c
typedef struct __CGEvent * CGEventRef;
```

## Overview

Low-level hardware events of this type are referred to as Quartz events. A typical event in macOS originates when the user manipulates an input device such as a mouse or a keyboard. The device driver associated with that device, through the I/O Kit, creates a low-level event, puts it in the window server’s event queue, and notifies the window server. The window server creates a Quartz event, annotates the event, and dispatches the event to the appropriate run-loop port of the target process. There the event is picked up by the Carbon Event Manager and forwarded to the event-handling mechanism appropriate to the application environment. You can use event taps to gain access to Quartz events at several different steps in this process.

This opaque type is derived from CFType and inherits the properties that all Core Foundation types have in common. For more information, see [`CFTypeRef`](../CoreFoundation/cftyperef.md).

## Topics

### Initializers
- [func copy() -> CGEvent?](./cgevent/copy%28%29.md)
  Returns a copy of an existing Quartz event.
- [init?(keyboardEventSource: CGEventSource?, virtualKey: CGKeyCode, keyDown: Bool)](./cgevent/init%28keyboardeventsource,virtualkey,keydown%29.md)
  Returns a new Quartz keyboard event.
- [init?(mouseEventSource: CGEventSource?, mouseType: CGEventType, mouseCursorPosition: CGPoint, mouseButton: CGMouseButton)](./cgevent/init%28mouseeventsource,mousetype,mousecursorposition,mousebutton%29.md)
  Returns a new Quartz mouse event.
- [init?(source: CGEventSource?)](./cgevent/init%28source%29.md)
  Returns a new Quartz event.
- [init?(withDataAllocator: CFAllocator?, data: CFData?)](./cgevent/init%28withdataallocator,data%29.md)
  Returns a Quartz event created from a flattened data representation of the event.
- [init?(scrollWheelEvent2Source: CGEventSource?, units: CGScrollEventUnit, wheelCount: UInt32, wheel1: Int32, wheel2: Int32, wheel3: Int32)](./cgevent/init%28scrollwheelevent2source,units,wheelcount,wheel1,wheel2,wheel3%29.md)
### Instance Properties
- [var flags: CGEventFlags](./cgevent/flags.md)
  Returns the event flags of a Quartz event.
- [var location: CGPoint](./cgevent/location.md)
  Returns the location of a Quartz mouse event.
- [var timestamp: CGEventTimestamp](./cgevent/timestamp.md)
  Returns the timestamp of a Quartz event.
- [var type: CGEventType](./cgevent/type.md)
  Returns the event type of a Quartz event (left mouse down, for example).
- [var unflippedLocation: CGPoint](./cgevent/unflippedlocation.md)
  Returns the location of a Quartz mouse event.
- [var data: CFData?](./cgevent/data.md)
### Type Properties
- [class var typeID: CFTypeID](./cgevent/typeid.md)
  Returns the type identifier for the opaque type `CGEventRef`.
### Instance Methods
- [func getDoubleValueField(CGEventField) -> Double](./cgevent/getdoublevaluefield%28_%29.md)
  Returns the floating-point value of a field in a Quartz event.
- [func getIntegerValueField(CGEventField) -> Int64](./cgevent/getintegervaluefield%28_%29.md)
  Returns the integer value of a field in a Quartz event.
- [func keyboardGetUnicodeString(maxStringLength: Int, actualStringLength: UnsafeMutablePointer<Int>?, unicodeString: UnsafeMutablePointer<UniChar>?)](./cgevent/keyboardgetunicodestring%28maxstringlength,actualstringlength,unicodestring%29.md)
  Returns the Unicode string associated with a Quartz keyboard event.
- [func keyboardSetUnicodeString(stringLength: Int, unicodeString: UnsafePointer<UniChar>?)](./cgevent/keyboardsetunicodestring%28stringlength,unicodestring%29.md)
  Sets the Unicode string associated with a Quartz keyboard event.
- [func post(tap: CGEventTapLocation)](./cgevent/post%28tap%29.md)
  Posts a Quartz event into the event stream at a specified location.
- [func postToPSN(processSerialNumber: UnsafeMutableRawPointer?)](./cgevent/posttopsn%28processserialnumber%29.md)
  Posts a Quartz event into the event stream for a specific application.
- [func postToPid(pid_t)](./cgevent/posttopid%28_%29.md)
- [func setDoubleValueField(CGEventField, value: Double)](./cgevent/setdoublevaluefield%28_,value%29.md)
  Sets the floating-point value of a field in a Quartz event.
- [func setIntegerValueField(CGEventField, value: Int64)](./cgevent/setintegervaluefield%28_,value%29.md)
  Sets the integer value of a field in a Quartz event.
- [func setSource(CGEventSource?)](./cgevent/setsource%28_%29.md)
  Sets the event source of a Quartz event.
- [func tapPostEvent(CGEventTapProxy?)](./cgevent/tappostevent%28_%29.md)
  Posts a Quartz event from an event tap into the event stream.
### Type Methods
- [class func tapCreate(tap: CGEventTapLocation, place: CGEventTapPlacement, options: CGEventTapOptions, eventsOfInterest: CGEventMask, callback: CGEventTapCallBack, userInfo: UnsafeMutableRawPointer?) -> CFMachPort?](./cgevent/tapcreate%28tap,place,options,eventsofinterest,callback,userinfo%29.md)
  Creates an event tap.
- [class func tapCreateForPSN(processSerialNumber: UnsafeMutableRawPointer, place: CGEventTapPlacement, options: CGEventTapOptions, eventsOfInterest: CGEventMask, callback: CGEventTapCallBack, userInfo: UnsafeMutableRawPointer?) -> CFMachPort?](./cgevent/tapcreateforpsn%28processserialnumber,place,options,eventsofinterest,callback,userinfo%29.md)
  Creates an event tap for a specified process.
- [class func tapCreateForPid(pid: pid_t, place: CGEventTapPlacement, options: CGEventTapOptions, eventsOfInterest: CGEventMask, callback: CGEventTapCallBack, userInfo: UnsafeMutableRawPointer?) -> CFMachPort?](./cgevent/tapcreateforpid%28pid,place,options,eventsofinterest,callback,userinfo%29.md)
- [class func tapEnable(tap: CFMachPort, enable: Bool)](./cgevent/tapenable%28tap,enable%29.md)
  Enables or disables an event tap.
- [class func tapIsEnabled(tap: CFMachPort) -> Bool](./cgevent/tapisenabled%28tap%29.md)
  Returns a Boolean value indicating whether an event tap is enabled.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Data Types
- [typealias CGButtonCount](./cgbuttoncount.md)
  Represents the number of buttons being set in a synthetic mouse event.
- [typealias CGCharCode](./cgcharcode.md)
  Represents a character generated by pressing one or more keys on a keyboard.
- [typealias CGDirectDisplayID](./cgdirectdisplayid.md)
  A unique identifier for an attached display.
- [typealias CGDisplayBlendFraction](./cgdisplayblendfraction.md)
  The percentage of blend color used in a fade operation.
- [typealias CGDisplayConfigRef](./cgdisplayconfigref.md)
  A reference to a display configuration transaction.
- [typealias CGDisplayCount](./cgdisplaycount.md)
  The number of displays in various lists.
- [typealias CGDisplayErr](./cgdisplayerr.md)
  A uniform type for result codes returned by functions in Quartz Display Services.
- [typealias CGDisplayFadeInterval](./cgdisplayfadeinterval.md)
  The duration in seconds of a fade operation or a fade hardware reservation.
- [typealias CGDisplayFadeReservationToken](./cgdisplayfadereservationtoken.md)
  A token issued by Quartz when reserving one or more displays for a fade operation during a specified interval.
- [class CGDisplayMode](./cgdisplaymode.md)
  A reference to a display mode object.
- [typealias CGDisplayReconfigurationCallBack](./cgdisplayreconfigurationcallback.md)
  A client-supplied callback function that’s invoked whenever the configuration of a local display is changed.
- [typealias CGDisplayReservationInterval](./cgdisplayreservationinterval.md)
  The time interval for a fade reservation.
- [class CGDisplayStream](./cgdisplaystream.md)
  A reference to a display stream object.
- [typealias CGDisplayStreamFrameAvailableHandler](./cgdisplaystreamframeavailablehandler.md)
  A block called when a data stream has a new frame event to process.
- [class CGDisplayStreamUpdate](./cgdisplaystreamupdate.md)
  A reference to frame update’s metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgevent)*