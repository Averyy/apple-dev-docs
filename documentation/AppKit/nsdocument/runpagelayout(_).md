# runPageLayout(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

The action method invoked in the receiver as first responder when the user chooses the Page Setup menu command.

**Availability**:
- macOS

## Declaration

```swift
@IBAction
func runPageLayout(_ sender: Any?)
```

```objc
- (void) runPageLayout:(id) sender;
```

## Discussion

The default implementation invokes [`runModalPageLayout(with:delegate:didRun:contextInfo:)`](./runmodalpagelayout%28with,delegate,didrun,contextinfo%29.md) with the document’s current NSPrintInfo object as argument; if the user clicks the OK button and the document authorizes changes to its printing information ([`shouldChangePrintInfo(_:)`](./shouldchangeprintinfo%28_%29.md)), the method sets the document’s new `NSPrintInfo` object and increments the document’s change count.

## Parameters

- `sender`: The control sending the message.

## See Also

### Related Documentation
- [func updateChangeCount(NSDocument.ChangeType)](./updatechangecount%28_%29.md)
  Updates the receiver’s change count according to the given change type.
- [var printInfo: NSPrintInfo](./printinfo.md)
  The printing information associated with the document.
### Handling User Actions
- [func printDocument(Any?)](./printdocument%28_%29.md)
  Prints the receiver in response to the user choosing the Print menu command.
- [func revertToSaved(Any?)](./reverttosaved%28_%29.md)
  The action of the File menu item Revert in a document-based app.
- [func save(Any?)](./save%28_%29.md)
  The action method invoked in the receiver as first responder when the user chooses the Save menu command.
- [func saveAs(Any?)](./saveas%28_%29.md)
  The action method invoked in the receiver as first responder when the user chooses the Save As menu command.
- [func saveTo(Any?)](./saveto%28_%29.md)
  The action method invoked in the receiver as first responder when the user chooses the Save To menu command.
- [func save(withDelegate: Any?, didSave: Selector?, contextInfo: UnsafeMutableRawPointer?)](./save%28withdelegate,didsave,contextinfo%29.md)
  Saves the document and delivers the results to the provided delegate object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/runpagelayout(_:))*