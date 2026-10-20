# printDocument(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Prints the receiver in response to the user choosing the Print menu command.

**Availability**:
- macOS

## Declaration

```swift
@IBAction
func printDocument(_ sender: Any?)
```

```objc
- (void) printDocument:(id) sender;
```

#### Discussion

An `NSDocument` object receives this action message as it travels up the responder chain. The default implementation invokes [`print(withSettings:showPrintPanel:delegate:didPrint:contextInfo:)`](./print%28withsettings,showprintpanel,delegate,didprint,contextinfo%29.md).

## Parameters

- `sender`: The control sending the message.

## See Also

### Related Documentation
- [var printInfo: NSPrintInfo](./printinfo.md)
  The printing information associated with the document.
- [func shouldChangePrintInfo(NSPrintInfo) -> Bool](./shouldchangeprintinfo%28_%29.md)
  Returns a Boolean value that indicates whether the document allows changes to the default printing information.
### Handling User Actions
- [func runPageLayout(Any?)](./runpagelayout%28_%29.md)
  The action method invoked in the receiver as first responder when the user chooses the Page Setup menu command.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/printdocument(_:))*