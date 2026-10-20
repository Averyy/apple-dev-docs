# windowNibName

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The name of the document’s sole nib file.

**Availability**:
- macOS

## Declaration

```swift
var windowNibName: NSNib.Name? { get }
```

```objc
@property (copy, readonly, nullable) NSNibName windowNibName;
```

#### Discussion

Using this name, `NSDocument` creates and instantiates a default instance of `NSWindowController` to manage the window. If your document has multiple nib files, each with its own single window, or if the default `NSWindowController` instance is not adequate for your purposes, you should override [`makeWindowControllers()`](./makewindowcontrollers%28%29.md).

The default value of this property is `nil`. Subclasses must override it to specify a nib file name.

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
- [func windowControllerDidLoadNib(NSWindowController)](./windowcontrollerdidloadnib%28_%29.md)
  Called after one of the document’s window controllers loads its nib file.
- [func windowControllerWillLoadNib(NSWindowController)](./windowcontrollerwillloadnib%28_%29.md)
  Called before one of the document’s window controllers loads its nib file.
- [func shouldCloseWindowController(NSWindowController, delegate: Any?, shouldClose: Selector?, contextInfo: UnsafeMutableRawPointer?)](./shouldclosewindowcontroller%28_,delegate,shouldclose,contextinfo%29.md)
  Determines whether the system should close the document and its associated window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/windownibname)*