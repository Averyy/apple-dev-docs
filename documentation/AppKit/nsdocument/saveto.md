# saveTo(_:)

**Framework**: AppKit  
**Kind**: method

The action method invoked in the receiver as first responder when the user chooses the Save To menu command.

**Availability**:
- macOS ?+

## Declaration

```swift
@IBAction
@MainActor func saveTo(_ sender: Any?)
```

#### Discussion

The default implementation is identical to [`saveAs(_:)`](nsdocument/saveas(_:).md) except that this method doesn’t clear the document’s edited status and doesn’t reset file location and document type if the document is a native type.

## Parameters

- `sender`: The control sending the message.

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
- [func save(withDelegate: Any?, didSave: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsdocument/save(withdelegate:didsave:contextinfo:).md)
  Saves the document and delivers the results to the provided delegate object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/saveto(_:))*