# windowShouldClose(_:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the user has attempted to close a window or the window has received a [`performClose(_:)`](nswindow/performclose(_:).md) message.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func windowShouldClose(_ sender: NSWindow) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) to allow `sender` to be closed; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

This method may not always be called during window closing. Specifically, this method is not called when a user quits an application.

## Parameters

- `sender`: The window being closed.

## See Also

- [func windowWillClose(Notification)](nswindowdelegate/windowwillclose(_:).md)
  Tells the delegate that the window is about to close.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowshouldclose(_:))*