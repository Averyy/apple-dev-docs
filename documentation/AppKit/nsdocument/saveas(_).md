# saveAs(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

The action method invoked in the receiver as first responder when the user chooses the Save As menu command.

**Availability**:
- macOS

## Declaration

```swift
@IBAction
func saveAs(_ sender: Any?)
```

```objc
- (void) saveDocumentAs:(id) sender;
```

## Discussion

The default implementation runs the modal Save panel to get the file location under which to save the document. It writes the document to this file, sets the document’s file location and document type (if a native type), and clears the document’s edited status.

## Parameters

- `sender`: The control sending the message.

## See Also

### Related Documentation
- [func updateChangeCount(NSDocument.ChangeType)](./updatechangecount%28_%29.md)
  Updates the receiver’s change count according to the given change type.
- [var fileType: String?](./filetype.md)
  The name of the document type, as specified in the app’s information property-list file.
- [var fileURL: URL?](./fileurl.md)
  The location of the document’s on-disk representation.
### Handling User Actions
- [func printDocument(Any?)](./printdocument%28_%29.md)
  Prints the receiver in response to the user choosing the Print menu command.
- [func runPageLayout(Any?)](./runpagelayout%28_%29.md)
  The action method invoked in the receiver as first responder when the user chooses the Page Setup menu command.
- [func revertToSaved(Any?)](./reverttosaved%28_%29.md)
  The action of the File menu item Revert in a document-based app.
- [func save(Any?)](./save%28_%29.md)
  The action method invoked in the receiver as first responder when the user chooses the Save menu command.
- [func saveTo(Any?)](./saveto%28_%29.md)
  The action method invoked in the receiver as first responder when the user chooses the Save To menu command.
- [func save(withDelegate: Any?, didSave: Selector?, contextInfo: UnsafeMutableRawPointer?)](./save%28withdelegate,didsave,contextinfo%29.md)
  Saves the document and delivers the results to the provided delegate object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/saveas(_:))*