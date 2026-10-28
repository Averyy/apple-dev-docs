# init(eventRef:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates and returns a new event object for a Carbon event.

**Availability**:
- macOS 10.5+

## Declaration

```swift
init?(eventRef: UnsafeRawPointer)
```

```objc
+ (NSEvent *) eventWithEventRef:(const void *) eventRef;
```

## Return Value

An autoreleased `NSEvent` object corresponding to `eventRef` or `nil` if `eventRef` cannot be converted into an equivalent `NSEvent` object.

## Discussion

This method is valid for all events. The created `NSEvent` object retains the `EventRef` object and is released when the `NSEvent` object is freed.

## Parameters

- `eventRef`: The `EventRef` opaque type to be associated with the created `NSEvent` object.

## See Also

### Related Documentation
- [var eventRef: UnsafeRawPointer?](./eventref.md)
  An opaque Carbon type associated with this event.
### Creating an event object
- [class func keyEvent(with: NSEvent.EventType, location: NSPoint, modifierFlags: NSEvent.ModifierFlags, timestamp: TimeInterval, windowNumber: Int, context: NSGraphicsContext?, characters: String, charactersIgnoringModifiers: String, isARepeat: Bool, keyCode: UInt16) -> NSEvent?](./keyevent%28with,location,modifierflags,timestamp,windownumber,context,characters,charactersignoringmodifiers,isarepeat,keycode%29.md)
  Creates and returns a new event object that describes a key event.
- [class func mouseEvent(with: NSEvent.EventType, location: NSPoint, modifierFlags: NSEvent.ModifierFlags, timestamp: TimeInterval, windowNumber: Int, context: NSGraphicsContext?, eventNumber: Int, clickCount: Int, pressure: Float) -> NSEvent?](./mouseevent%28with,location,modifierflags,timestamp,windownumber,context,eventnumber,clickcount,pressure%29.md)
  Creates and returns a new event object that describes a mouse-down, -up, -moved, or -dragged event.
- [class func enterExitEvent(with: NSEvent.EventType, location: NSPoint, modifierFlags: NSEvent.ModifierFlags, timestamp: TimeInterval, windowNumber: Int, context: NSGraphicsContext?, eventNumber: Int, trackingNumber: Int, userData: UnsafeMutableRawPointer?) -> NSEvent?](./enterexitevent%28with,location,modifierflags,timestamp,windownumber,context,eventnumber,trackingnumber,userdata%29.md)
  Creates and returns a new event object that describes a tracking-rectangle or cursor-update event.
- [class func otherEvent(with: NSEvent.EventType, location: NSPoint, modifierFlags: NSEvent.ModifierFlags, timestamp: TimeInterval, windowNumber: Int, context: NSGraphicsContext?, subtype: Int16, data1: Int, data2: Int) -> NSEvent?](./otherevent%28with,location,modifierflags,timestamp,windownumber,context,subtype,data1,data2%29.md)
  Creates and returns a new event object that describes a custom event.
- [init?(cgEvent: CGEvent)](./init%28cgevent%29-4igjn.md)
  Creates and returns an event object for a Core Graphics event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/init(eventref:))*