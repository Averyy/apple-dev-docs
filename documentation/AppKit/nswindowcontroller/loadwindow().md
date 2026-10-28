# loadWindow()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Loads the receiver’s window from the nib file.

**Availability**:
- macOS

## Declaration

```swift
func loadWindow()
```

```objc
- (void) loadWindow;
```

## Discussion

You should never directly invoke this method. Instead, access the [`window`](./window.md) property so the [`windowDidLoad()`](./windowdidload%28%29.md) and [`windowWillLoad()`](./windowwillload%28%29.md) methods are invoked. Subclasses can override this method if the way it finds and loads the window is not adequate. It uses the [`Bundle`](../../Foundation/bundle.md) class’s [`init(for:)`](../../Foundation/bundle/init%28for%29.md) method to get the bundle, using the class of the nib file owner as argument. It then locates the nib file within the bundle and, if successful, loads it; if unsuccessful, it tries to find the nib file in the main bundle.

## See Also

### Loading and Displaying the Window
- [func showWindow(Any?)](./showwindow%28_%29.md)
  Displays the window associated with the receiver.
- [var isWindowLoaded: Bool](./iswindowloaded.md)
  A Boolean value that indicates whether the nib file containing the receiver’s window has been loaded.
- [var window: NSWindow?](./window.md)
  The window owned by the receiver.
- [func windowDidLoad()](./windowdidload%28%29.md)
  Sent after the window owned by the receiver has been loaded.
- [func windowWillLoad()](./windowwillload%28%29.md)
  Sent before the window owned by the receiver is loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowcontroller/loadwindow())*