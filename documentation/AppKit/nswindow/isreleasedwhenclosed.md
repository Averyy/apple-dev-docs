# isReleasedWhenClosed

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the window is released when it receives the `close` message.

**Availability**:
- macOS

## Declaration

```swift
var isReleasedWhenClosed: Bool { get set }
```

```objc
@property (getter=isReleasedWhenClosed) BOOL releasedWhenClosed;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) if the window is automatically released after being closed; [`false`](../../Swift/false.md) if it’s simply removed from the screen.

The default for `NSWindow` is [`true`](../../Swift/true.md); the default for `NSPanel` is [`false`](../../Swift/false.md). Release when closed, however, is ignored for windows owned by window controllers.

> ⚠️ **Warning**: Swift and Automatic Reference Counting (ARC) clients need to set this property to [`false`](../../Swift/false.md) to avoid releasing the window too many times.

## See Also

### Closing Windows
- [func performClose(Any?)](./performclose%28_%29.md)
  Simulates the user clicking the close button by momentarily highlighting the button and then closing the window.
- [func close()](./close%28%29.md)
  Removes the window from the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/isreleasedwhenclosed)*