# print(withSettings:showPrintPanel:delegate:didPrint:contextInfo:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Prints the document’s contents, optionally displaying a print panel to the user.

**Availability**:
- macOS

## Declaration

```swift
func print(withSettings printSettings: [NSPrintInfo.AttributeKey : Any], showPrintPanel: Bool, delegate: Any?, didPrint didPrintSelector: Selector?, contextInfo: UnsafeMutableRawPointer?)
```

```objc
- (void) printDocumentWithSettings:(NSDictionary<NSString *,id> *) printSettings showPrintPanel:(BOOL) showPrintPanel delegate:(id) delegate didPrintSelector:(SEL) didPrintSelector contextInfo:(void *) contextInfo;
```

#### Discussion

If showing of the print panel is specified by `showPrintPanel`, the method presents it first and prints only if the user approves the panel. The `NSPrintInfo` attributes in the passed-in `printSettings` dictionary are added to a copy of the document’s print info, and the resulting print info settings are used for the operation. When printing is complete or canceled, the method sends the message selected by `didPrintSelector` to the `delegate`, with the `contextInfo` as the last argument. The method selected by `didPrintSelector` must have the same signature as:

```objc
- (void)document:(NSDocument *)document didPrint:(BOOL)didPrintSuccessfully  contextInfo: (void *)contextInfo
```

The default implementation of this method invokes [`printOperation(withSettings:)`](./printoperation%28withsettings%29.md). If `nil` is returned it presents the error to the user in a document-modal panel before messaging the delegate. Otherwise it invokes `[thePrintOperation setShowsPrintPanel:showPrintPanel]` then `[self runModalPrintOperation:thePrintOperation delegate:delegate didRunSelector:didPrintSelector contextInfo:contextInfo]`.

For backward binary compatibility with OS X v10.3 and earlier, the default implementation of this method invokes [`printShowingPrintPanel:`](./printshowingprintpanel_.md) if it is overridden. When doing this it uses private functionality to arrange for the print settings to take effect (despite the fact that the override of [`printShowingPrintPanel:`](./printshowingprintpanel_.md) can’t possibly know about them) and to get notified when the print operation has been completed, so it can message the delegate at the correct time. Correct messaging of the delegate is necessary for correct handling of the Print Apple event.

## Parameters

- `printSettings`: The print settings dictionary to use.
- `showPrintPanel`: A Boolean value indicating whether the print panel is shown.
- `delegate`: The delegate to which the selector message is sent.
- `didPrintSelector`: The selector of the message sent to the delegate.
- `contextInfo`: Object passed with the callback to provide any additional context information.

## See Also

### Printing the Document
- [var printInfo: NSPrintInfo](./printinfo.md)
  The printing information associated with the document.
- [func preparePageLayout(NSPageLayout) -> Bool](./preparepagelayout%28_%29.md)
  Adds document-specific content to the Page Layout panel.
- [func runModalPageLayout(with: NSPrintInfo, delegate: Any?, didRun: Selector?, contextInfo: UnsafeMutableRawPointer?)](./runmodalpagelayout%28with,delegate,didrun,contextinfo%29.md)
  Runs the modal page layout panel with the receiver’s printing information object.
- [func runModalPrintOperation(NSPrintOperation, delegate: Any?, didRun: Selector?, contextInfo: UnsafeMutableRawPointer?)](./runmodalprintoperation%28_,delegate,didrun,contextinfo%29.md)
  Runs the specified print operation modally.
- [func shouldChangePrintInfo(NSPrintInfo) -> Bool](./shouldchangeprintinfo%28_%29.md)
  Returns a Boolean value that indicates whether the document allows changes to the default printing information.
- [func printOperation(withSettings: [NSPrintInfo.AttributeKey : Any]) throws -> NSPrintOperation](./printoperation%28withsettings%29.md)
  Creates and returns a print operation for the document’s contents.
- [var pdfPrintOperation: NSPrintOperation](./pdfprintoperation.md)
  A print operation you can use to create a PDF representation of the document’s current contents.
- [func saveToPDF(Any?)](./savetopdf%28_%29.md)
  Exports a PDF representation of the document’s current contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/print(withsettings:showprintpanel:delegate:didprint:contextinfo:))*