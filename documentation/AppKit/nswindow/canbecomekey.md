# canBecomeKey

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the window can become the key window.

**Availability**:
- macOS

## Declaration

```swift
var canBecomeKey: Bool { get }
```

```objc
@property (readonly) BOOL canBecomeKeyWindow;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) if the window can become the key window, otherwise, [`false`](../../Swift/false.md).

Attempts to make the window the key window are abandoned if the value of this property is [`false`](../../Swift/false.md). The value of this property is [`true`](../../Swift/true.md) if the window’s style mask includes the [`titled`](./stylemask-swift.struct/titled.md) flag, or [`false`](../../Swift/false.md) otherwise.

> **Note**:  To make a window key without including the `titled` flag in its style mask, override this property in an [`NSWindow`](../nswindow.md) subclass to return [`true`](../../Swift/true.md).

## See Also

### Managing Key Status
- [var isKeyWindow: Bool](./iskeywindow.md)
  A Boolean value that indicates whether the window is the key window for the application.
- [func makeKey()](./makekey%28%29.md)
  Makes the window the key window.
- [func makeKeyAndOrderFront(Any?)](./makekeyandorderfront%28_%29.md)
  Moves the window to the front of the screen list, within its level, and makes it the key window; that is, it shows the window.
- [func becomeKey()](./becomekey%28%29.md)
  Informs the window that it has become the key window.
- [func resignKey()](./resignkey%28%29.md)
  Resigns the window’s key window status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/canbecomekey)*