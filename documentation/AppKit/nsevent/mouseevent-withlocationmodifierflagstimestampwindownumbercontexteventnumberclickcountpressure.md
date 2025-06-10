# mouseEvent(with:location:modifierFlags:timestamp:windowNumber:context:eventNumber:clickCount:pressure:)

**Framework**: AppKit  
**Kind**: method

Creates and returns a new event object that describes a mouse-down, -up, -moved, or -dragged event.

**Availability**:
- macOS ?+

## Declaration

```swift
class func mouseEvent(with type: NSEvent.EventType, location: NSPoint, modifierFlags flags: NSEvent.ModifierFlags, timestamp time: TimeInterval, windowNumber wNum: Int, context unusedPassNil: NSGraphicsContext?, eventNumber eNum: Int, clickCount cNum: Int, pressure: Float) -> NSEvent?
```

#### Return Value

The created `NSEvent` instance or `nil` if the instance could not be created.

## Parameters

- `type`: One of the modifier key masks described in  , or an   is raised.
- `location`: The cursor location in the base coordinate system of the window specified by  .
- `flags`: An integer bit field containing any of the modifier key masks described in  , combined using the C bitwise OR operator.
- `time`: The time the event occurred in seconds since system startup.
- `wNum`: An integer that identifies the window device associated with the event, which is associated with the   that will receive the event.
- `unusedPassNil`: The display graphics context of the event. Pass   for this parameter.
- `eNum`: An identifier for the new event. It’s normally taken from a counter for mouse events, which continually increases as the application runs.
- `cNum`: The number of mouse clicks associated with the mouse event.
- `pressure`: A value from   to   indicating the pressure applied to the input device on a mouse event, used for an appropriate device such as a graphics tablet. For devices that aren’t pressure-sensitive, the value should be either   or  .

## See Also

- [var clickCount: Int](nsevent/clickcount.md)
  The number of mouse clicks associated with a mouse-down or mouse-up event.
- [var eventNumber: Int](nsevent/eventnumber.md)
  The counter value of the latest mouse or tracking-rectangle event object.
- [var systemUptime: TimeInterval { get }](../Foundation/ProcessInfo/systemUptime.md)
  The amount of time the system has been awake since the last time it was restarted.
- [var pressure: Float](nsevent/pressure.md)
  A normalized value that indicates the degree of pressure applied to an appropriate input device.
- [class func keyEvent(with: NSEvent.EventType, location: NSPoint, modifierFlags: NSEvent.ModifierFlags, timestamp: TimeInterval, windowNumber: Int, context: NSGraphicsContext?, characters: String, charactersIgnoringModifiers: String, isARepeat: Bool, keyCode: UInt16) -> NSEvent?](nsevent/keyevent(with:location:modifierflags:timestamp:windownumber:context:characters:charactersignoringmodifiers:isarepeat:keycode:).md)
  Creates and returns a new event object that describes a key event.
- [class func enterExitEvent(with: NSEvent.EventType, location: NSPoint, modifierFlags: NSEvent.ModifierFlags, timestamp: TimeInterval, windowNumber: Int, context: NSGraphicsContext?, eventNumber: Int, trackingNumber: Int, userData: UnsafeMutableRawPointer?) -> NSEvent?](nsevent/enterexitevent(with:location:modifierflags:timestamp:windownumber:context:eventnumber:trackingnumber:userdata:).md)
  Creates and returns a new event object that describes a tracking-rectangle or cursor-update event.
- [class func otherEvent(with: NSEvent.EventType, location: NSPoint, modifierFlags: NSEvent.ModifierFlags, timestamp: TimeInterval, windowNumber: Int, context: NSGraphicsContext?, subtype: Int16, data1: Int, data2: Int) -> NSEvent?](nsevent/otherevent(with:location:modifierflags:timestamp:windownumber:context:subtype:data1:data2:).md)
  Creates and returns a new event object that describes a custom event.
- [init?(eventRef: UnsafeRawPointer)](nsevent/init(eventref:).md)
  Creates and returns a new event object for a Carbon event.
- [init?(cgEvent: CGEvent)](nsevent/init(cgevent:).md)
  Creates and returns an event object for a Core Graphics event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/mouseevent(with:location:modifierflags:timestamp:windownumber:context:eventnumber:clickcount:pressure:))*