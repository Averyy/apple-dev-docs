# window

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The window owned by the receiver.

**Availability**:
- macOS

## Declaration

```swift
var window: NSWindow? { get set }
```

```objc
@property (strong, nullable) NSWindow * window;
```

## Discussion

Accessing this property loads the nib file if there is one and it has not yet been loaded. If the window was loaded, the following methods are called in order: [`windowWillLoad()`](./windowwillload%28%29.md), [`loadWindow()`](./loadwindow%28%29.md), and [`windowDidLoad()`](./windowdidload%28%29.md). If the window controller has a document, the document’s corresponding methods [`windowControllerWillLoadNib(_:)`](../nsdocument/windowcontrollerwillloadnib%28_%29.md) and [`windowControllerDidLoadNib(_:)`](../nsdocument/windowcontrollerdidloadnib%28_%29.md) are also called (if implemented). To affect nib loading or do something before or after it happens, you should always override these methods.

Setting this property releases the window controller’s old window along with any associated top-level objects in its nib file, and establishes ownership of the specified new window. Typically, you should not use this property to set the window. Instead, create a new window controller for the new window and then release the old window controller.

## See Also

### Related Documentation
- [func windowControllerWillLoadNib(NSWindowController)](../nsdocument/windowcontrollerwillloadnib%28_%29.md)
  Called before one of the document’s window controllers loads its nib file.
### Loading and Displaying the Window
- [func loadWindow()](./loadwindow%28%29.md)
  Loads the receiver’s window from the nib file.
- [func showWindow(Any?)](./showwindow%28_%29.md)
  Displays the window associated with the receiver.
- [var isWindowLoaded: Bool](./iswindowloaded.md)
  A Boolean value that indicates whether the nib file containing the receiver’s window has been loaded.
- [func windowDidLoad()](./windowdidload%28%29.md)
  Sent after the window owned by the receiver has been loaded.
- [func windowWillLoad()](./windowwillload%28%29.md)
  Sent before the window owned by the receiver is loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowcontroller/window)*