# init(cgEvent:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates and returns an event object for a Core Graphics event.

**Availability**:
- macOS 10.5+

## Declaration

```swift
init?(cgEvent: CGEvent)
```

```objc
+ (NSEvent *) eventWithCGEvent:(CGEventRef) cgEvent;
```

## Return Value

An autoreleased `NSEvent` object that is equivalent to `cgEvent`.

## Discussion

The returned object retains the `CGEventRef` object (`cgEvent`) until it (the Objective-C object) is freed—it then releases the `CGEventRef` object.  If no Cocoa event corresponds to the `CGEventRef` object, this method returns `nil`.

## Parameters

- `cgEvent`: A [`CGEvent`](../../CoreGraphics/cgevent.md) opaque type that represents an event.

## See Also

### Related Documentation
- [var cgEvent: CGEvent?](./cgevent.md)
  The Core Graphics event object corresponding to this event.
### Creating an event object
- [class func keyEvent(with: NSEvent.EventType, location: NSPoint, modifierFlags: NSEvent.ModifierFlags, timestamp: TimeInterval, windowNumber: Int, context: NSGraphicsContext?, characters: String, charactersIgnoringModifiers: String, isARepeat: Bool, keyCode: UInt16) -> NSEvent?](./keyevent%28with,location,modifierflags,timestamp,windownumber,context,characters,charactersignoringmodifiers,isarepeat,keycode%29.md)
  Creates and returns a new event object that describes a key event.
- [class func mouseEvent(with: NSEvent.EventType, location: NSPoint, modifierFlags: NSEvent.ModifierFlags, timestamp: TimeInterval, windowNumber: Int, context: NSGraphicsContext?, eventNumber: Int, clickCount: Int, pressure: Float) -> NSEvent?](./mouseevent%28with,location,modifierflags,timestamp,windownumber,context,eventnumber,clickcount,pressure%29.md)
  Creates and returns a new event object that describes a mouse-down, -up, -moved, or -dragged event.
- [class func enterExitEvent(with: NSEvent.EventType, location: NSPoint, modifierFlags: NSEvent.ModifierFlags, timestamp: TimeInterval, windowNumber: Int, context: NSGraphicsContext?, eventNumber: Int, trackingNumber: Int, userData: UnsafeMutableRawPointer?) -> NSEvent?](./enterexitevent%28with,location,modifierflags,timestamp,windownumber,context,eventnumber,trackingnumber,userdata%29.md)
  Creates and returns a new event object that describes a tracking-rectangle or cursor-update event.
- [class func otherEvent(with: NSEvent.EventType, location: NSPoint, modifierFlags: NSEvent.ModifierFlags, timestamp: TimeInterval, windowNumber: Int, context: NSGraphicsContext?, subtype: Int16, data1: Int, data2: Int) -> NSEvent?](./otherevent%28with,location,modifierflags,timestamp,windownumber,context,subtype,data1,data2%29.md)
  Creates and returns a new event object that describes a custom event.
- [init?(eventRef: UnsafeRawPointer)](./init%28eventref%29.md)
  Creates and returns a new event object for a Carbon event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/init(cgevent:)-4igjn)*