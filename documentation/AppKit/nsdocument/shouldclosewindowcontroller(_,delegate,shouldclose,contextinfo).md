# shouldCloseWindowController(_:delegate:shouldClose:contextInfo:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Determines whether the system should close the document and its associated window.

**Availability**:
- macOS

## Declaration

```swift
func shouldCloseWindowController(_ windowController: NSWindowController, delegate: Any?, shouldClose shouldCloseSelector: Selector?, contextInfo: UnsafeMutableRawPointer?)
```

```objc
- (void) shouldCloseWindowController:(NSWindowController *) windowController delegate:(id) delegate shouldCloseSelector:(SEL) shouldCloseSelector contextInfo:(void *) contextInfo;
```

#### Discussion

If the window controller is the document’s last one, or is marked as causing the document to close, this method calls the method in the `shouldCloseSelector` parameter with the result of [`canClose(withDelegate:shouldClose:contextInfo:)`](./canclose%28withdelegate,shouldclose,contextinfo%29.md). In all other cases, this method calls `shouldCloseSelector` with [`true`](../../Swift/true.md). This method is called automatically by [`NSWindow`](../nswindow.md) for any window that has a window controller and a document associated with it. `NSWindow` calls this method prior to sending its `delegate` the [`windowShouldClose(_:)`](../nswindowdelegate/windowshouldclose%28_%29.md) message. Pass the `contextInfo` object with the callback.

The `shouldCloseSelector` callback method should have the following signature:

```objc
- (void)document:(NSDocument *)document shouldClose:(BOOL)shouldClose  contextInfo:(void  *)contextInfo
```

## Parameters

- `windowController`: The window controller that is closed.
- `delegate`: The delegate to which the selector message is sent.
- `shouldCloseSelector`: The selector of the message sent to the delegate.
- `contextInfo`: Object passed with the callback to provide any additional context information.

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
- [func windowControllerDidLoadNib(NSWindowController)](./windowcontrollerdidloadnib%28_%29.md)
  Called after one of the document’s window controllers loads its nib file.
- [func windowControllerWillLoadNib(NSWindowController)](./windowcontrollerwillloadnib%28_%29.md)
  Called before one of the document’s window controllers loads its nib file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/shouldclosewindowcontroller(_:delegate:shouldclose:contextinfo:))*