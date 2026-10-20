# addWindowController(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds the specified window controller to the current document.

**Availability**:
- macOS

## Declaration

```swift
func addWindowController(_ windowController: NSWindowController)
```

```objc
- (void) addWindowController:(NSWindowController *) windowController;
```

#### Discussion

An [`NSDocument`](../nsdocument.md) object uses its list of window controllers when it displays all document windows, sets window edited status upon an undo or redo operation, and modifies window titles. If you create window controllers by overriding [`windowNibName`](./windownibname.md), this method is invoked automatically. If you create window controllers in [`makeWindowControllers()`](./makewindowcontrollers%28%29.md) or in any other context, such as in apps that present multiple windows per document, you should invoke this method for each window controller created.

You cannot attach a window controller to more than one document at a time. The default implementation of this method removes the passed-in window controller from the document to which it is attached, if it is already attached to one, then sends it a [`document`](../nswindowcontroller/document.md) message with `self` as the argument. It also ignores redundant invocations.

You would not typically override this method.

## Parameters

- `windowController`: The window controller that is added.

## See Also

### Related Documentation
- [var document: AnyObject?](../nswindowcontroller/document.md)
  The document associated with the window controller.
### Creating and Managing Window Controllers
- [func makeWindowControllers()](./makewindowcontrollers%28%29.md)
  Creates the window controller objects that the document uses to display its content.
- [func removeWindowController(NSWindowController)](./removewindowcontroller%28_%29.md)
  Removes the specified window controller from the receiver’s array of window controllers.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/addwindowcontroller(_:))*