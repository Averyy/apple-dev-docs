# pagesAcross

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

An `NSNumber` object that specifies the number of logical pages to be tiled horizontally on a physical sheet of paper.

**Availability**:
- macOS

## Declaration

```swift
static let pagesAcross: NSPrintInfo.AttributeKey
```

```c
extern NSPrintInfoAttributeKey const NSPrintPagesAcross;
```

## See Also

### Other Attributes
- [static let allPages: NSPrintInfo.AttributeKey](./allpages.md)
  An `NSNumber` object containing a Boolean value that specifies whether to include all pages.
- [static let copies: NSPrintInfo.AttributeKey](./copies.md)
  An `NSNumber` object containing an integer—the number of copies to spool.
- [static let detailedErrorReporting: NSPrintInfo.AttributeKey](./detailederrorreporting.md)
  An `NSNumber` object containing a Boolean value that specifies whether to produce detailed error reports.
- [static let faxNumber: NSPrintInfo.AttributeKey](./faxnumber.md)
  An `NSString` object that specifies a fax number.
- [static let firstPage: NSPrintInfo.AttributeKey](./firstpage.md)
  An `NSNumber` object containing an integer value that specifies the first page in the print job.
- [static let headerAndFooter: NSPrintInfo.AttributeKey](./headerandfooter.md)
  An `NSNumber` object containing a Boolean value that specifies whether to include a header and footer.
- [static let jobDisposition: NSPrintInfo.AttributeKey](./jobdisposition.md)
  An `NSString` object that specifies the job disposition.
- [static let jobSavingFileNameExtensionHidden: NSPrintInfo.AttributeKey](./jobsavingfilenameextensionhidden.md)
  An `NSNumber` object containing a Boolean value that specifies whether to hide the job’s file name extension.
- [static let jobSavingURL: NSPrintInfo.AttributeKey](./jobsavingurl.md)
  An `NSURL` containing the location to which the job file will be saved when the [`jobDisposition`](../jobdisposition-swift.property.md) is [`save`](../jobdisposition-swift.struct/save.md).
- [static let lastPage: NSPrintInfo.AttributeKey](./lastpage.md)
  An `NSNumber` object containing an integer value that specifies the last page in the print job.
- [static let mustCollate: NSPrintInfo.AttributeKey](./mustcollate.md)
  An `NSNumber` object containing a Boolean value that specifies whether to collate output.
- [static let pagesDown: NSPrintInfo.AttributeKey](./pagesdown.md)
  An `NSNumber` object that specifies the number of logical pages to be tiled vertically on a physical sheet of paper.
- [static let printer: NSPrintInfo.AttributeKey](./printer.md)
  An `NSPrinter` object—the printer to use.
- [static let printerName: NSPrintInfo.AttributeKey](./printername.md)
  An `NSString` object that specifies the name of a printer.
- [static let reversePageOrder: NSPrintInfo.AttributeKey](./reversepageorder.md)
  An `NSNumber` object containing a Boolean value that specifies whether to print pages in reverse order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintinfo/attributekey/pagesacross)*