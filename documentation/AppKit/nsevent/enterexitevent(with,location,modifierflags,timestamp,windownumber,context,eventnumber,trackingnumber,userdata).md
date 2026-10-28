# enterExitEvent(with:location:modifierFlags:timestamp:windowNumber:context:eventNumber:trackingNumber:userData:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Creates and returns a new event object that describes a tracking-rectangle or cursor-update event.

**Availability**:
- macOS

## Declaration

```swift
class func enterExitEvent(with type: NSEvent.EventType, location: NSPoint, modifierFlags flags: NSEvent.ModifierFlags, timestamp time: TimeInterval, windowNumber wNum: Int, context unusedPassNil: NSGraphicsContext?, eventNumber eNum: Int, trackingNumber tNum: Int, userData data: UnsafeMutableRawPointer?) -> NSEvent?
```

```objc
+ (NSEvent *) enterExitEventWithType:(NSEventType) type location:(NSPoint) location modifierFlags:(NSEventModifierFlags) flags timestamp:(NSTimeInterval) time windowNumber:(NSInteger) wNum context:(NSGraphicsContext *) unusedPassNil eventNumber:(NSInteger) eNum trackingNumber:(NSInteger) tNum userData:(void *) data;
```

## Return Value

The created `NSEvent` object or `nil` if the object could not be created.

## Parameters

- `type`: One of the following event-type constants:  `NSMouseEntered`, `NSMouseExited`, `NSCursorUpdate`. If the specified constant is not one of these, an `NSInternalInconsistencyException` is raised
- `location`: The cursor location in the base coordinate system of the window specified by `windowNum`.
- `flags`: An integer bit field containing any of the modifier key masks described in `Getting Unicode Values`, combined using the C bitwise OR operator.
- `time`: The time the event occurred in seconds since system startup.
- `wNum`: An integer that identifies the window device associated with the event, which is associated with the `NSWindow` that will receive the event.
- `unusedPassNil`: The display graphics context of the event. Pass `nil` for this parameter.
- `eNum`: An identifier for the new event. It’s normally taken from a counter for mouse events, which continually increases as the application runs.
- `tNum`: A number that identifies the tracking rectangle. This identifier is the same as that returned by the `NSView` method [`addTrackingRect(_:owner:userData:assumeInside:)`](../nsview/addtrackingrect%28_,owner,userdata,assumeinside%29.md).
- `data`: Data arbitrarily associated with the tracking rectangle when it was set up using the `NSView` method [`addTrackingRect(_:owner:userData:assumeInside:)`](../nsview/addtrackingrect%28_,owner,userdata,assumeinside%29.md).

## See Also

### Related Documentation
- [var eventNumber: Int](./eventnumber.md)
  The counter value of the latest mouse or tracking-rectangle event object.
- [var trackingNumber: Int](./trackingnumber.md)
  The identifier of a mouse-tracking event.
- [var systemUptime: TimeInterval](../../Foundation/processinfo/systemuptime.md)
  The amount of time the system has been awake since the last time it was restarted.
- [var userData: UnsafeMutableRawPointer?](./userdata.md)
  The data associated with a mouse-tracking event.
### Creating an event object
- [class func keyEvent(with: NSEvent.EventType, location: NSPoint, modifierFlags: NSEvent.ModifierFlags, timestamp: TimeInterval, windowNumber: Int, context: NSGraphicsContext?, characters: String, charactersIgnoringModifiers: String, isARepeat: Bool, keyCode: UInt16) -> NSEvent?](./keyevent%28with,location,modifierflags,timestamp,windownumber,context,characters,charactersignoringmodifiers,isarepeat,keycode%29.md)
  Creates and returns a new event object that describes a key event.
- [class func mouseEvent(with: NSEvent.EventType, location: NSPoint, modifierFlags: NSEvent.ModifierFlags, timestamp: TimeInterval, windowNumber: Int, context: NSGraphicsContext?, eventNumber: Int, clickCount: Int, pressure: Float) -> NSEvent?](./mouseevent%28with,location,modifierflags,timestamp,windownumber,context,eventnumber,clickcount,pressure%29.md)
  Creates and returns a new event object that describes a mouse-down, -up, -moved, or -dragged event.
- [class func otherEvent(with: NSEvent.EventType, location: NSPoint, modifierFlags: NSEvent.ModifierFlags, timestamp: TimeInterval, windowNumber: Int, context: NSGraphicsContext?, subtype: Int16, data1: Int, data2: Int) -> NSEvent?](./otherevent%28with,location,modifierflags,timestamp,windownumber,context,subtype,data1,data2%29.md)
  Creates and returns a new event object that describes a custom event.
- [init?(eventRef: UnsafeRawPointer)](./init%28eventref%29.md)
  Creates and returns a new event object for a Carbon event.
- [init?(cgEvent: CGEvent)](./init%28cgevent%29-4igjn.md)
  Creates and returns an event object for a Core Graphics event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/enterexitevent(with:location:modifierflags:timestamp:windownumber:context:eventnumber:trackingnumber:userdata:))*