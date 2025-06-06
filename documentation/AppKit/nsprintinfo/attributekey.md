# NSPrintInfo.AttributeKey

**Framework**: AppKit  
**Kind**: struct

Constants that specify print job attributes.

**Availability**:
- macOS ?+

## Declaration

```swift
struct AttributeKey
```

## Topics

### Page Setup Attributes
- [static let paperName: NSPrintInfo.AttributeKey](nsprintinfo/attributekey/papername.md)
  An `NSString` object containing the paper name.
- [static let paperSize: NSPrintInfo.AttributeKey](nsprintinfo/attributekey/papersize.md)
  An `NSSize` value specifying the height and width of paper in points.
- [static let orientation: NSPrintInfo.AttributeKey](nsprintinfo/attributekey/orientation.md)
  An `NSNumber` object containing an `NSPrintingOrientation`.
- [static let scalingFactor: NSPrintInfo.AttributeKey](nsprintinfo/attributekey/scalingfactor.md)
  Scale factor percentage before pagination.
### Pagination Attributes
- [static let leftMargin: NSPrintInfo.AttributeKey](nsprintinfo/attributekey/leftmargin.md)
  `NSNumber`, containing a floating-point value that specifies the left margin, in points.
- [static let rightMargin: NSPrintInfo.AttributeKey](nsprintinfo/attributekey/rightmargin.md)
  `NSNumber`, containing a floating-point value that specifies the right margin, in points.
- [static let topMargin: NSPrintInfo.AttributeKey](nsprintinfo/attributekey/topmargin.md)
  `NSNumber`, containing a floating-point value that specifies the top margin, in points.
- [static let bottomMargin: NSPrintInfo.AttributeKey](nsprintinfo/attributekey/bottommargin.md)
  `NSNumber`, containing a floating-point value that specifies the bottom margin, in points.
- [static let horizontallyCentered: NSPrintInfo.AttributeKey](nsprintinfo/attributekey/horizontallycentered.md)
  `NSNumber`, containing a Boolean value that is [`true`](https://developer.apple.com/documentation/swift/true) if pages are centered horizontally.
- [static let verticallyCentered: NSPrintInfo.AttributeKey](nsprintinfo/attributekey/verticallycentered.md)
  `NSNumber`, containing a Boolean value that is [`true`](https://developer.apple.com/documentation/swift/true) if pages are centered vertically.
- [static let horizontalPagination: NSPrintInfo.AttributeKey](nsprintinfo/attributekey/horizontalpagination.md)
  `NSNumber`, containing a `NSPrintingPaginationMode` value.
- [static let verticalPagination: NSPrintInfo.AttributeKey](nsprintinfo/attributekey/verticalpagination.md)
  `NSNumber`, containing a `NSPrintingPaginationMode` value.
### Other Attributes
- [static let allPages: NSPrintInfo.AttributeKey](nsprintinfo/attributekey/allpages.md)
  An `NSNumber` object containing a Boolean value—if [`true`](https://developer.apple.com/documentation/swift/true), includes all pages in output.
- [static let copies: NSPrintInfo.AttributeKey](nsprintinfo/attributekey/copies.md)
  An `NSNumber` object containing an integer—the number of copies to spool.
- [static let detailedErrorReporting: NSPrintInfo.AttributeKey](nsprintinfo/attributekey/detailederrorreporting.md)
  An `NSNumber` object containing a Boolean value—if [`true`](https://developer.apple.com/documentation/swift/true), produce detailed reports when an error occurs.
- [static let faxNumber: NSPrintInfo.AttributeKey](nsprintinfo/attributekey/faxnumber.md)
  An `NSString` object that specifies a fax number.
- [static let firstPage: NSPrintInfo.AttributeKey](nsprintinfo/attributekey/firstpage.md)
  An `NSNumber` object containing an integer value that specifies the first page in the print job.
- [static let headerAndFooter: NSPrintInfo.AttributeKey](nsprintinfo/attributekey/headerandfooter.md)
  An `NSNumber` object containing a Boolean value—if [`true`](https://developer.apple.com/documentation/swift/true), a standard header and footer are added outside the margins of each page.
- [static let jobDisposition: NSPrintInfo.AttributeKey](nsprintinfo/attributekey/jobdisposition.md)
  An `NSString` object that specifies the job disposition.
- [static let jobSavingFileNameExtensionHidden: NSPrintInfo.AttributeKey](nsprintinfo/attributekey/jobsavingfilenameextensionhidden.md)
  A Boolean [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) indicating whether the job’s file name extension should be hidden when the [`jobDisposition`](nsprintinfo/jobdisposition-swift.property.md) is [`save`](nsprintinfo/jobdisposition-swift.struct/save.md). The default is [`false`](https://developer.apple.com/documentation/swift/false).
- [static let jobSavingURL: NSPrintInfo.AttributeKey](nsprintinfo/attributekey/jobsavingurl.md)
  An `NSURL` containing the location to which the job file will be saved when the [`jobDisposition`](nsprintinfo/jobdisposition-swift.property.md) is [`save`](nsprintinfo/jobdisposition-swift.struct/save.md).
- [static let lastPage: NSPrintInfo.AttributeKey](nsprintinfo/attributekey/lastpage.md)
  An `NSNumber` object containing an integer value that specifies the last page in the print job.
- [static let mustCollate: NSPrintInfo.AttributeKey](nsprintinfo/attributekey/mustcollate.md)
  An `NSNumber` object containing a Boolean value—if [`true`](https://developer.apple.com/documentation/swift/true), collates output.
- [static let pagesAcross: NSPrintInfo.AttributeKey](nsprintinfo/attributekey/pagesacross.md)
  An `NSNumber` object that specifies the number of logical pages to be tiled horizontally on a physical sheet of paper.
- [static let pagesDown: NSPrintInfo.AttributeKey](nsprintinfo/attributekey/pagesdown.md)
  An `NSNumber` object that specifies the number of logical pages to be tiled vertically on a physical sheet of paper.
- [static let printer: NSPrintInfo.AttributeKey](nsprintinfo/attributekey/printer.md)
  An `NSPrinter` object—the printer to use.
- [static let printerName: NSPrintInfo.AttributeKey](nsprintinfo/attributekey/printername.md)
  An `NSString` object that specifies the name of a printer.
- [static let reversePageOrder: NSPrintInfo.AttributeKey](nsprintinfo/attributekey/reversepageorder.md)
  An `NSNumber` object containing a Boolean value—if [`true`](https://developer.apple.com/documentation/swift/true), prints first page last.
- [static let selectionOnly: NSPrintInfo.AttributeKey](nsprintinfo/attributekey/selectiononly.md)
  An `NSNumber` object containing a Boolean value—if [`true`](https://developer.apple.com/documentation/swift/true) only the current selection is printed.
- [static let time: NSPrintInfo.AttributeKey](nsprintinfo/attributekey/time.md)
  An `NSDate` object that specifies the time at which printing should begin.
### Initializers
- [init(String)](nsprintinfo/attributekey/init(_:).md)
  Creates a print job attribute key.
- [init(rawValue: String)](nsprintinfo/attributekey/init(rawvalue:).md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintinfo/attributekey)*