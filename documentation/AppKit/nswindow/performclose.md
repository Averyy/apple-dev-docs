# performClose(_:)

**Framework**: AppKit  
**Kind**: method

Simulates the user clicking the close button by momentarily highlighting the button and then closing the window.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func performClose(_ sender: Any?)
```

#### Discussion

If the window’s delegate or the window itself implements [`windowShouldClose(_:)`](nswindowdelegate/windowshouldclose(_:).md), the window sends that message with the window as the argument. The window sends only one such message; if both the delegate and the window implement the method, the delegate receives the message. If the [`windowShouldClose(_:)`](nswindowdelegate/windowshouldclose(_:).md) method returns [`false`](https://developer.apple.com/documentation/swift/false), the window doesn’t close. If neither the window nor the delegate implement [`windowShouldClose(_:)`](nswindowdelegate/windowshouldclose(_:).md), or it returns [`true`](https://developer.apple.com/documentation/swift/true), this method invokes [`close()`](nswindow/close().md) to close the window.

If the window doesn’t have a close button or can’t close (for example, if the delegate replies [`false`](https://developer.apple.com/documentation/swift/false) to a [`windowShouldClose(_:)`](nswindowdelegate/windowshouldclose(_:).md) message), the system emits the alert sound.

## Parameters

- `sender`: The message’s sender.

## See Also

- [var styleMask: NSWindow.StyleMask](nswindow/stylemask-swift.property.md)
  Flags that describe the window’s current style, such as if it’s resizable or in full-screen mode.
- [func performMiniaturize(Any?)](nswindow/performminiaturize(_:).md)
  Simulates the user clicking the minimize button by momentarily highlighting the button, then minimizing the window.
- [func close()](nswindow/close.md)
  Removes the window from the screen.
- [var isReleasedWhenClosed: Bool](nswindow/isreleasedwhenclosed.md)
  A Boolean value that indicates whether the window is released when it receives the `close` message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/performclose(_:))*