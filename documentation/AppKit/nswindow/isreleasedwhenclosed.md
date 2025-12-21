# isReleasedWhenClosed

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the window is released when it receives the `close` message.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isReleasedWhenClosed: Bool { get set }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) if the window is automatically released after being closed; [`false`](https://developer.apple.com/documentation/Swift/false) if it’s simply removed from the screen.

The default for `NSWindow` is [`true`](https://developer.apple.com/documentation/Swift/true); the default for `NSPanel` is [`false`](https://developer.apple.com/documentation/Swift/false). Release when closed, however, is ignored for windows owned by window controllers. Another strategy for releasing an `NSWindow` object is to have its delegate autorelease it on receiving a [`windowShouldClose(_:)`](nswindowdelegate/windowshouldclose(_:).md) message.

## See Also

- [func performClose(Any?)](nswindow/performclose(_:).md)
  Simulates the user clicking the close button by momentarily highlighting the button and then closing the window.
- [func close()](nswindow/close.md)
  Removes the window from the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/isreleasedwhenclosed)*