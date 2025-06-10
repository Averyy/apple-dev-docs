# pdfPrintOperation

**Framework**: AppKit  
**Kind**: property

A print operation you can use to create a PDF representation of the document’s current contents.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
var pdfPrintOperation: NSPrintOperation { get }
```

#### Discussion

The object in this property can be run to print the document’s current contents to a PDF file.

The default print operation stored by this property is obtained by calling the [`printOperation(withSettings:)`](nsdocument/printoperation(withsettings:).md) method and  passing a print settings object that contains only the disposition ([`save`](nsprintinfo/jobdisposition-swift.struct/save.md)) and a `NULL` error object reference. If your document subclass supports creating PDF representations, you can override this property as needed to customize the options.

> ❗ **Important**:  This property does not copy the document’s [`printInfo`](nsdocument/printinfo.md) to the PDF printing operation object. Your app should maintain a separate [`NSPrintInfo`](nsprintinfo.md) instance specifically for creating PDFs and assign it to the [`printInfo`](nsprintoperation/printinfo.md) property of the operation object.

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
- [func saveToPDF(Any?)](nsdocument/savetopdf(_:).md)
  Exports a PDF representation of the document’s current contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/pdfprintoperation)*