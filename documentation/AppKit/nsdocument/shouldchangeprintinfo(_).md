# shouldChangePrintInfo(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the document allows changes to the default printing information.

**Availability**:
- macOS

## Declaration

```swift
func shouldChangePrintInfo(_ newPrintInfo: NSPrintInfo) -> Bool
```

```objc
- (BOOL) shouldChangePrintInfo:(NSPrintInfo *) newPrintInfo;
```

#### Return Value

[`true`](../../Swift/true.md) by default; subclasses can override this method to return [`false`](../../Swift/false.md).

#### Discussion

This method is invoked by the [`runPageLayout(_:)`](./runpagelayout%28_%29.md) method, which sets a new `NSPrintInfo`object for the document only if this method returns [`true`](../../Swift/true.md).

## Parameters

- `newPrintInfo`: The `NSPrintInfo` object that is the result of the user approving the page layout panel presented by [`runPageLayout(_:)`](./runpagelayout%28_%29.md).

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
- [func print(withSettings: [NSPrintInfo.AttributeKey : Any], showPrintPanel: Bool, delegate: Any?, didPrint: Selector?, contextInfo: UnsafeMutableRawPointer?)](./print%28withsettings,showprintpanel,delegate,didprint,contextinfo%29.md)
  Prints the document’s contents, optionally displaying a print panel to the user.
- [func printOperation(withSettings: [NSPrintInfo.AttributeKey : Any]) throws -> NSPrintOperation](./printoperation%28withsettings%29.md)
  Creates and returns a print operation for the document’s contents.
- [var pdfPrintOperation: NSPrintOperation](./pdfprintoperation.md)
  A print operation you can use to create a PDF representation of the document’s current contents.
- [func saveToPDF(Any?)](./savetopdf%28_%29.md)
  Exports a PDF representation of the document’s current contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/shouldchangeprintinfo(_:))*