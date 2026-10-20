# orderFrontRegardless()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Moves the window to the front of its level, even if its application isn’t active, without changing either the key window or the main window.

**Availability**:
- macOS

## Declaration

```swift
func orderFrontRegardless()
```

```objc
- (void) orderFrontRegardless;
```

#### Discussion

Normally an `NSWindow` object can’t be moved in front of the key window unless it and the key window are in the same application. You should rarely need to invoke this method; it’s designed to be used when applications are cooperating in such a way that an active application (with the key window) is using another application to display data.

## See Also

### Managing Window Layers
- [func orderOut(Any?)](./orderout%28_%29.md)
  Removes the window from the screen list, which hides the window.
- [func orderBack(Any?)](./orderback%28_%29.md)
  Moves the window to the back of its level in the screen list, without changing either the key window or the main window.
- [func orderFront(Any?)](./orderfront%28_%29.md)
  Moves the window to the front of its level in the screen list, without changing either the key window or the main window.
- [func order(NSWindow.OrderingMode, relativeTo: Int)](./order%28_,relativeto%29.md)
  Repositions the window’s window device in the window server’s screen list.
- [var level: NSWindow.Level](./level-swift.property.md)
  The window level of the window.
- [NSWindow.Level](./level-swift.struct.md)
  The standard window levels in macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/orderfrontregardless())*