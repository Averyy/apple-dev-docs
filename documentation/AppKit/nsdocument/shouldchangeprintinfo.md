# shouldChangePrintInfo(_:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value that indicates whether the document allows changes to the default printing information.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func shouldChangePrintInfo(_ newPrintInfo: NSPrintInfo) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) by default; subclasses can override this method to return [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

This method is invoked by the [`runPageLayout(_:)`](nsdocument/runpagelayout(_:).md) method, which sets a new `NSPrintInfo`object for the document only if this method returns [`true`](https://developer.apple.com/documentation/Swift/true).

## Parameters

- `newPrintInfo`: The   object that is the result of the user approving the page layout panel presented by  .

## See Also

- [var printInfo: NSPrintInfo](nsdocument/printinfo.md)
  The printing information associated with the document.
- [func preparePageLayout(NSPageLayout) -> Bool](nsdocument/preparepagelayout(_:).md)
  Adds document-specific content to the Page Layout panel.
- [func runModalPageLayout(with: NSPrintInfo, delegate: Any?, didRun: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsdocument/runmodalpagelayout(with:delegate:didrun:contextinfo:).md)
  Runs the modal page layout panel with the receiver’s printing information object.
- [func runModalPrintOperation(NSPrintOperation, delegate: Any?, didRun: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsdocument/runmodalprintoperation(_:delegate:didrun:contextinfo:).md)
  Runs the specified print operation modally.
- [func print(withSettings: [NSPrintInfo.AttributeKey : Any], showPrintPanel: Bool, delegate: Any?, didPrint: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsdocument/print(withsettings:showprintpanel:delegate:didprint:contextinfo:).md)
  Prints the document’s contents, optionally displaying a print panel to the user.
- [func printOperation(withSettings: [NSPrintInfo.AttributeKey : Any]) throws -> NSPrintOperation](nsdocument/printoperation(withsettings:).md)
  Creates and returns a print operation for the document’s contents.
- [var pdfPrintOperation: NSPrintOperation](nsdocument/pdfprintoperation.md)
  A print operation you can use to create a PDF representation of the document’s current contents.
- [func saveToPDF(Any?)](nsdocument/savetopdf(_:).md)
  Exports a PDF representation of the document’s current contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/shouldchangeprintinfo(_:))*