# pagesAcross

**Framework**: AppKit  
**Kind**: property

An `NSNumber` object that specifies the number of logical pages to be tiled horizontally on a physical sheet of paper.

**Availability**:
- macOS ?+

## Declaration

```swift
static let pagesAcross: NSPrintInfo.AttributeKey
```

## See Also

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
- [static let pagesDown: NSPrintInfo.AttributeKey](nsprintinfo/attributekey/pagesdown.md)
  An `NSNumber` object that specifies the number of logical pages to be tiled vertically on a physical sheet of paper.
- [static let printer: NSPrintInfo.AttributeKey](nsprintinfo/attributekey/printer.md)
  An `NSPrinter` object—the printer to use.
- [static let printerName: NSPrintInfo.AttributeKey](nsprintinfo/attributekey/printername.md)
  An `NSString` object that specifies the name of a printer.
- [static let reversePageOrder: NSPrintInfo.AttributeKey](nsprintinfo/attributekey/reversepageorder.md)
  An `NSNumber` object containing a Boolean value—if [`true`](https://developer.apple.com/documentation/swift/true), prints first page last.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintinfo/attributekey/pagesacross)*