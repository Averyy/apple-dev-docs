# windowControllerWillLoadNib(_:)

**Framework**: AppKit  
**Kind**: method

Called before one of the document’s window controllers loads its nib file.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func windowControllerWillLoadNib(_ windowController: NSWindowController)
```

#### Discussion

See the class description for [`NSWindowController`](nswindowcontroller.md) for additional information about nib files and the file’s owner object.

Typically an `NSDocument` subclass overrides [`windowNibName`](nsdocument/windownibname.md) or [`makeWindowControllers()`](nsdocument/makewindowcontrollers().md), but not both. If [`windowNibName`](nsdocument/windownibname.md) is overridden, the default implementation of [`makeWindowControllers()`](nsdocument/makewindowcontrollers().md) will load the named nib file, making the NSDocument the nib file’s owner. In that case, you can override [`windowControllerWillLoadNib(_:)`](nsdocument/windowcontrollerwillloadnib(_:).md) and do custom processing before the nib file is loaded.

The default implementation of this method does nothing.

## Parameters

- `windowController`: The window controller that loads the nib file.

## See Also

- [func makeWindowControllers()](nsdocument/makewindowcontrollers.md)
  Creates the window controller objects that the document uses to display its content.
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
- [func shouldCloseWindowController(NSWindowController, delegate: Any?, shouldClose: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsdocument/shouldclosewindowcontroller(_:delegate:shouldclose:contextinfo:).md)
  Determines whether the system should close the document and its associated window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/windowcontrollerwillloadnib(_:))*