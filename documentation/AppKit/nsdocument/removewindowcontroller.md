# removeWindowController(_:)

**Framework**: AppKit  
**Kind**: method

Removes the specified window controller from the receiver’s array of window controllers.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func removeWindowController(_ windowController: NSWindowController)
```

#### Discussion

A document with no window controllers is not necessarily closed. However, a window controller can be set to close its associated document when the window is closed or the window controller is deallocated.

The default implementation of this method sends a [`document`](nswindowcontroller/document.md) message to the passed-in window controller with a `nil` argument. You would not typically override this method.

## Parameters

- `windowController`: The window controller that is removed.

## See Also

- [var shouldCloseDocument: Bool](nswindowcontroller/shouldclosedocument.md)
  A Boolean value that indicates whether the receiver necessarily closes the associated document when the window it manages is closed.
- [func makeWindowControllers()](nsdocument/makewindowcontrollers.md)
  Creates the window controller objects that the document uses to display its content.
- [func addWindowController(NSWindowController)](nsdocument/addwindowcontroller(_:).md)
  Adds the specified window controller to the current document.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/removewindowcontroller(_:))*