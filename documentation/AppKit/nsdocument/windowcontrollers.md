# windowControllers

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The document’s current window controllers.

**Availability**:
- macOS

## Declaration

```swift
var windowControllers: [NSWindowController] { get }
```

```objc
@property (copy, readonly) NSArray<__kindof NSWindowController *> * windowControllers;
```

#### Discussion

The value of this property is an array of [`NSWindowController`](../nswindowcontroller.md) objects belonging to the current document. If there are no window controllers, the value is an empty array object.

## See Also

### Creating and Managing Window Controllers
- [func makeWindowControllers()](./makewindowcontrollers%28%29.md)
  Creates the window controller objects that the document uses to display its content.
- [func addWindowController(NSWindowController)](./addwindowcontroller%28_%29.md)
  Adds the specified window controller to the current document.
- [func removeWindowController(NSWindowController)](./removewindowcontroller%28_%29.md)
  Removes the specified window controller from the receiver’s array of window controllers.
- [var windowNibName: NSNib.Name?](./windownibname.md)
  The name of the document’s sole nib file.
- [func windowControllerDidLoadNib(NSWindowController)](./windowcontrollerdidloadnib%28_%29.md)
  Called after one of the document’s window controllers loads its nib file.
- [func windowControllerWillLoadNib(NSWindowController)](./windowcontrollerwillloadnib%28_%29.md)
  Called before one of the document’s window controllers loads its nib file.
- [func shouldCloseWindowController(NSWindowController, delegate: Any?, shouldClose: Selector?, contextInfo: UnsafeMutableRawPointer?)](./shouldclosewindowcontroller%28_,delegate,shouldclose,contextinfo%29.md)
  Determines whether the system should close the document and its associated window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/windowcontrollers)*