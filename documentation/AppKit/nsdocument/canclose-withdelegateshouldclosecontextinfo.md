# canClose(withDelegate:shouldClose:contextInfo:)

**Framework**: AppKit  
**Kind**: method

Determines whether to close the document, prompting the user as needed to choose a course of action.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func canClose(withDelegate delegate: Any, shouldClose shouldCloseSelector: Selector?, contextInfo: UnsafeMutableRawPointer?)
```

#### Discussion

If the document is not dirty, this method immediately calls the `shouldCloseSelector` callback on the specified delegate with [`true`](https://developer.apple.com/documentation/Swift/true).

If the document is dirty, an alert is presented giving the user a chance to save, not save, or cancel. If the user chooses to save, this method saves the document. If the save completes successfully, this method calls the callback with [`true`](https://developer.apple.com/documentation/Swift/true). If the save is canceled or otherwise unsuccessful, this method calls the callback with [`false`](https://developer.apple.com/documentation/Swift/false). This method may be called by [`shouldCloseWindowController(_:delegate:shouldClose:contextInfo:)`](nsdocument/shouldclosewindowcontroller(_:delegate:shouldclose:contextinfo:).md). It is also called by the `NSDocumentController` method [`closeAllDocuments(withDelegate:didCloseAllSelector:contextInfo:)`](nsdocumentcontroller/closealldocuments(withdelegate:didcloseallselector:contextinfo:).md). You should call it before you call [`close()`](nsdocument/close().md) if you are closing the document and want to give the user a chance to save any edits. Pass the `contextInfo` object with the callback.

The `shouldCloseSelector` callback method should have the following signature:

```objc
- (void)document:(NSDocument *)doc shouldClose:(BOOL)shouldClose  contextInfo:(void  *)contextInfo
```

## Parameters

- `delegate`: The delegate to which the selector message is sent.
- `shouldCloseSelector`: The selector of the message sent to the delegate.
- `contextInfo`: Object passed with the callback to provide any additional context information.

## See Also

- [func close()](nsdocument/close.md)
  Closes all of the document’s windows and removes the document from its document controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/canclose(withdelegate:shouldclose:contextinfo:))*