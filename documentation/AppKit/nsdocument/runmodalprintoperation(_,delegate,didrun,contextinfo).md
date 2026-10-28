# runModalPrintOperation(_:delegate:didRun:contextInfo:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Runs the specified print operation modally.

**Availability**:
- macOS

## Declaration

```swift
func runModalPrintOperation(_ printOperation: NSPrintOperation, delegate: Any?, didRun didRunSelector: Selector?, contextInfo: UnsafeMutableRawPointer?)
```

```objc
- (void) runModalPrintOperation:(NSPrintOperation *) printOperation delegate:(id) delegate didRunSelector:(SEL) didRunSelector contextInfo:(void *) contextInfo;
```

## Discussion

Overrides of [`printShowingPrintPanel:`](./printshowingprintpanel_.md) can invoke this method.

When the panel is dismissed, `delegate` is sent a `didRunSelector` message. Pass the `contextInfo` object with the callback. The `didRunSelector` callback method should have the following signature:

```objc
- (void)documentDidRunModalPrintOperation:(NSDocument *)document  success:(BOOL)success  contextInfo:(void *)contextInfo
```

## Parameters

- `printOperation`: The print operation to run.
- `delegate`: The delegate to which the selector message is sent.
- `didRunSelector`: The selector of the message sent to the delegate.
- `contextInfo`: Object passed with the callback to provide any additional context information.

## See Also

### Printing the Document
- [var printInfo: NSPrintInfo](./printinfo.md)
  The printing information associated with the document.
- [func preparePageLayout(NSPageLayout) -> Bool](./preparepagelayout%28_%29.md)
  Adds document-specific content to the Page Layout panel.
- [func runModalPageLayout(with: NSPrintInfo, delegate: Any?, didRun: Selector?, contextInfo: UnsafeMutableRawPointer?)](./runmodalpagelayout%28with,delegate,didrun,contextinfo%29.md)
  Runs the modal page layout panel with the receiver’s printing information object.
- [func shouldChangePrintInfo(NSPrintInfo) -> Bool](./shouldchangeprintinfo%28_%29.md)
  Returns a Boolean value that indicates whether the document allows changes to the default printing information.
- [func print(withSettings: [NSPrintInfo.AttributeKey : Any], showPrintPanel: Bool, delegate: Any?, didPrint: Selector?, contextInfo: UnsafeMutableRawPointer?)](./print%28withsettings,showprintpanel,delegate,didprint,contextinfo%29.md)
  Prints the document’s contents, optionally displaying a print panel to the user.
- [func printOperation(withSettings: [NSPrintInfo.AttributeKey : Any]) throws -> NSPrintOperation](./printoperation%28withsettings%29.md)
  Creates and returns a print operation for the document’s contents.
- [var pdfPrintOperation: NSPrintOperation](./pdfprintoperation.md)
  A print operation you can use to create a PDF representation of the document’s current contents.
- [func saveToPDF(Any?)](./savetopdf%28_%29.md)
  Exports a PDF representation of the document’s current contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/runmodalprintoperation(_:delegate:didrun:contextinfo:))*