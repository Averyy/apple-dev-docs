# printDocument(_:)

**Framework**: AppKit  
**Kind**: method

Prints the receiver in response to the user choosing the Print menu command.

**Availability**:
- macOS ?+

## Declaration

```swift
@IBAction
@MainActor func printDocument(_ sender: Any?)
```

#### Discussion

An `NSDocument` object receives this action message as it travels up the responder chain. The default implementation invokes [`print(withSettings:showPrintPanel:delegate:didPrint:contextInfo:)`](nsdocument/print(withsettings:showprintpanel:delegate:didprint:contextinfo:).md).

## Parameters

- `sender`: The control sending the message.

## See Also

- [var printInfo: NSPrintInfo](nsdocument/printinfo.md)
  The printing information associated with the document.
- [func shouldChangePrintInfo(NSPrintInfo) -> Bool](nsdocument/shouldchangeprintinfo(_:).md)
  Returns a Boolean value that indicates whether the document allows changes to the default printing information.
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
- [func save(withDelegate: Any?, didSave: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsdocument/save(withdelegate:didsave:contextinfo:).md)
  Saves the document and delivers the results to the provided delegate object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/printdocument(_:))*