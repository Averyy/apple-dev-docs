# saveToPDF(_:)

**Framework**: AppKit  
**Kind**: method

Exports a PDF representation of the document’s current contents.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@IBAction
@MainActor func saveToPDF(_ sender: Any?)
```

#### Discussion

This action method handles the File menu’s “Export As PDF…” item in a document-based application.

The default implementation of this method calls the [`print(withSettings:showPrintPanel:delegate:didPrint:contextInfo:)`](nsdocument/print(withsettings:showprintpanel:delegate:didprint:contextinfo:).md) method, passing a print settings object that contains only the disposition ([`save`](nsprintinfo/jobdisposition-swift.struct/save.md)), with user interaction disabled and `NULL` or `nil` for all other parameters.

If your document subclass supports creating PDF representations, you can override this method, if needed.

> ❗ **Important**:  This method does not copy the document’s [`printInfo`](nsdocument/printinfo.md) to the operation object when creating a PDF printing operation. Your app should maintain a separate [`NSPrintInfo`](nsprintinfo.md) instance specifically for creating PDFs and pass it to the print operation’s [`printInfo`](nsprintoperation/printinfo.md) method.

 This method does not copy the document’s [`printInfo`](nsdocument/printinfo.md) to the operation object when creating a PDF printing operation. Your app should maintain a separate [`NSPrintInfo`](nsprintinfo.md) instance specifically for creating PDFs and pass it to the print operation’s [`printInfo`](nsprintoperation/printinfo.md) method.

## Parameters

- `sender`: The control sending the message.

## See Also

- [var printInfo: NSPrintInfo](nsdocument/printinfo.md)
  The printing information associated with the document.
- [func preparePageLayout(NSPageLayout) -> Bool](nsdocument/preparepagelayout(_:).md)
  Adds document-specific content to the Page Layout panel.
- [func runModalPageLayout(with: NSPrintInfo, delegate: Any?, didRun: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsdocument/runmodalpagelayout(with:delegate:didrun:contextinfo:).md)
  Runs the modal page layout panel with the receiver’s printing information object.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/savetopdf(_:))*