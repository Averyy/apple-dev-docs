# windowNibName

**Framework**: AppKit  
**Kind**: property

The name of the document’s sole nib file.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var windowNibName: NSNib.Name? { get }
```

#### Discussion

Using this name, `NSDocument` creates and instantiates a default instance of `NSWindowController` to manage the window. If your document has multiple nib files, each with its own single window, or if the default `NSWindowController` instance is not adequate for your purposes, you should override [`makeWindowControllers()`](nsdocument/makewindowcontrollers().md).

The default value of this property is `nil`. Subclasses must override it to specify a nib file name.

## See Also

- [func makeWindowControllers()](nsdocument/makewindowcontrollers.md)
  Creates the window controller objects that the document uses to display its content.
- [func addWindowController(NSWindowController)](nsdocument/addwindowcontroller(_:).md)
  Adds the specified window controller to the current document.
- [func removeWindowController(NSWindowController)](nsdocument/removewindowcontroller(_:).md)
  Removes the specified window controller from the receiver’s array of window controllers.
- [var windowControllers: [NSWindowController]](nsdocument/windowcontrollers.md)
  The document’s current window controllers.
- [func windowControllerDidLoadNib(NSWindowController)](nsdocument/windowcontrollerdidloadnib(_:).md)
  Called after one of the document’s window controllers loads its nib file.
- [func windowControllerWillLoadNib(NSWindowController)](nsdocument/windowcontrollerwillloadnib(_:).md)
  Called before one of the document’s window controllers loads its nib file.
- [func shouldCloseWindowController(NSWindowController, delegate: Any?, shouldClose: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsdocument/shouldclosewindowcontroller(_:delegate:shouldclose:contextinfo:).md)
  Determines whether the system should close the document and its associated window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/windownibname)*