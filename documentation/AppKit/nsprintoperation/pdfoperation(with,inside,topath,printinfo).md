# pdfOperation(with:inside:toPath:printInfo:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Creates and returns a new print operation object ready to control the copying of PDF graphics from the specified view and write the resulting data to the specified file.

**Availability**:
- macOS

## Declaration

```swift
class func pdfOperation(with view: NSView, inside rect: NSRect, toPath path: String, printInfo: NSPrintInfo) -> NSPrintOperation
```

```objc
+ (NSPrintOperation *) PDFOperationWithView:(NSView *) view insideRect:(NSRect) rect toPath:(NSString *) path printInfo:(NSPrintInfo *) printInfo;
```

#### Return Value

The new `NSPrintOperation` object. You must run the operation to generate the PDF data.

#### Discussion

This method raises an `NSPrintOperationExistsException` if there is already a print operation in progress; otherwise the returned object is made the current print operation for this thread.

## Parameters

- `view`: The view containing the data to be turned into PDF data.
- `rect`: The portion of the view (specified in points in the view’s coordinate space) to be rendered as PDF data.
- `path`: The path to a file. After the job is run, this file contains the PDF data.
- `printInfo`: The print settings to use when generating the PDF data.

## See Also

### Related Documentation
- [func run() -> Bool](./run%28%29.md)
  Runs the print operation on the current thread.
### Creating the Printing Operation Object
- [class func epsOperation(with: NSView, inside: NSRect, to: NSMutableData?) -> NSPrintOperation](./epsoperation%28with,inside,to%29.md)
  Creates and returns a new print operation object ready to control the copying of EPS graphics from the specified view.
- [class func epsOperation(with: NSView, inside: NSRect, to: NSMutableData, printInfo: NSPrintInfo) -> NSPrintOperation](./epsoperation%28with,inside,to,printinfo%29.md)
  Creates and returns a new print operation object ready to control the copying of EPS graphics from the specified view using the specified print settings.
- [class func epsOperation(with: NSView, inside: NSRect, toPath: String, printInfo: NSPrintInfo) -> NSPrintOperation](./epsoperation%28with,inside,topath,printinfo%29.md)
  Creates and returns a new print operation object ready to control the copying of EPS graphics from the specified view and write the resulting data to the specified file.
- [class func pdfOperation(with: NSView, inside: NSRect, to: NSMutableData) -> NSPrintOperation](./pdfoperation%28with,inside,to%29.md)
  Creates and returns a new print operation object ready to control the copying of PDF graphics from the specified view.
- [class func pdfOperation(with: NSView, inside: NSRect, to: NSMutableData, printInfo: NSPrintInfo) -> NSPrintOperation](./pdfoperation%28with,inside,to,printinfo%29.md)
  Creates and returns a new print operation object ready to control the copying of PDF graphics from the specified view using the specified print settings.
- [init(view: NSView)](./init%28view%29.md)
  Creates and returns an print operation object ready to control the printing of the specified view.
- [init(view: NSView, printInfo: NSPrintInfo)](./init%28view,printinfo%29.md)
  Creates and returns an print operation object ready to control the printing of the specified view using custom print settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation/pdfoperation(with:inside:topath:printinfo:))*