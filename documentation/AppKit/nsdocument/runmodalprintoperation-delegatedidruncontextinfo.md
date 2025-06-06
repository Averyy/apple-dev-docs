# runModalPrintOperation(_:delegate:didRun:contextInfo:)

**Framework**: AppKit  
**Kind**: method

Runs the specified print operation modally.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func runModalPrintOperation(_ printOperation: NSPrintOperation, delegate: Any?, didRun didRunSelector: Selector?, contextInfo: UnsafeMutableRawPointer?)
```

#### Discussion

Overrides of [`printShowingPrintPanel:`](nsdocument/printshowingprintpanel:.md) can invoke this method.

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

- [var printInfo: NSPrintInfo](nsdocument/printinfo.md)
  The printing information associated with the document.
- [func preparePageLayout(NSPageLayout) -> Bool](nsdocument/preparepagelayout(_:).md)
  Adds document-specific content to the Page Layout panel.
- [func runModalPageLayout(with: NSPrintInfo, delegate: Any?, didRun: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsdocument/runmodalpagelayout(with:delegate:didrun:contextinfo:).md)
  Runs the modal page layout panel with the receiver’s printing information object.
- [func shouldChangePrintInfo(NSPrintInfo) -> Bool](nsdocument/shouldchangeprintinfo(_:).md)
  Returns a Boolean value that indicates whether the document allows changes to the default printing information.
- [func print(withSettings: [NSPrintInfo.AttributeKey : Any], showPrintPanel: Bool, delegate: Any?, didPrint: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsdocument/print(withsettings:showprintpanel:delegate:didprint:contextinfo:).md)
  Prints the document’s contents, optionally displaying a print panel to the user.
- [func printOperation(withSettings: [NSPrintInfo.AttributeKey : Any]) throws -> NSPrintOperation](nsdocument/printoperation(withsettings:).md)
  Creates and returns a print operation for the document’s contents.
- [var pdfPrintOperation: NSPrintOperation](nsdocument/pdfprintoperation.md)
  A print operation you can use to create a PDF representation of the document’s current contents.
- [func saveToPDF(Any?)](nsdocument/savetopdf(_:).md)
  Exports a PDF representation of the document’s current contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/runmodalprintoperation(_:delegate:didrun:contextinfo:))*