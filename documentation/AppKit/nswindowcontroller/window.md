# window

**Framework**: AppKit  
**Kind**: property

The window owned by the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var window: NSWindow? { get set }
```

#### Discussion

Accessing this property loads the nib file if there is one and it has not yet been loaded. If the window was loaded, the following methods are called in order: [`windowWillLoad()`](nswindowcontroller/windowwillload().md), [`loadWindow()`](nswindowcontroller/loadwindow().md), and [`windowDidLoad()`](nswindowcontroller/windowdidload().md). If the window controller has a document, the document’s corresponding methods [`windowControllerWillLoadNib(_:)`](nsdocument/windowcontrollerwillloadnib(_:).md) and [`windowControllerDidLoadNib(_:)`](nsdocument/windowcontrollerdidloadnib(_:).md) are also called (if implemented). To affect nib loading or do something before or after it happens, you should always override these methods.

Setting this property releases the window controller’s old window along with any associated top-level objects in its nib file, and establishes ownership of the specified new window. Typically, you should not use this property to set the window. Instead, create a new window controller for the new window and then release the old window controller.

## See Also

- [func windowControllerWillLoadNib(NSWindowController)](nsdocument/windowcontrollerwillloadnib(_:).md)
  Called before one of the document’s window controllers loads its nib file.
- [func loadWindow()](nswindowcontroller/loadwindow.md)
  Loads the receiver’s window from the nib file.
- [func showWindow(Any?)](nswindowcontroller/showwindow(_:).md)
  Displays the window associated with the receiver.
- [var isWindowLoaded: Bool](nswindowcontroller/iswindowloaded.md)
  A Boolean value that indicates whether the nib file containing the receiver’s window has been loaded.
- [func windowDidLoad()](nswindowcontroller/windowdidload.md)
  Sent after the window owned by the receiver has been loaded.
- [func windowWillLoad()](nswindowcontroller/windowwillload.md)
  Sent before the window owned by the receiver is loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowcontroller/window)*