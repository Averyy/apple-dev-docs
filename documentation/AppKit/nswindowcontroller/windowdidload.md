# windowDidLoad()

**Framework**: AppKit  
**Kind**: method

Sent after the window owned by the receiver has been loaded.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func windowDidLoad()
```

#### Discussion

The default implementation does nothing.

## See Also

- [class NSWindowController](nswindowcontroller.md)
  A controller that manages a window, usually a window stored in a nib file.
- [func loadWindow()](nswindowcontroller/loadwindow.md)
  Loads the receiver’s window from the nib file.
- [func showWindow(Any?)](nswindowcontroller/showwindow(_:).md)
  Displays the window associated with the receiver.
- [var isWindowLoaded: Bool](nswindowcontroller/iswindowloaded.md)
  A Boolean value that indicates whether the nib file containing the receiver’s window has been loaded.
- [var window: NSWindow?](nswindowcontroller/window.md)
  The window owned by the receiver.
- [func windowWillLoad()](nswindowcontroller/windowwillload.md)
  Sent before the window owned by the receiver is loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowcontroller/windowdidload())*