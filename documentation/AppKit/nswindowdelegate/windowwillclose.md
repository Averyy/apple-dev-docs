# windowWillClose(_:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the window is about to close.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func windowWillClose(_ notification: Notification)
```

#### Discussion

You can retrieve the `NSWindow` object in question by sending [`object`](https://developer.apple.com/documentation/foundation/nsnotification/1414469-object) to `notification`.

## Parameters

- `notification`: A notification named  .

## See Also

- [func windowShouldClose(NSWindow) -> Bool](nswindowdelegate/windowshouldclose(_:).md)
  Tells the delegate that the user has attempted to close a window or the window has received a [`performClose(_:)`](nswindow/performclose(_:).md) message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowwillclose(_:))*