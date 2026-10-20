# context

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The display graphics context for this event.

**Availability**:
- macOS 10.0+ - Deprecated in 10.12

> **Deprecated**: This method always returns `nil`. If you need access to the current drawing context, use [`current`](../nsgraphicscontext/current.md) inside of a draw operation.

## Declaration

```swift
var context: NSGraphicsContext? { get }
```

```objc
@property (strong, readonly, nullable) NSGraphicsContext * context;
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
- [class var foreverDuration: TimeInterval](./foreverduration.md)
  The longest time duration possible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/context)*