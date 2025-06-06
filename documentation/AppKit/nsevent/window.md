# window

**Framework**: AppKit  
**Kind**: property

The window object associated with the event.

**Availability**:
- macOS ?+

## Declaration

```swift
weak var window: NSWindow? { get }
```

#### Discussion

Periodic events do not have a window. The result of accessing this property on a periodic event is undefined.

## See Also

- [var locationInWindow: NSPoint](nsevent/locationinwindow.md)
  The event location in the base coordinate system of the associated window.
- [var timestamp: TimeInterval](nsevent/timestamp.md)
  The time when the event occurred in seconds since system startup.
- [var windowNumber: Int](nsevent/windownumber.md)
  The identifier for the window device associated with the event.
- [var eventRef: UnsafeRawPointer?](nsevent/eventref.md)
  An opaque Carbon type associated with this event.
- [var cgEvent: CGEvent?](nsevent/cgevent.md)
  The Core Graphics event object corresponding to this event.
- [class let foreverDuration: TimeInterval](nsevent/foreverduration.md)
  The longest time duration possible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/window)*