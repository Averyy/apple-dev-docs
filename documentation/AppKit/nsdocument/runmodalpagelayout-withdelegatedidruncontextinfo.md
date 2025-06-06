# runModalPageLayout(with:delegate:didRun:contextInfo:)

**Framework**: AppKit  
**Kind**: method

Runs the modal page layout panel with the receiver’s printing information object.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func runModalPageLayout(with printInfo: NSPrintInfo, delegate: Any?, didRun didRunSelector: Selector?, contextInfo: UnsafeMutableRawPointer?)
```

#### Discussion

Invoked from the action method [`runPageLayout(_:)`](nsdocument/runpagelayout(_:).md). Presents the page layout panel app modally if there is no document window to which it can be presented document modally.

When the panel is dismissed, `delegate` is sent a `didRunSelector` message. The `didRunSelector` callback method should have the following signature:

```objc
- (void)documentDidRunModalPageLayout:(NSDocument *)document accepted:(BOOL)accepted  contextInfo:(void *)contextInfo
```

## Parameters

- `printInfo`: The   object for the page layout panel to use.
- `delegate`: The delegate to which the selector message is sent.
- `didRunSelector`: The selector of the message sent to the delegate.
- `contextInfo`: Object passed with the callback to provide any additional context information.

## See Also

- [var printInfo: NSPrintInfo](nsdocument/printinfo.md)
  The printing information associated with the document.
- [func preparePageLayout(NSPageLayout) -> Bool](nsdocument/preparepagelayout(_:).md)
  Adds document-specific content to the Page Layout panel.
- [func runModalPrintOperation(NSPrintOperation, delegate: Any?, didRun: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsdocument/runmodalprintoperation(_:delegate:didrun:contextinfo:).md)
  Runs the specified print operation modally.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/runmodalpagelayout(with:delegate:didrun:contextinfo:))*