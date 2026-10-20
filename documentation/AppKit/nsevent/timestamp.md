# timestamp

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The time when the event occurred in seconds since system startup.

**Availability**:
- macOS

## Declaration

```swift
var timestamp: TimeInterval { get }
```

```objc
@property (readonly) NSTimeInterval timestamp;
```

## See Also

### Related Documentation
- [var systemUptime: TimeInterval](../../Foundation/processinfo/systemuptime.md)
  The amount of time the system has been awake since the last time it was restarted.
### Getting general event information
- [var locationInWindow: NSPoint](./locationinwindow.md)
  The event location in the base coordinate system of the associated window.
- [var window: NSWindow?](./window.md)
  The window object associated with the event.
- [var windowNumber: Int](./windownumber.md)
  The identifier for the window device associated with the event.
- [var eventRef: UnsafeRawPointer?](./eventref.md)
  An opaque Carbon type associated with this event.
- [var cgEvent: CGEvent?](./cgevent.md)
  The Core Graphics event object corresponding to this event.
- [class var foreverDuration: TimeInterval](./foreverduration.md)
  The longest time duration possible.
- [var context: NSGraphicsContext?](./context.md)
  The display graphics context for this event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/timestamp)*