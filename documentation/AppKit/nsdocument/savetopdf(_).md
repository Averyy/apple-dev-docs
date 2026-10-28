# saveToPDF(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Exports a PDF representation of the document’s current contents.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@IBAction
func saveToPDF(_ sender: Any?)
```

```objc
- (void) saveDocumentToPDF:(id) sender;
```

## Discussion

This action method handles the File menu’s “Export As PDF…” item in a document-based application.

The default implementation of this method calls the [`print(withSettings:showPrintPanel:delegate:didPrint:contextInfo:)`](./print%28withsettings,showprintpanel,delegate,didprint,contextinfo%29.md) method, passing a print settings object that contains only the disposition ([`save`](../nsprintinfo/jobdisposition-swift.struct/save.md)), with user interaction disabled and `NULL` or `nil` for all other parameters.

If your document subclass supports creating PDF representations, you can override this method, if needed.

> ❗ **Important**:  This method does not copy the document’s [`printInfo`](./printinfo.md) to the operation object when creating a PDF printing operation. Your app should maintain a separate [`NSPrintInfo`](../nsprintinfo.md) instance specifically for creating PDFs and pass it to the print operation’s [`printInfo`](../nsprintoperation/printinfo.md) method.

## Parameters

- `sender`: The control sending the message.

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
- [func print(withSettings: [NSPrintInfo.AttributeKey : Any], showPrintPanel: Bool, delegate: Any?, didPrint: Selector?, contextInfo: UnsafeMutableRawPointer?)](./print%28withsettings,showprintpanel,delegate,didprint,contextinfo%29.md)
  Prints the document’s contents, optionally displaying a print panel to the user.
- [func printOperation(withSettings: [NSPrintInfo.AttributeKey : Any]) throws -> NSPrintOperation](./printoperation%28withsettings%29.md)
  Creates and returns a print operation for the document’s contents.
- [var pdfPrintOperation: NSPrintOperation](./pdfprintoperation.md)
  A print operation you can use to create a PDF representation of the document’s current contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/savetopdf(_:))*