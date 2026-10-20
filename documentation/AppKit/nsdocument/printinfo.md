# printInfo

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The printing information associated with the document.

**Availability**:
- macOS

## Declaration

```swift
@NSCopying
var printInfo: NSPrintInfo { get set }
```

```objc
@property (copy) NSPrintInfo * printInfo;
```

#### Return Value

The receiver’s `NSPrintInfo` object.

#### Discussion

The default value of this property is the default [`NSPrintInfo`](../nsprintinfo.md) object. To customize the printing information, assign a new value to this property. The Page Layout panel may also update the object in this property to reflect the options selected by the user.

## See Also

### Related Documentation
- [func runPageLayout(Any?)](./runpagelayout%28_%29.md)
  The action method invoked in the receiver as first responder when the user chooses the Page Setup menu command.
### Printing the Document
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
- [func saveToPDF(Any?)](./savetopdf%28_%29.md)
  Exports a PDF representation of the document’s current contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/printinfo)*