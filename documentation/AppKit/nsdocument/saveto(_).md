# saveTo(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

The action method invoked in the receiver as first responder when the user chooses the Save To menu command.

**Availability**:
- macOS

## Declaration

```swift
@IBAction
func saveTo(_ sender: Any?)
```

```objc
- (void) saveDocumentTo:(id) sender;
```

#### Discussion

The default implementation is identical to [`saveAs(_:)`](./saveas%28_%29.md) except that this method doesn’t clear the document’s edited status and doesn’t reset file location and document type if the document is a native type.

## Parameters

- `sender`: The control sending the message.

## See Also

### Handling User Actions
- [func printDocument(Any?)](./printdocument%28_%29.md)
  Prints the receiver in response to the user choosing the Print menu command.
- [func runPageLayout(Any?)](./runpagelayout%28_%29.md)
  The action method invoked in the receiver as first responder when the user chooses the Page Setup menu command.
- [func revertToSaved(Any?)](./reverttosaved%28_%29.md)
  The action of the File menu item Revert in a document-based app.
- [func save(Any?)](./save%28_%29.md)
  The action method invoked in the receiver as first responder when the user chooses the Save menu command.
- [func saveAs(Any?)](./saveas%28_%29.md)
  The action method invoked in the receiver as first responder when the user chooses the Save As menu command.
- [func save(withDelegate: Any?, didSave: Selector?, contextInfo: UnsafeMutableRawPointer?)](./save%28withdelegate,didsave,contextinfo%29.md)
  Saves the document and delivers the results to the provided delegate object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/saveto(_:))*