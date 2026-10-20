# removeWindowController(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes the specified window controller from the receiver’s array of window controllers.

**Availability**:
- macOS

## Declaration

```swift
func removeWindowController(_ windowController: NSWindowController)
```

```objc
- (void) removeWindowController:(NSWindowController *) windowController;
```

#### Discussion

A document with no window controllers is not necessarily closed. However, a window controller can be set to close its associated document when the window is closed or the window controller is deallocated.

The default implementation of this method sends a [`document`](../nswindowcontroller/document.md) message to the passed-in window controller with a `nil` argument. You would not typically override this method.

## Parameters

- `windowController`: The window controller that is removed.

## See Also

### Related Documentation
- [var shouldCloseDocument: Bool](../nswindowcontroller/shouldclosedocument.md)
  A Boolean value that indicates whether the receiver necessarily closes the associated document when the window it manages is closed.
### Creating and Managing Window Controllers
- [func makeWindowControllers()](./makewindowcontrollers%28%29.md)
  Creates the window controller objects that the document uses to display its content.
- [func addWindowController(NSWindowController)](./addwindowcontroller%28_%29.md)
  Adds the specified window controller to the current document.
- [var windowControllers: [NSWindowController]](./windowcontrollers.md)
  The document’s current window controllers.
- [var windowNibName: NSNib.Name?](./windownibname.md)
  The name of the document’s sole nib file.
- [func windowControllerDidLoadNib(NSWindowController)](./windowcontrollerdidloadnib%28_%29.md)
  Called after one of the document’s window controllers loads its nib file.
- [func windowControllerWillLoadNib(NSWindowController)](./windowcontrollerwillloadnib%28_%29.md)
  Called before one of the document’s window controllers loads its nib file.
- [func shouldCloseWindowController(NSWindowController, delegate: Any?, shouldClose: Selector?, contextInfo: UnsafeMutableRawPointer?)](./shouldclosewindowcontroller%28_,delegate,shouldclose,contextinfo%29.md)
  Determines whether the system should close the document and its associated window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/removewindowcontroller(_:))*