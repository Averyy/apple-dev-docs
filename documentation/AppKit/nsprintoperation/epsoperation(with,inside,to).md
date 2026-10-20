# epsOperation(with:inside:to:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Creates and returns a new print operation object ready to control the copying of EPS graphics from the specified view.

**Availability**:
- macOS

## Declaration

```swift
class func epsOperation(with view: NSView, inside rect: NSRect, to data: NSMutableData?) -> NSPrintOperation
```

```objc
+ (NSPrintOperation *) EPSOperationWithView:(NSView *) view insideRect:(NSRect) rect toData:(NSMutableData *) data;
```

#### Return Value

The new `NSPrintOperation` object. You must run the operation to generate the EPS data.

#### Discussion

The new `NSPrintOperation` object uses the default `NSPrintInfo` object. This method raises an `NSPrintOperationExistsException` if there is already a print operation in progress; otherwise the returned object is made the current print operation for this thread.

## Parameters

- `view`: The view containing the data to be turned into EPS data.
- `rect`: The portion of the view (specified in points in the view’s coordinate space) to be rendered as EPS data.
- `data`: An empty `NSMutableData` object. After the job is run, this object contains the EPS data.

## See Also

### Related Documentation
- [class NSPrintOperation](../nsprintoperation.md)
  An object that controls operations that generate Encapsulated PostScript (EPS) code, Portable Document Format (PDF) code, or print jobs.
- [func run() -> Bool](./run%28%29.md)
  Runs the print operation on the current thread.
### Creating the Printing Operation Object
- [class func epsOperation(with: NSView, inside: NSRect, to: NSMutableData, printInfo: NSPrintInfo) -> NSPrintOperation](./epsoperation%28with,inside,to,printinfo%29.md)
  Creates and returns a new print operation object ready to control the copying of EPS graphics from the specified view using the specified print settings.
- [class func epsOperation(with: NSView, inside: NSRect, toPath: String, printInfo: NSPrintInfo) -> NSPrintOperation](./epsoperation%28with,inside,topath,printinfo%29.md)
  Creates and returns a new print operation object ready to control the copying of EPS graphics from the specified view and write the resulting data to the specified file.
- [class func pdfOperation(with: NSView, inside: NSRect, to: NSMutableData) -> NSPrintOperation](./pdfoperation%28with,inside,to%29.md)
  Creates and returns a new print operation object ready to control the copying of PDF graphics from the specified view.
- [class func pdfOperation(with: NSView, inside: NSRect, to: NSMutableData, printInfo: NSPrintInfo) -> NSPrintOperation](./pdfoperation%28with,inside,to,printinfo%29.md)
  Creates and returns a new print operation object ready to control the copying of PDF graphics from the specified view using the specified print settings.
- [class func pdfOperation(with: NSView, inside: NSRect, toPath: String, printInfo: NSPrintInfo) -> NSPrintOperation](./pdfoperation%28with,inside,topath,printinfo%29.md)
  Creates and returns a new print operation object ready to control the copying of PDF graphics from the specified view and write the resulting data to the specified file.
- [init(view: NSView)](./init%28view%29.md)
  Creates and returns an print operation object ready to control the printing of the specified view.
- [init(view: NSView, printInfo: NSPrintInfo)](./init%28view,printinfo%29.md)
  Creates and returns an print operation object ready to control the printing of the specified view using custom print settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation/epsoperation(with:inside:to:))*