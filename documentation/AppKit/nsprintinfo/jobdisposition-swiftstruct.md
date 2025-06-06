# NSPrintInfo.JobDisposition

**Framework**: AppKit  
**Kind**: struct

Constants that specify values for the print job disposition.

**Availability**:
- macOS ?+

## Declaration

```swift
struct JobDisposition
```

#### Discussion

These constants are used by the [`jobDisposition`](nsprintinfo/jobdisposition-swift.property.md) property.

## Topics

### Constants
- [static let spool: NSPrintInfo.JobDisposition](nsprintinfo/jobdisposition-swift.struct/spool.md)
  Normal print job.
- [static let preview: NSPrintInfo.JobDisposition](nsprintinfo/jobdisposition-swift.struct/preview.md)
  Send to Preview application.
- [static let save: NSPrintInfo.JobDisposition](nsprintinfo/jobdisposition-swift.struct/save.md)
  Save to a file.
- [static let cancel: NSPrintInfo.JobDisposition](nsprintinfo/jobdisposition-swift.struct/cancel.md)
  Cancel print job.
### Initializers
- [init(rawValue: String)](nsprintinfo/jobdisposition-swift.struct/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var jobDisposition: NSPrintInfo.JobDisposition](nsprintinfo/jobdisposition-swift.property.md)
  The action specified for the job.
- [func setUpPrintOperationDefaultValues()](nsprintinfo/setupprintoperationdefaultvalues.md)
  Validates the attributes encapsulated by the print info.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintinfo/jobdisposition-swift.struct)*