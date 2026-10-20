# windowShouldClose(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the user has attempted to close a window or the window has received a [`performClose(_:)`](../nswindow/performclose%28_%29.md) message.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func windowShouldClose(_ sender: NSWindow) -> Bool
```

```objc
- (BOOL) windowShouldClose:(NSWindow *) sender;
```

#### Return Value

[`true`](../../Swift/true.md) to allow `sender` to be closed; otherwise, [`false`](../../Swift/false.md).

#### Discussion

This method may not always be called during window closing. Specifically, this method is not called when a user quits an application.

## Parameters

- `sender`: The window being closed.

## See Also

### Closing Windows
- [func windowWillClose(Notification)](./windowwillclose%28_%29.md)
  Tells the delegate that the window is about to close.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowshouldclose(_:))*