# save(_:)

**Framework**: AppKit  
**Kind**: method

The action method invoked in the receiver as first responder when the user chooses the Save menu command.

**Availability**:
- macOS ?+

## Declaration

```swift
@IBAction
@MainActor func save(_ sender: Any?)
```

#### Discussion

The default implementation saves the document in two different ways, depending on whether the document has a file path and a document type assigned. If path and type are assigned, it simply writes the document under its current file path and type after making a backup copy of the previous file. If the document is new (no file path and type), it runs the modal Save panel to get the file location under which to save the document. It writes the document to this file, sets the document’s file location and document type (if a native type), and clears the document’s edited status.

## Parameters

- `sender`: The control sending the message.

## See Also

- [func updateChangeCount(NSDocument.ChangeType)](nsdocument/updatechangecount(_:).md)
  Updates the receiver’s change count according to the given change type.
- [var fileType: String?](nsdocument/filetype.md)
  The name of the document type, as specified in the app’s information property-list file.
- [var fileURL: URL?](nsdocument/fileurl.md)
  The location of the document’s on-disk representation.
- [func printDocument(Any?)](nsdocument/printdocument(_:).md)
  Prints the receiver in response to the user choosing the Print menu command.
- [func runPageLayout(Any?)](nsdocument/runpagelayout(_:).md)
  The action method invoked in the receiver as first responder when the user chooses the Page Setup menu command.
- [func revertToSaved(Any?)](nsdocument/reverttosaved(_:).md)
  The action of the File menu item Revert in a document-based app.
- [func saveAs(Any?)](nsdocument/saveas(_:).md)
  The action method invoked in the receiver as first responder when the user chooses the Save As menu command.
- [func saveTo(Any?)](nsdocument/saveto(_:).md)
  The action method invoked in the receiver as first responder when the user chooses the Save To menu command.
- [func save(withDelegate: Any?, didSave: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsdocument/save(withdelegate:didsave:contextinfo:).md)
  Saves the document and delivers the results to the provided delegate object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/save(_:))*