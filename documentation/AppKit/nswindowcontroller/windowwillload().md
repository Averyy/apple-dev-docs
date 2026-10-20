# windowWillLoad()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sent before the window owned by the receiver is loaded.

**Availability**:
- macOS

## Declaration

```swift
func windowWillLoad()
```

```objc
- (void) windowWillLoad;
```

#### Discussion

The default implementation does nothing.

## See Also

### Related Documentation
- [class NSWindowController](../nswindowcontroller.md)
  A controller that manages a window, usually a window stored in a nib file.
### Loading and Displaying the Window
- [func loadWindow()](./loadwindow%28%29.md)
  Loads the receiver’s window from the nib file.
- [func showWindow(Any?)](./showwindow%28_%29.md)
  Displays the window associated with the receiver.
- [var isWindowLoaded: Bool](./iswindowloaded.md)
  A Boolean value that indicates whether the nib file containing the receiver’s window has been loaded.
- [var window: NSWindow?](./window.md)
  The window owned by the receiver.
- [func windowDidLoad()](./windowdidload%28%29.md)
  Sent after the window owned by the receiver has been loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowcontroller/windowwillload())*