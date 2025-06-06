# runPageLayout(_:)

**Framework**: AppKit  
**Kind**: method

The action method invoked in the receiver as first responder when the user chooses the Page Setup menu command.

**Availability**:
- macOS ?+

## Declaration

```swift
@IBAction
@MainActor func runPageLayout(_ sender: Any?)
```

#### Discussion

The default implementation invokes [`runModalPageLayout(with:delegate:didRun:contextInfo:)`](nsdocument/runmodalpagelayout(with:delegate:didrun:contextinfo:).md) with the document’s current NSPrintInfo object as argument; if the user clicks the OK button and the document authorizes changes to its printing information ([`shouldChangePrintInfo(_:)`](nsdocument/shouldchangeprintinfo(_:).md)), the method sets the document’s new `NSPrintInfo` object and increments the document’s change count.

## Parameters

- `sender`: The control sending the message.

## See Also

- [func updateChangeCount(NSDocument.ChangeType)](nsdocument/updatechangecount(_:).md)
  Updates the receiver’s change count according to the given change type.
- [var printInfo: NSPrintInfo](nsdocument/printinfo.md)
  The printing information associated with the document.
- [func printDocument(Any?)](nsdocument/printdocument(_:).md)
  Prints the receiver in response to the user choosing the Print menu command.
- [func revertToSaved(Any?)](nsdocument/reverttosaved(_:).md)
  The action of the File menu item Revert in a document-based app.
- [func save(Any?)](nsdocument/save(_:).md)
  The action method invoked in the receiver as first responder when the user chooses the Save menu command.
- [func saveAs(Any?)](nsdocument/saveas(_:).md)
  The action method invoked in the receiver as first responder when the user chooses the Save As menu command.
- [func saveTo(Any?)](nsdocument/saveto(_:).md)
  The action method invoked in the receiver as first responder when the user chooses the Save To menu command.
- [func save(withDelegate: Any?, didSave: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsdocument/save(withdelegate:didsave:contextinfo:).md)
  Saves the document and delivers the results to the provided delegate object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/runpagelayout(_:))*