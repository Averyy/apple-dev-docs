# NSPrintOperation

**Framework**: AppKit  
**Kind**: class

An object that controls operations that generate Encapsulated PostScript (EPS) code, Portable Document Format (PDF) code, or print jobs.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSPrintOperation
```

#### Overview

An [`NSPrintOperation`](nsprintoperation.md) object works in conjunction with two other objects: an [`NSPrintInfo`](nsprintinfo.md) object, which specifies how the code should be generated, and an [`NSView`](nsview.md) object, which generates the actual code.

It is important to note that the majority of methods in [`NSPrintOperation`](nsprintoperation.md) copy the instance of [`NSPrintInfo`](nsprintinfo.md) passed into them. Future changes to that print info are not reflected in the print info retained by the current [`NSPrintOperation`](nsprintoperation.md) object. All changes should be made to the print info before passing to the methods of this class. The only method in [`NSPrintOperation`](nsprintoperation.md) which does not copy the [`NSPrintInfo`](nsprintinfo.md) instance is [`printInfo`](nsprintoperation/printinfo.md).

> **Note**:  You should not subclass [`NSPrintOperation`](nsprintoperation.md). Methods that return a print operation object return an instance of a concrete subclass whose implementation is private.

 You should not subclass [`NSPrintOperation`](nsprintoperation.md). Methods that return a print operation object return an instance of a concrete subclass whose implementation is private.

## Topics

### Creating the Printing Operation Object
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
- [init(view: NSView, printInfo: NSPrintInfo)](nsprintoperation/init(view:printinfo:).md)
  Creates and returns an print operation object ready to control the printing of the specified view using custom print settings.
### Setting the Current Print Operation for This Thread
- [class var current: NSPrintOperation?](nsprintoperation/current.md)
  The current print operation for this thread.
### Determining the Type of Operation
- [var isCopyingOperation: Bool](nsprintoperation/iscopyingoperation.md)
  A Boolean value that indicates whether the print operation is an EPS or PDF copy operation.
### Modifying the Printing Information
- [var printInfo: NSPrintInfo](nsprintoperation/printinfo.md)
  The printing information associated with the print operation.
- [class NSPrintInfo](nsprintinfo.md)
  An object that stores information that’s used to generate printed output.
### Getting the View
- [var view: NSView?](nsprintoperation/view.md)
  The view object that generates the actual data for the print operation.
### Getting the Printing Quality
- [var preferredRenderingQuality: NSPrintOperation.RenderingQuality](nsprintoperation/preferredrenderingquality.md)
  The printing quality.
- [NSPrintOperation.RenderingQuality](nsprintoperation/renderingquality.md)
  Constants that specify the print quality in use.
### Running the Print Operation
- [func run() -> Bool](nsprintoperation/run.md)
  Runs the print operation on the current thread.
- [func runModal(for: NSWindow, delegate: Any?, didRun: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsprintoperation/runmodal(for:delegate:didrun:contextinfo:).md)
  Runs the print operation, calling your custom delegate method upon completion.
- [func cleanUp()](nsprintoperation/cleanup.md)
  Called at the end of a print operation to remove the print operation as the current operation.
- [func deliverResult() -> Bool](nsprintoperation/deliverresult.md)
  Delivers the results of the print operation to the intended destination.
### Modifying the User Interface
- [var showsPrintPanel: Bool](nsprintoperation/showsprintpanel.md)
  A Boolean value that determines whether the print operation displays a print panel.
- [var showsProgressPanel: Bool](nsprintoperation/showsprogresspanel.md)
  A Boolean value that determines whether the print operation displays a progress panel.
- [var jobTitle: String?](nsprintoperation/jobtitle.md)
  The custom title of the print job.
- [var printPanel: NSPrintPanel](nsprintoperation/printpanel.md)
  The print panel object to use during the operation.
- [var pdfPanel: NSPDFPanel](nsprintoperation/pdfpanel.md)
  The PDF panel object to use during the operation.
### Managing the Drawing Context
- [var context: NSGraphicsContext?](nsprintoperation/context.md)
  The graphics context object used for generating output.
- [func createContext() -> NSGraphicsContext?](nsprintoperation/createcontext.md)
  Creates the graphics context object used for drawing during the operation.
- [func destroyContext()](nsprintoperation/destroycontext.md)
  Destroys the print operation’s graphics context.
### Managing Page Information
- [var currentPage: Int](nsprintoperation/currentpage.md)
  The current page number being printed.
- [var pageRange: NSRange](nsprintoperation/pagerange.md)
  The range of pages associated with the print operation.
- [var pageOrder: NSPrintOperation.PageOrder](nsprintoperation/pageorder-swift.property.md)
  The print order for the pages of the operation.
- [NSPrintOperation.PageOrder](nsprintoperation/pageorder-swift.enum.md)
  Constants that specify the page order.
### Managing Printing Threads
- [var canSpawnSeparateThread: Bool](nsprintoperation/canspawnseparatethread.md)
  A Boolean value that determines whether the print operation is allowed to spawn a separate printing thread.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class NSPrinter](nsprinter.md)
  An object that describes a printer’s capabilities.
- [class NSPrintInfo](nsprintinfo.md)
  An object that stores information that’s used to generate printed output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation)*