# performClose(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Simulates the user clicking the close button by momentarily highlighting the button and then closing the window.

**Availability**:
- macOS

## Declaration

```swift
func performClose(_ sender: Any?)
```

```objc
- (void) performClose:(id) sender;
```

## Discussion

If the window’s delegate or the window itself implements [`windowShouldClose(_:)`](../nswindowdelegate/windowshouldclose%28_%29.md), the window sends that message with the window as the argument. The window sends only one such message; if both the delegate and the window implement the method, the delegate receives the message. If the [`windowShouldClose(_:)`](../nswindowdelegate/windowshouldclose%28_%29.md) method returns [`false`](../../Swift/false.md), the window doesn’t close. If neither the window nor the delegate implement [`windowShouldClose(_:)`](../nswindowdelegate/windowshouldclose%28_%29.md), or it returns [`true`](../../Swift/true.md), this method invokes [`close()`](./close%28%29.md) to close the window.

If the window doesn’t have a close button or can’t close (for example, if the delegate replies [`false`](../../Swift/false.md) to a [`windowShouldClose(_:)`](../nswindowdelegate/windowshouldclose%28_%29.md) message), the system emits the alert sound.

## Parameters

- `sender`: The message’s sender.

## See Also

### Related Documentation
- [var styleMask: NSWindow.StyleMask](./stylemask-swift.property.md)
  Flags that describe the window’s current style, such as if it’s resizable or in full-screen mode.
- [func performMiniaturize(Any?)](./performminiaturize%28_%29.md)
  Simulates the user clicking the minimize button by momentarily highlighting the button, then minimizing the window.
### Closing Windows
- [func close()](./close%28%29.md)
  Removes the window from the screen.
- [var isReleasedWhenClosed: Bool](./isreleasedwhenclosed.md)
  A Boolean value that indicates whether the window is released when it receives the `close` message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/performclose(_:))*