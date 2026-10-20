# NSPrintInfo.AttributeKey

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants that specify print job attributes.

**Availability**:
- macOS

## Declaration

```swift
struct AttributeKey
```

```c
typedef NSString * NSPrintInfoAttributeKey;
```

## Topics

### Page Setup Attributes
- [static let paperName: NSPrintInfo.AttributeKey](./attributekey/papername.md)
  An `NSString` object containing the paper name.
- [static let paperSize: NSPrintInfo.AttributeKey](./attributekey/papersize.md)
  An `NSSize` value specifying the height and width of paper in points.
- [static let orientation: NSPrintInfo.AttributeKey](./attributekey/orientation.md)
  An `NSNumber` object containing an `NSPrintingOrientation`.
- [static let scalingFactor: NSPrintInfo.AttributeKey](./attributekey/scalingfactor.md)
  Scale factor percentage before pagination.
### Pagination Attributes
- [static let leftMargin: NSPrintInfo.AttributeKey](./attributekey/leftmargin.md)
  `NSNumber`, containing a floating-point value that specifies the left margin, in points.
- [static let rightMargin: NSPrintInfo.AttributeKey](./attributekey/rightmargin.md)
  `NSNumber`, containing a floating-point value that specifies the right margin, in points.
- [static let topMargin: NSPrintInfo.AttributeKey](./attributekey/topmargin.md)
  `NSNumber`, containing a floating-point value that specifies the top margin, in points.
- [static let bottomMargin: NSPrintInfo.AttributeKey](./attributekey/bottommargin.md)
  `NSNumber`, containing a floating-point value that specifies the bottom margin, in points.
- [static let horizontallyCentered: NSPrintInfo.AttributeKey](./attributekey/horizontallycentered.md)
  An `NSNumber` object containing a Boolean value that specifies whether to horizontally center pages.
- [static let verticallyCentered: NSPrintInfo.AttributeKey](./attributekey/verticallycentered.md)
  An `NSNumber` object containing a Boolean value that specifies whether to vertically center pages.
- [static let horizontalPagination: NSPrintInfo.AttributeKey](./attributekey/horizontalpagination.md)
  `NSNumber`, containing a `NSPrintingPaginationMode` value.
- [static let verticalPagination: NSPrintInfo.AttributeKey](./attributekey/verticalpagination.md)
  `NSNumber`, containing a `NSPrintingPaginationMode` value.
### Other Attributes
- [static let allPages: NSPrintInfo.AttributeKey](./attributekey/allpages.md)
  An `NSNumber` object containing a Boolean value that specifies whether to include all pages.
- [static let copies: NSPrintInfo.AttributeKey](./attributekey/copies.md)
  An `NSNumber` object containing an integer—the number of copies to spool.
- [static let detailedErrorReporting: NSPrintInfo.AttributeKey](./attributekey/detailederrorreporting.md)
  An `NSNumber` object containing a Boolean value that specifies whether to produce detailed error reports.
- [static let faxNumber: NSPrintInfo.AttributeKey](./attributekey/faxnumber.md)
  An `NSString` object that specifies a fax number.
- [static let firstPage: NSPrintInfo.AttributeKey](./attributekey/firstpage.md)
  An `NSNumber` object containing an integer value that specifies the first page in the print job.
- [static let headerAndFooter: NSPrintInfo.AttributeKey](./attributekey/headerandfooter.md)
  An `NSNumber` object containing a Boolean value that specifies whether to include a header and footer.
- [static let jobDisposition: NSPrintInfo.AttributeKey](./attributekey/jobdisposition.md)
  An `NSString` object that specifies the job disposition.
- [static let jobSavingFileNameExtensionHidden: NSPrintInfo.AttributeKey](./attributekey/jobsavingfilenameextensionhidden.md)
  An `NSNumber` object containing a Boolean value that specifies whether to hide the job’s file name extension.
- [static let jobSavingURL: NSPrintInfo.AttributeKey](./attributekey/jobsavingurl.md)
  An `NSURL` containing the location to which the job file will be saved when the [`jobDisposition`](./jobdisposition-swift.property.md) is [`save`](./jobdisposition-swift.struct/save.md).
- [static let lastPage: NSPrintInfo.AttributeKey](./attributekey/lastpage.md)
  An `NSNumber` object containing an integer value that specifies the last page in the print job.
- [static let mustCollate: NSPrintInfo.AttributeKey](./attributekey/mustcollate.md)
  An `NSNumber` object containing a Boolean value that specifies whether to collate output.
- [static let pagesAcross: NSPrintInfo.AttributeKey](./attributekey/pagesacross.md)
  An `NSNumber` object that specifies the number of logical pages to be tiled horizontally on a physical sheet of paper.
- [static let pagesDown: NSPrintInfo.AttributeKey](./attributekey/pagesdown.md)
  An `NSNumber` object that specifies the number of logical pages to be tiled vertically on a physical sheet of paper.
- [static let printer: NSPrintInfo.AttributeKey](./attributekey/printer.md)
  An `NSPrinter` object—the printer to use.
- [static let printerName: NSPrintInfo.AttributeKey](./attributekey/printername.md)
  An `NSString` object that specifies the name of a printer.
- [static let reversePageOrder: NSPrintInfo.AttributeKey](./attributekey/reversepageorder.md)
  An `NSNumber` object containing a Boolean value that specifies whether to print pages in reverse order.
- [static let selectionOnly: NSPrintInfo.AttributeKey](./attributekey/selectiononly.md)
  An `NSNumber` object containing a Boolean value that specifies whether to print the current selection.
- [static let time: NSPrintInfo.AttributeKey](./attributekey/time.md)
  An `NSDate` object that specifies the time at which printing should begin.
### Initializers
- [init(String)](./attributekey/init%28_%29.md)
  Creates a print job attribute key.
- [init(rawValue: String)](./attributekey/init%28rawvalue%29.md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintinfo/attributekey)*