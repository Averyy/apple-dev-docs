# enterExitEvent(with:location:modifierFlags:timestamp:windowNumber:context:eventNumber:trackingNumber:userData:)

**Framework**: AppKit  
**Kind**: method

Creates and returns a new event object that describes a tracking-rectangle or cursor-update event.

**Availability**:
- macOS ?+

## Declaration

```swift
class func enterExitEvent(with type: NSEvent.EventType, location: NSPoint, modifierFlags flags: NSEvent.ModifierFlags, timestamp time: TimeInterval, windowNumber wNum: Int, context unusedPassNil: NSGraphicsContext?, eventNumber eNum: Int, trackingNumber tNum: Int, userData data: UnsafeMutableRawPointer?) -> NSEvent?
```

#### Return Value

The created `NSEvent` object or `nil` if the object could not be created.

## Parameters

- `type`: One of the following event-type constants:   ,  ,  . If the specified constant is not one of these, an   is raised
- `location`: The cursor location in the base coordinate system of the window specified by  .
- `flags`: An integer bit field containing any of the modifier key masks described in  , combined using the C bitwise OR operator.
- `time`: The time the event occurred in seconds since system startup.
- `wNum`: An integer that identifies the window device associated with the event, which is associated with the   that will receive the event.
- `unusedPassNil`: The display graphics context of the event. Pass   for this parameter.
- `eNum`: An identifier for the new event. It’s normally taken from a counter for mouse events, which continually increases as the application runs.
- `tNum`: A number that identifies the tracking rectangle. This identifier is the same as that returned by the   method  .
- `data`: Data arbitrarily associated with the tracking rectangle when it was set up using the   method  .

## See Also

- [var eventNumber: Int](nsevent/eventnumber.md)
  The counter value of the latest mouse or tracking-rectangle event object.
- [var trackingNumber: Int](nsevent/trackingnumber.md)
  The identifier of a mouse-tracking event.
- [var systemUptime: TimeInterval](../foundation/processinfo/1414553-systemuptime.md)
  The amount of time the system has been awake since the last time it was restarted.
- [var userData: UnsafeMutableRawPointer?](nsevent/userdata.md)
  The data associated with a mouse-tracking event.
- [class func keyEvent(with: NSEvent.EventType, location: NSPoint, modifierFlags: NSEvent.ModifierFlags, timestamp: TimeInterval, windowNumber: Int, context: NSGraphicsContext?, characters: String, charactersIgnoringModifiers: String, isARepeat: Bool, keyCode: UInt16) -> NSEvent?](nsevent/keyevent(with:location:modifierflags:timestamp:windownumber:context:characters:charactersignoringmodifiers:isarepeat:keycode:).md)
  Creates and returns a new event object that describes a key event.
- [class func mouseEvent(with: NSEvent.EventType, location: NSPoint, modifierFlags: NSEvent.ModifierFlags, timestamp: TimeInterval, windowNumber: Int, context: NSGraphicsContext?, eventNumber: Int, clickCount: Int, pressure: Float) -> NSEvent?](nsevent/mouseevent(with:location:modifierflags:timestamp:windownumber:context:eventnumber:clickcount:pressure:).md)
  Creates and returns a new event object that describes a mouse-down, -up, -moved, or -dragged event.
- [class func otherEvent(with: NSEvent.EventType, location: NSPoint, modifierFlags: NSEvent.ModifierFlags, timestamp: TimeInterval, windowNumber: Int, context: NSGraphicsContext?, subtype: Int16, data1: Int, data2: Int) -> NSEvent?](nsevent/otherevent(with:location:modifierflags:timestamp:windownumber:context:subtype:data1:data2:).md)
  Creates and returns a new event object that describes a custom event.
- [init?(eventRef: UnsafeRawPointer)](nsevent/init(eventref:).md)
  Creates and returns a new event object for a Carbon event.
- [init?(cgEvent: CGEvent)](nsevent/init(cgevent:).md)
  Creates and returns an event object for a Core Graphics event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/enterexitevent(with:location:modifierflags:timestamp:windownumber:context:eventnumber:trackingnumber:userdata:))*