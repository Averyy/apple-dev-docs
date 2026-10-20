# revertToSaved(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

The action of the File menu item Revert in a document-based app.

**Availability**:
- macOS

## Declaration

```swift
@IBAction
func revertToSaved(_ sender: Any?)
```

```objc
- (void) revertDocumentToSaved:(id) sender;
```

#### Discussion

The default implementation of this method presents an alert dialog giving the user the opportunity to cancel the operation. If the user chooses to continue, the method ensures that any editor registered using the Cocoa Bindings `NSEditorRegistration` informal protocol has discarded its changes and then invokes [`revert(toContentsOf:ofType:)`](./revert%28tocontentsof,oftype%29.md). If that returns [`false`](../../Swift/false.md), the method presents the error to the user in an document-modal alert dialog.

## Parameters

- `sender`: The control sending the message.

## See Also

### Related Documentation
- [func updateChangeCount(NSDocument.ChangeType)](./updatechangecount%28_%29.md)
  Updates the receiver’s change count according to the given change type.
### Handling User Actions
- [func printDocument(Any?)](./printdocument%28_%29.md)
  Prints the receiver in response to the user choosing the Print menu command.
- [func runPageLayout(Any?)](./runpagelayout%28_%29.md)
  The action method invoked in the receiver as first responder when the user chooses the Page Setup menu command.
- [func save(Any?)](./save%28_%29.md)
  The action method invoked in the receiver as first responder when the user chooses the Save menu command.
- [func saveAs(Any?)](./saveas%28_%29.md)
  The action method invoked in the receiver as first responder when the user chooses the Save As menu command.
- [func saveTo(Any?)](./saveto%28_%29.md)
  The action method invoked in the receiver as first responder when the user chooses the Save To menu command.
- [func save(withDelegate: Any?, didSave: Selector?, contextInfo: UnsafeMutableRawPointer?)](./save%28withdelegate,didsave,contextinfo%29.md)
  Saves the document and delivers the results to the provided delegate object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/reverttosaved(_:))*