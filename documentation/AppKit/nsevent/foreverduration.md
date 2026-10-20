# foreverDuration

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The longest time duration possible.

**Availability**:
- macOS

## Declaration

```swift
class var foreverDuration: TimeInterval { get }
```

```c
static const NSTimeInterval NSEventDurationForever;
```

## See Also

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
- [var cgEvent: CGEvent?](./cgevent.md)
  The Core Graphics event object corresponding to this event.
- [var context: NSGraphicsContext?](./context.md)
  The display graphics context for this event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/foreverduration)*