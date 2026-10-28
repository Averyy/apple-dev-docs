# cgEvent

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The Core Graphics event object corresponding to this event.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var cgEvent: CGEvent? { get }
```

```objc
@property (readonly, nullable) CGEventRef CGEvent;
```

## Discussion

The [`CGEvent`](../../CoreGraphics/cgevent.md) opaque type returned is autoreleased. If no `CGEventRef` object corresponding to the `NSEvent` object can be created, this method returns `NULL`.

## See Also

### Related Documentation
- [init?(cgEvent: CGEvent)](./init%28cgevent%29-4igjn.md)
  Creates and returns an event object for a Core Graphics event.
### Getting general event information
- [var locationInWindow: NSPoint](./locationinwindow.md)
  The event location in the base coordinate system of the associated window.
- [var timestamp: TimeInterval](./timestamp.md)
  The time when the event occurred in seconds since system startup.
- [var window: NSWindow?](./window.md)
  The window object associated with the event.
- [var windowNumber: Int](./windownumber.md)
  The identifier for the window device associated with the event.
- [var eventRef: UnsafeRawPointer?](./eventref.md)
  An opaque Carbon type associated with this event.
- [class var foreverDuration: TimeInterval](./foreverduration.md)
  The longest time duration possible.
- [var context: NSGraphicsContext?](./context.md)
  The display graphics context for this event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/cgevent)*