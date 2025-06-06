# makeWindowControllers()

**Framework**: AppKit  
**Kind**: method

Creates the window controller objects that the document uses to display its content.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func makeWindowControllers()
```

#### Discussion

Subclasses may override this method to create the initial window controller(s) for the document.

The base class implementation creates an `NSWindowController` object with [`windowNibName`](nsdocument/windownibname.md) and with the document as the file’s owner if [`windowNibName`](nsdocument/windownibname.md) returns a name. If you override this method to create your own window controllers, be sure to use [`addWindowController(_:)`](nsdocument/addwindowcontroller(_:).md) to add them to the document after creating them.

This method is called by the `NSDocumentController` `open...` methods, but you might want to call it directly in some circumstances.

## See Also

- [func addWindowController(NSWindowController)](nsdocument/addwindowcontroller(_:).md)
  Adds the specified window controller to the current document.
- [func removeWindowController(NSWindowController)](nsdocument/removewindowcontroller(_:).md)
  Removes the specified window controller from the receiver’s array of window controllers.
- [var windowControllers: [NSWindowController]](nsdocument/windowcontrollers.md)
  The document’s current window controllers.
- [var windowNibName: NSNib.Name?](nsdocument/windownibname.md)
  The name of the document’s sole nib file.
- [func windowControllerDidLoadNib(NSWindowController)](nsdocument/windowcontrollerdidloadnib(_:).md)
  Called after one of the document’s window controllers loads its nib file.
- [func windowControllerWillLoadNib(NSWindowController)](nsdocument/windowcontrollerwillloadnib(_:).md)
  Called before one of the document’s window controllers loads its nib file.
- [func shouldCloseWindowController(NSWindowController, delegate: Any?, shouldClose: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsdocument/shouldclosewindowcontroller(_:delegate:shouldclose:contextinfo:).md)
  Determines whether the system should close the document and its associated window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/makewindowcontrollers())*