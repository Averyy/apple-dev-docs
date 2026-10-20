# closeAllDocuments(withDelegate:didCloseAllSelector:contextInfo:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Iterates through all the open documents and tries to close them one by one using the specified delegate.

**Availability**:
- macOS

## Declaration

```swift
func closeAllDocuments(withDelegate delegate: Any?, didCloseAllSelector: Selector?, contextInfo: UnsafeMutableRawPointer?)
```

```objc
- (void) closeAllDocumentsWithDelegate:(id) delegate didCloseAllSelector:(SEL) didCloseAllSelector contextInfo:(void *) contextInfo;
```

#### Discussion

Each `NSDocument` object is sent [`canClose(withDelegate:shouldClose:contextInfo:)`](../nsdocument/canclose%28withdelegate,shouldclose,contextinfo%29.md), which, if the document is dirty, gives it a chance to refuse to close or to save itself first. This method may ask whether to save or to perform a save.

The `didCloseAllSelector` callback method is called with [`true`](../../Swift/true.md) if all documents are closed, and [`false`](../../Swift/false.md) otherwise. Pass the `contextInfo` object with the callback. The `didCloseAllSelector` callback method should have the following signature:

```objc
- (void)documentController:(NSDocumentController *)docController  didCloseAll:(BOOL)didCloseAll contextInfo:(void *)contextInfo
```

## Parameters

- `delegate`: The object responsible for closing the document.
- `didCloseAllSelector`: The selector to call after all documents have been closed.
- `contextInfo`: A pointer to user-supplied data.

## See Also

### Closing Documents
- [func reviewUnsavedDocuments(withAlertTitle: String?, cancellable: Bool, delegate: Any?, didReviewAllSelector: Selector?, contextInfo: UnsafeMutableRawPointer?)](./reviewunsaveddocuments%28withalerttitle,cancellable,delegate,didreviewallselector,contextinfo%29.md)
  Displays an alert asking if the user wants to review unsaved documents, quit regardless of unsaved documents, or cancel the save operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/closealldocuments(withdelegate:didcloseallselector:contextinfo:))*