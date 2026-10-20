# windowWillClose(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the window is about to close.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func windowWillClose(_ notification: Notification)
```

```objc
- (void) windowWillClose:(NSNotification *) notification;
```

#### Discussion

You can retrieve the `NSWindow` object in question by sending [`object`](../../Foundation/nsnotification/object.md) to `notification`.

## Parameters

- `notification`: A notification named [`willCloseNotification`](../nswindow/willclosenotification.md).

## See Also

### Closing Windows
- [func windowShouldClose(NSWindow) -> Bool](./windowshouldclose%28_%29.md)
  Tells the delegate that the user has attempted to close a window or the window has received a [`performClose(_:)`](../nswindow/performclose%28_%29.md) message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowwillclose(_:))*