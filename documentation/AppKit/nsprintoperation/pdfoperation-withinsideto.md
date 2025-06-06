# pdfOperation(with:inside:to:)

**Framework**: AppKit  
**Kind**: method

Creates and returns a new print operation object ready to control the copying of PDF graphics from the specified view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class func pdfOperation(with view: NSView, inside rect: NSRect, to data: NSMutableData) -> NSPrintOperation
```

#### Return Value

The new `NSPrintOperation` object. You must run the operation to generate the PDF data.

#### Discussion

The new `NSPrintOperation` object uses the default `NSPrintInfo` object. This method raises an `NSPrintOperationExistsException` if there is already a print operation in progress; otherwise the returned object is made the current print operation for this thread.

## Parameters

- `view`: The view containing the data to be turned into PDF data.
- `rect`: The portion of the view (specified in points in the view’s coordinate space) to be rendered as PDF data.
- `data`: An empty   object. After the job is run, this object contains the PDF data.

## See Also

- [func run() -> Bool](nsprintoperation/run.md)
  Runs the print operation on the current thread.
- [class func epsOperation(with: NSView, inside: NSRect, to: NSMutableData?) -> NSPrintOperation](nsprintoperation/epsoperation(with:inside:to:).md)
  Creates and returns a new print operation object ready to control the copying of EPS graphics from the specified view.
- [class func epsOperation(with: NSView, inside: NSRect, to: NSMutableData, printInfo: NSPrintInfo) -> NSPrintOperation](nsprintoperation/epsoperation(with:inside:to:printinfo:).md)
  Creates and returns a new print operation object ready to control the copying of EPS graphics from the specified view using the specified print settings.
- [class func epsOperation(with: NSView, inside: NSRect, toPath: String, printInfo: NSPrintInfo) -> NSPrintOperation](nsprintoperation/epsoperation(with:inside:topath:printinfo:).md)
  Creates and returns a new print operation object ready to control the copying of EPS graphics from the specified view and write the resulting data to the specified file.
- [class func pdfOperation(with: NSView, inside: NSRect, to: NSMutableData, printInfo: NSPrintInfo) -> NSPrintOperation](nsprintoperation/pdfoperation(with:inside:to:printinfo:).md)
  Creates and returns a new print operation object ready to control the copying of PDF graphics from the specified view using the specified print settings.
- [class func pdfOperation(with: NSView, inside: NSRect, toPath: String, printInfo: NSPrintInfo) -> NSPrintOperation](nsprintoperation/pdfoperation(with:inside:topath:printinfo:).md)
  Creates and returns a new print operation object ready to control the copying of PDF graphics from the specified view and write the resulting data to the specified file.
- [init(view: NSView)](nsprintoperation/init(view:).md)
  Creates and returns an print operation object ready to control the printing of the specified view.
- [init(view: NSView, printInfo: NSPrintInfo)](nsprintoperation/init(view:printinfo:).md)
  Creates and returns an print operation object ready to control the printing of the specified view using custom print settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation/pdfoperation(with:inside:to:))*