# windowControllerDidLoadNib(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Called after one of the document’s window controllers loads its nib file.

**Availability**:
- macOS

## Declaration

```swift
func windowControllerDidLoadNib(_ windowController: NSWindowController)
```

```objc
- (void) windowControllerDidLoadNib:(NSWindowController *) windowController;
```

## Discussion

See the class description for [`NSWindowController`](../nswindowcontroller.md) for additional information about nib files and the file’s owner object.

Typically an `NSDocument` subclass overrides [`windowNibName`](./windownibname.md) or [`makeWindowControllers()`](./makewindowcontrollers%28%29.md), but not both. If [`windowNibName`](./windownibname.md) is overridden, the default implementation of [`makeWindowControllers()`](./makewindowcontrollers%28%29.md) will load the named nib file, making the `NSDocument` object the nib file’s owner. In that case, you can override [`windowControllerDidLoadNib(_:)`](./windowcontrollerdidloadnib%28_%29.md) and do custom processing after the nib file is loaded.

The default implementation of this method does nothing.

## Parameters

- `windowController`: The window controller that loaded the nib file.

## See Also

### Creating and Managing Window Controllers
- [func makeWindowControllers()](./makewindowcontrollers%28%29.md)
  Creates the window controller objects that the document uses to display its content.
- [func addWindowController(NSWindowController)](./addwindowcontroller%28_%29.md)
  Adds the specified window controller to the current document.
- [func removeWindowController(NSWindowController)](./removewindowcontroller%28_%29.md)
  Removes the specified window controller from the receiver’s array of window controllers.
- [var windowControllers: [NSWindowController]](./windowcontrollers.md)
  The document’s current window controllers.
- [var windowNibName: NSNib.Name?](./windownibname.md)
  The name of the document’s sole nib file.
- [func windowControllerWillLoadNib(NSWindowController)](./windowcontrollerwillloadnib%28_%29.md)
  Called before one of the document’s window controllers loads its nib file.
- [func shouldCloseWindowController(NSWindowController, delegate: Any?, shouldClose: Selector?, contextInfo: UnsafeMutableRawPointer?)](./shouldclosewindowcontroller%28_,delegate,shouldclose,contextinfo%29.md)
  Determines whether the system should close the document and its associated window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/windowcontrollerdidloadnib(_:))*