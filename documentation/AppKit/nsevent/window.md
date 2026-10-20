# window

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The window object associated with the event.

**Availability**:
- macOS

## Declaration

```swift
weak var window: NSWindow? { get }
```

```objc
@property (weak, readonly, nullable) NSWindow * window;
```

#### Discussion

Periodic events do not have a window. The result of accessing this property on a periodic event is undefined.

## See Also

### Getting general event information
- [var locationInWindow: NSPoint](./locationinwindow.md)
  The event location in the base coordinate system of the associated window.
- [var timestamp: TimeInterval](./timestamp.md)
  The time when the event occurred in seconds since system startup.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/window)*