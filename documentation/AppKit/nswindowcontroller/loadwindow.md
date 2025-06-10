# loadWindow()

**Framework**: AppKit  
**Kind**: method

Loads the receiver’s window from the nib file.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func loadWindow()
```

#### Discussion

You should never directly invoke this method. Instead, access the [`window`](nswindowcontroller/window.md) property so the [`windowDidLoad()`](nswindowcontroller/windowdidload().md) and [`windowWillLoad()`](nswindowcontroller/windowwillload().md) methods are invoked. Subclasses can override this method if the way it finds and loads the window is not adequate. It uses the [`Bundle`](https://developer.apple.com/documentation/Foundation/Bundle) class’s [`init(for:)`](https://developer.apple.com/documentation/Foundation/Bundle/init(for:)) method to get the bundle, using the class of the nib file owner as argument. It then locates the nib file within the bundle and, if successful, loads it; if unsuccessful, it tries to find the nib file in the main bundle.

## See Also

- [func showWindow(Any?)](nswindowcontroller/showwindow(_:).md)
  Displays the window associated with the receiver.
- [var isWindowLoaded: Bool](nswindowcontroller/iswindowloaded.md)
  A Boolean value that indicates whether the nib file containing the receiver’s window has been loaded.
- [var window: NSWindow?](nswindowcontroller/window.md)
  The window owned by the receiver.
- [func windowDidLoad()](nswindowcontroller/windowdidload.md)
  Sent after the window owned by the receiver has been loaded.
- [func windowWillLoad()](nswindowcontroller/windowwillload.md)
  Sent before the window owned by the receiver is loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowcontroller/loadwindow())*