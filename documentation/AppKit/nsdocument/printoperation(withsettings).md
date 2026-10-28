# printOperation(withSettings:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Creates and returns a print operation for the document’s contents.

**Availability**:
- macOS

## Declaration

```swift
func printOperation(withSettings printSettings: [NSPrintInfo.AttributeKey : Any]) throws -> NSPrintOperation
```

```objc
- (NSPrintOperation *) printOperationWithSettings:(NSDictionary<NSString *,id> *) printSettings error:(NSError **) outError;
```

## Return Value

The print operation, or `nil` if unsuccessful.

## Discussion

The print operation can be run to print the document’s current contents. The `NSPrintInfo` attributes in the passed-in `printSettings` dictionary are added to a copy of the document’s print info, and the resulting print info is used for the operation.

> ❗ **Important**:  You must override this method to enable printing in your app. The default implementation raises an exception.

> **Handling Errors in Swift**:  In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> When overriding this method, use the `throw` statement to throw an `NSError`, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `printSettings`: The print settings dictionary to use.

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
- [var pdfPrintOperation: NSPrintOperation](./pdfprintoperation.md)
  A print operation you can use to create a PDF representation of the document’s current contents.
- [func saveToPDF(Any?)](./savetopdf%28_%29.md)
  Exports a PDF representation of the document’s current contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/printoperation(withsettings:))*