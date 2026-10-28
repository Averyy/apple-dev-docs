# mouseEvent(with:location:modifierFlags:timestamp:windowNumber:context:eventNumber:clickCount:pressure:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Creates and returns a new event object that describes a mouse-down, -up, -moved, or -dragged event.

**Availability**:
- macOS

## Declaration

```swift
class func mouseEvent(with type: NSEvent.EventType, location: NSPoint, modifierFlags flags: NSEvent.ModifierFlags, timestamp time: TimeInterval, windowNumber wNum: Int, context unusedPassNil: NSGraphicsContext?, eventNumber eNum: Int, clickCount cNum: Int, pressure: Float) -> NSEvent?
```

```objc
+ (NSEvent *) mouseEventWithType:(NSEventType) type location:(NSPoint) location modifierFlags:(NSEventModifierFlags) flags timestamp:(NSTimeInterval) time windowNumber:(NSInteger) wNum context:(NSGraphicsContext *) unusedPassNil eventNumber:(NSInteger) eNum clickCount:(NSInteger) cNum pressure:(float) pressure;
```

## Return Value

The created `NSEvent` instance or `nil` if the instance could not be created.

## Parameters

- `type`: One of the modifier key masks described in [`NSEvent.EventType`](./eventtype.md), or an `NSInternalInconsistencyException` is raised.
- `location`: The cursor location in the base coordinate system of the window specified by `windowNum`.
- `flags`: An integer bit field containing any of the modifier key masks described in `Getting Unicode Values`, combined using the C bitwise OR operator.
- `time`: The time the event occurred in seconds since system startup.
- `wNum`: An integer that identifies the window device associated with the event, which is associated with the `NSWindow` that will receive the event.
- `unusedPassNil`: The display graphics context of the event. Pass `nil` for this parameter.
- `eNum`: An identifier for the new event. It’s normally taken from a counter for mouse events, which continually increases as the application runs.
- `cNum`: The number of mouse clicks associated with the mouse event.
- `pressure`: A value from `0.0` to `1.0` indicating the pressure applied to the input device on a mouse event, used for an appropriate device such as a graphics tablet. For devices that aren’t pressure-sensitive, the value should be either `0.0` or `1.0`.

## See Also

### Related Documentation
- [var clickCount: Int](./clickcount.md)
  The number of mouse clicks associated with a mouse-down or mouse-up event.
- [var eventNumber: Int](./eventnumber.md)
  The counter value of the latest mouse or tracking-rectangle event object.
- [var systemUptime: TimeInterval](../../Foundation/processinfo/systemuptime.md)
  The amount of time the system has been awake since the last time it was restarted.
- [var pressure: Float](./pressure.md)
  A normalized value that indicates the degree of pressure applied to an appropriate input device.
### Creating an event object
- [class func keyEvent(with: NSEvent.EventType, location: NSPoint, modifierFlags: NSEvent.ModifierFlags, timestamp: TimeInterval, windowNumber: Int, context: NSGraphicsContext?, characters: String, charactersIgnoringModifiers: String, isARepeat: Bool, keyCode: UInt16) -> NSEvent?](./keyevent%28with,location,modifierflags,timestamp,windownumber,context,characters,charactersignoringmodifiers,isarepeat,keycode%29.md)
  Creates and returns a new event object that describes a key event.
- [class func enterExitEvent(with: NSEvent.EventType, location: NSPoint, modifierFlags: NSEvent.ModifierFlags, timestamp: TimeInterval, windowNumber: Int, context: NSGraphicsContext?, eventNumber: Int, trackingNumber: Int, userData: UnsafeMutableRawPointer?) -> NSEvent?](./enterexitevent%28with,location,modifierflags,timestamp,windownumber,context,eventnumber,trackingnumber,userdata%29.md)
  Creates and returns a new event object that describes a tracking-rectangle or cursor-update event.
- [class func otherEvent(with: NSEvent.EventType, location: NSPoint, modifierFlags: NSEvent.ModifierFlags, timestamp: TimeInterval, windowNumber: Int, context: NSGraphicsContext?, subtype: Int16, data1: Int, data2: Int) -> NSEvent?](./otherevent%28with,location,modifierflags,timestamp,windownumber,context,subtype,data1,data2%29.md)
  Creates and returns a new event object that describes a custom event.
- [init?(eventRef: UnsafeRawPointer)](./init%28eventref%29.md)
  Creates and returns a new event object for a Carbon event.
- [init?(cgEvent: CGEvent)](./init%28cgevent%29-4igjn.md)
  Creates and returns an event object for a Core Graphics event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/mouseevent(with:location:modifierflags:timestamp:windownumber:context:eventnumber:clickcount:pressure:))*