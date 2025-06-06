# save(withDelegate:didSave:contextInfo:)

**Framework**: AppKit  
**Kind**: method

Saves the document and delivers the results to the provided delegate object.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func save(withDelegate delegate: Any?, didSave didSaveSelector: Selector?, contextInfo: UnsafeMutableRawPointer?)
```

#### Discussion

If an [`NSDocument.SaveOperationType.saveOperation`](nsdocument/saveoperationtype/saveoperation.md) can be performed without further user intervention (at the very least, neither [`fileURL`](nsdocument/fileurl.md) nor [`fileType`](nsdocument/filetype.md) are `nil`), then the method immediately saves the document. Otherwise, it presents a Save panel to the user and saves the document if the user approves the panel. When saving has been completed or canceled, the method sends the message selected by `didSaveSelector` to the `delegate`, with the `contextInfo` as the last argument.

As of OS X v10.5, this method checks to see if the document’s file has been modified since the document was opened or most recently saved or reverted, in addition to the checking for file moving, renaming, and trashing that it has done since OS X v10.1. When it senses file modification it presents an alert telling the user “This document’s file has been changed by another app since you opened or saved it,” giving them the choice of saving or not saving. For backward binary compatibility this is only done in apps linked against macOS 10.5 or later.

The `didSaveSelector` callback method should have the following signature:

```objc
- (void)document:(NSDocument *)doc didSave:(BOOL)didSave contextInfo:(void  *)contextInfo
```

## Parameters

- `delegate`: The delegate to which the selector message is sent.
- `didSaveSelector`: The selector of the message sent to the delegate.
- `contextInfo`: Object passed with the callback to provide any additional context information.

## See Also

- [func printDocument(Any?)](nsdocument/printdocument(_:).md)
  Prints the receiver in response to the user choosing the Print menu command.
- [func runPageLayout(Any?)](nsdocument/runpagelayout(_:).md)
  The action method invoked in the receiver as first responder when the user chooses the Page Setup menu command.
- [func revertToSaved(Any?)](nsdocument/reverttosaved(_:).md)
  The action of the File menu item Revert in a document-based app.
- [func save(Any?)](nsdocument/save(_:).md)
  The action method invoked in the receiver as first responder when the user chooses the Save menu command.
- [func saveAs(Any?)](nsdocument/saveas(_:).md)
  The action method invoked in the receiver as first responder when the user chooses the Save As menu command.
- [func saveTo(Any?)](nsdocument/saveto(_:).md)
  The action method invoked in the receiver as first responder when the user chooses the Save To menu command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/save(withdelegate:didsave:contextinfo:))*