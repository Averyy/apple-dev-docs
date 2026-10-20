# preparePageLayout(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds document-specific content to the Page Layout panel.

**Availability**:
- macOS

## Declaration

```swift
func preparePageLayout(_ pageLayout: NSPageLayout) -> Bool
```

```objc
- (BOOL) preparePageLayout:(NSPageLayout *) pageLayout;
```

#### Return Value

[`true`](../../Swift/true.md) if successfully prepared; otherwise, [`false`](../../Swift/false.md).

#### Discussion

The [`runModalPageLayoutWithPrintInfo:`](./runmodalpagelayoutwithprintinfo_.md) and [`runModalPageLayout(with:delegate:didRun:contextInfo:)`](./runmodalpagelayout%28with,delegate,didrun,contextinfo%29.md) methods call this method to allow the document to customize the Page Layout panel `pageLayout`. You might use this method to add a document-related accessory view.

The default implementation returns [`true`](../../Swift/true.md).

## Parameters

- `pageLayout`: The page layout panel to prepare.

## See Also

### Printing the Document
- [var printInfo: NSPrintInfo](./printinfo.md)
  The printing information associated with the document.
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
- [func saveToPDF(Any?)](./savetopdf%28_%29.md)
  Exports a PDF representation of the document’s current contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/preparepagelayout(_:))*