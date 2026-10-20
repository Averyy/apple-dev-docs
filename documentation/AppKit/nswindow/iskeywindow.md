# isKeyWindow

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the window is the key window for the application.

**Availability**:
- macOS

## Declaration

```swift
var isKeyWindow: Bool { get }
```

```objc
@property (readonly, getter=isKeyWindow) BOOL keyWindow;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) if the window is the key window for the application; otherwise, [`false`](../../Swift/false.md).

## See Also

### Related Documentation
- [var isMainWindow: Bool](./ismainwindow.md)
  A Boolean value that indicates whether the window is the application’s main window.
### Managing Key Status
- [var canBecomeKey: Bool](./canbecomekey.md)
  A Boolean value that indicates whether the window can become the key window.
- [func makeKey()](./makekey%28%29.md)
  Makes the window the key window.
- [func makeKeyAndOrderFront(Any?)](./makekeyandorderfront%28_%29.md)
  Moves the window to the front of the screen list, within its level, and makes it the key window; that is, it shows the window.
- [func becomeKey()](./becomekey%28%29.md)
  Informs the window that it has become the key window.
- [func resignKey()](./resignkey%28%29.md)
  Resigns the window’s key window status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/iskeywindow)*