# isWindowLoaded

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the nib file containing the receiver’s window has been loaded.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isWindowLoaded: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) if the nib file containing the receiver’s window has been loaded, [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

## See Also

- [func loadWindow()](nswindowcontroller/loadwindow.md)
  Loads the receiver’s window from the nib file.
- [func showWindow(Any?)](nswindowcontroller/showwindow(_:).md)
  Displays the window associated with the receiver.
- [var window: NSWindow?](nswindowcontroller/window.md)
  The window owned by the receiver.
- [func windowDidLoad()](nswindowcontroller/windowdidload.md)
  Sent after the window owned by the receiver has been loaded.
- [func windowWillLoad()](nswindowcontroller/windowwillload.md)
  Sent before the window owned by the receiver is loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowcontroller/iswindowloaded)*