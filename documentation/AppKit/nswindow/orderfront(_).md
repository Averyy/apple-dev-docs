# orderFront(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Moves the window to the front of its level in the screen list, without changing either the key window or the main window.

**Availability**:
- macOS

## Declaration

```swift
func orderFront(_ sender: Any?)
```

```objc
- (void) orderFront:(id) sender;
```

#### Discussion

The default animation based on the window type will be used when the window is ordered front unless it has been modified by the [`animationBehavior`](./animationbehavior-swift.property.md) property.

## Parameters

- `sender`: The message’s sender.

## See Also

### Related Documentation
- [func makeKeyAndOrderFront(Any?)](./makekeyandorderfront%28_%29.md)
  Moves the window to the front of the screen list, within its level, and makes it the key window; that is, it shows the window.
### Managing Window Layers
- [func orderOut(Any?)](./orderout%28_%29.md)
  Removes the window from the screen list, which hides the window.
- [func orderBack(Any?)](./orderback%28_%29.md)
  Moves the window to the back of its level in the screen list, without changing either the key window or the main window.
- [func orderFrontRegardless()](./orderfrontregardless%28%29.md)
  Moves the window to the front of its level, even if its application isn’t active, without changing either the key window or the main window.
- [func order(NSWindow.OrderingMode, relativeTo: Int)](./order%28_,relativeto%29.md)
  Repositions the window’s window device in the window server’s screen list.
- [var level: NSWindow.Level](./level-swift.property.md)
  The window level of the window.
- [NSWindow.Level](./level-swift.struct.md)
  The standard window levels in macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/orderfront(_:))*