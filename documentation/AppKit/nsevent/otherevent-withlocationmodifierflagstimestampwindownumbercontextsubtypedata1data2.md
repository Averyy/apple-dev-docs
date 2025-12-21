# otherEvent(with:location:modifierFlags:timestamp:windowNumber:context:subtype:data1:data2:)

**Framework**: AppKit  
**Kind**: method

Creates and returns a new event object that describes a custom event.

**Availability**:
- macOS ?+

## Declaration

```swift
class func otherEvent(with type: NSEvent.EventType, location: NSPoint, modifierFlags flags: NSEvent.ModifierFlags, timestamp time: TimeInterval, windowNumber wNum: Int, context unusedPassNil: NSGraphicsContext?, subtype: Int16, data1 d1: Int, data2 d2: Int) -> NSEvent?
```

#### Return Value

The created `NSEvent` object or `nil` if the object couldn’t be created.

## Parameters

- `type`: If   is anything else, an   is raised. Your code should only create events of type  .
- `location`: The cursor location in the base coordinate system of the window specified by  .
- `flags`: An integer bit field containing any of the modifier key masks described in  , combined using the C bitwise OR operator.
- `time`: The time the event occurred in seconds since system startup.
- `wNum`: An integer that identifies the window device associated with the event, which is associated with the   that will receive the event.
- `unusedPassNil`: The display graphics context of the event. Pass   for this parameter.
- `subtype`: A numeric identifier that further differentiates custom events of types  ,  , and  .   events don’t use this attribute.
- `d1`: Additional data associated with the event.   events don’t use these attributes.
- `d2`: Additional data associated with the event.   events don’t use these attributes.

## See Also

- [var subtype: NSEvent.EventSubtype](nsevent/subtype.md)
  The event’s subtype.
- [var data1: Int](nsevent/data1.md)
  Additional data associated with this event.
- [var systemUptime: TimeInterval](../Foundation/ProcessInfo/systemUptime.md)
  The amount of time the system has been awake since the last time it was restarted.
- [var data2: Int](nsevent/data2.md)
  Additional data associated with this event.
- [class func keyEvent(with: NSEvent.EventType, location: NSPoint, modifierFlags: NSEvent.ModifierFlags, timestamp: TimeInterval, windowNumber: Int, context: NSGraphicsContext?, characters: String, charactersIgnoringModifiers: String, isARepeat: Bool, keyCode: UInt16) -> NSEvent?](nsevent/keyevent(with:location:modifierflags:timestamp:windownumber:context:characters:charactersignoringmodifiers:isarepeat:keycode:).md)
  Creates and returns a new event object that describes a key event.
- [class func mouseEvent(with: NSEvent.EventType, location: NSPoint, modifierFlags: NSEvent.ModifierFlags, timestamp: TimeInterval, windowNumber: Int, context: NSGraphicsContext?, eventNumber: Int, clickCount: Int, pressure: Float) -> NSEvent?](nsevent/mouseevent(with:location:modifierflags:timestamp:windownumber:context:eventnumber:clickcount:pressure:).md)
  Creates and returns a new event object that describes a mouse-down, -up, -moved, or -dragged event.
- [class func enterExitEvent(with: NSEvent.EventType, location: NSPoint, modifierFlags: NSEvent.ModifierFlags, timestamp: TimeInterval, windowNumber: Int, context: NSGraphicsContext?, eventNumber: Int, trackingNumber: Int, userData: UnsafeMutableRawPointer?) -> NSEvent?](nsevent/enterexitevent(with:location:modifierflags:timestamp:windownumber:context:eventnumber:trackingnumber:userdata:).md)
  Creates and returns a new event object that describes a tracking-rectangle or cursor-update event.
- [init?(eventRef: UnsafeRawPointer)](nsevent/init(eventref:).md)
  Creates and returns a new event object for a Carbon event.
- [init?(cgEvent: CGEvent)](nsevent/init(cgevent:).md)
  Creates and returns an event object for a Core Graphics event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/otherevent(with:location:modifierflags:timestamp:windownumber:context:subtype:data1:data2:))*