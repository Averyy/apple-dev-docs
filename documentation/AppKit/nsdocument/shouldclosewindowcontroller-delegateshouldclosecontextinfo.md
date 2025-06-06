# shouldCloseWindowController(_:delegate:shouldClose:contextInfo:)

**Framework**: AppKit  
**Kind**: method

Determines whether the system should close the document and its associated window.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func shouldCloseWindowController(_ windowController: NSWindowController, delegate: Any?, shouldClose shouldCloseSelector: Selector?, contextInfo: UnsafeMutableRawPointer?)
```

#### Discussion

If the window controller is the document’s last one, or is marked as causing the document to close, this method calls the method in the `shouldCloseSelector` parameter with the result of [`canClose(withDelegate:shouldClose:contextInfo:)`](nsdocument/canclose(withdelegate:shouldclose:contextinfo:).md). In all other cases, this method calls `shouldCloseSelector` with [`true`](https://developer.apple.com/documentation/swift/true). This method is called automatically by [`NSWindow`](nswindow.md) for any window that has a window controller and a document associated with it. `NSWindow` calls this method prior to sending its `delegate` the [`windowShouldClose(_:)`](nswindowdelegate/windowshouldclose(_:).md) message. Pass the `contextInfo` object with the callback.

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
- [func windowControllerWillLoadNib(NSWindowController)](nsdocument/windowcontrollerwillloadnib(_:).md)
  Called before one of the document’s window controllers loads its nib file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/shouldclosewindowcontroller(_:delegate:shouldclose:contextinfo:))*