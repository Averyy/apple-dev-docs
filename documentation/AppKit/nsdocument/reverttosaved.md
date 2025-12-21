# revertToSaved(_:)

**Framework**: AppKit  
**Kind**: method

The action of the File menu item Revert in a document-based app.

**Availability**:
- macOS ?+

## Declaration

```swift
@IBAction
@MainActor func revertToSaved(_ sender: Any?)
```

#### Discussion

The default implementation of this method presents an alert dialog giving the user the opportunity to cancel the operation. If the user chooses to continue, the method ensures that any editor registered using the Cocoa Bindings `NSEditorRegistration` informal protocol has discarded its changes and then invokes [`revert(toContentsOf:ofType:)`](nsdocument/revert(tocontentsof:oftype:).md). If that returns [`false`](https://developer.apple.com/documentation/Swift/false), the method presents the error to the user in an document-modal alert dialog.

## Parameters

- `sender`: The control sending the message.

## See Also

- [func updateChangeCount(NSDocument.ChangeType)](nsdocument/updatechangecount(_:).md)
  Updates the receiver’s change count according to the given change type.
- [func printDocument(Any?)](nsdocument/printdocument(_:).md)
  Prints the receiver in response to the user choosing the Print menu command.
- [func runPageLayout(Any?)](nsdocument/runpagelayout(_:).md)
  The action method invoked in the receiver as first responder when the user chooses the Page Setup menu command.
- [func save(Any?)](nsdocument/save(_:).md)
  The action method invoked in the receiver as first responder when the user chooses the Save menu command.
- [func saveAs(Any?)](nsdocument/saveas(_:).md)
  The action method invoked in the receiver as first responder when the user chooses the Save As menu command.
- [func saveTo(Any?)](nsdocument/saveto(_:).md)
  The action method invoked in the receiver as first responder when the user chooses the Save To menu command.
- [func save(withDelegate: Any?, didSave: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsdocument/save(withdelegate:didsave:contextinfo:).md)
  Saves the document and delivers the results to the provided delegate object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/reverttosaved(_:))*