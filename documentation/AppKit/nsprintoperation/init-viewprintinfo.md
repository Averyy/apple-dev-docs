# init(view:printInfo:)

**Framework**: AppKit  
**Kind**: init

Creates and returns an print operation object ready to control the printing of the specified view using custom print settings.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
init(view: NSView, printInfo: NSPrintInfo)
```

#### Return Value

The new `NSPrintOperation` object. You must run the operation to print the view.

#### Discussion

This method raises an `NSPrintOperationExistsException` if there is already a print operation in progress; otherwise the returned object is made the current print operation for this thread.

## Parameters

- `view`: The view whose contents you want to print.
- `printInfo`: The print settings to use when printing the view.

## See Also

- [func run() -> Bool](nsprintoperation/run.md)
  Runs the print operation on the current thread.
- [class func epsOperation(with: NSView, inside: NSRect, to: NSMutableData?) -> NSPrintOperation](nsprintoperation/epsoperation(with:inside:to:).md)
  Creates and returns a new print operation object ready to control the copying of EPS graphics from the specified view.
- [class func epsOperation(with: NSView, inside: NSRect, to: NSMutableData, printInfo: NSPrintInfo) -> NSPrintOperation](nsprintoperation/epsoperation(with:inside:to:printinfo:).md)
  Creates and returns a new print operation object ready to control the copying of EPS graphics from the specified view using the specified print settings.
- [class func epsOperation(with: NSView, inside: NSRect, toPath: String, printInfo: NSPrintInfo) -> NSPrintOperation](nsprintoperation/epsoperation(with:inside:topath:printinfo:).md)
  Creates and returns a new print operation object ready to control the copying of EPS graphics from the specified view and write the resulting data to the specified file.
- [class func pdfOperation(with: NSView, inside: NSRect, to: NSMutableData) -> NSPrintOperation](nsprintoperation/pdfoperation(with:inside:to:).md)
  Creates and returns a new print operation object ready to control the copying of PDF graphics from the specified view.
- [class func pdfOperation(with: NSView, inside: NSRect, to: NSMutableData, printInfo: NSPrintInfo) -> NSPrintOperation](nsprintoperation/pdfoperation(with:inside:to:printinfo:).md)
  Creates and returns a new print operation object ready to control the copying of PDF graphics from the specified view using the specified print settings.
- [class func pdfOperation(with: NSView, inside: NSRect, toPath: String, printInfo: NSPrintInfo) -> NSPrintOperation](nsprintoperation/pdfoperation(with:inside:topath:printinfo:).md)
  Creates and returns a new print operation object ready to control the copying of PDF graphics from the specified view and write the resulting data to the specified file.
- [init(view: NSView)](nsprintoperation/init(view:).md)
  Creates and returns an print operation object ready to control the printing of the specified view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation/init(view:printinfo:))*