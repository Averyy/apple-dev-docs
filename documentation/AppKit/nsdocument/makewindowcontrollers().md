# makeWindowControllers()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Creates the window controller objects that the document uses to display its content.

**Availability**:
- macOS

## Declaration

```swift
func makeWindowControllers()
```

```objc
- (void) makeWindowControllers;
```

#### Discussion

Subclasses may override this method to create the initial window controller(s) for the document.

The base class implementation creates an `NSWindowController` object with [`windowNibName`](./windownibname.md) and with the document as the file’s owner if [`windowNibName`](./windownibname.md) returns a name. If you override this method to create your own window controllers, be sure to use [`addWindowController(_:)`](./addwindowcontroller%28_%29.md) to add them to the document after creating them.

This method is called by the `NSDocumentController` `open...` methods, but you might want to call it directly in some circumstances.

## See Also

### Creating and Managing Window Controllers
- [func addWindowController(NSWindowController)](./addwindowcontroller%28_%29.md)
  Adds the specified window controller to the current document.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/makewindowcontrollers())*