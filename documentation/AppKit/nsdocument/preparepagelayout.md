# preparePageLayout(_:)

**Framework**: AppKit  
**Kind**: method

Adds document-specific content to the Page Layout panel.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func preparePageLayout(_ pageLayout: NSPageLayout) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if successfully prepared; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

The [`runModalPageLayoutWithPrintInfo:`](nsdocument/runmodalpagelayoutwithprintinfo:.md) and [`runModalPageLayout(with:delegate:didRun:contextInfo:)`](nsdocument/runmodalpagelayout(with:delegate:didrun:contextinfo:).md) methods call this method to allow the document to customize the Page Layout panel `pageLayout`. You might use this method to add a document-related accessory view.

The default implementation returns [`true`](https://developer.apple.com/documentation/Swift/true).

## Parameters

- `pageLayout`: The page layout panel to prepare.

## See Also

- [var printInfo: NSPrintInfo](nsdocument/printinfo.md)
  The printing information associated with the document.
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
- [func saveToPDF(Any?)](nsdocument/savetopdf(_:).md)
  Exports a PDF representation of the document’s current contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/preparepagelayout(_:))*