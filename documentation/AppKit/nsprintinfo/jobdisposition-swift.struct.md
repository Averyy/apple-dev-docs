# NSPrintInfo.JobDisposition

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants that specify values for the print job disposition.

**Availability**:
- macOS

## Declaration

```swift
struct JobDisposition
```

```c
typedef NSString * NSPrintJobDispositionValue;
```

## Discussion

These constants are used by the [`jobDisposition`](./jobdisposition-swift.property.md) property.

## Topics

### Constants
- [static let spool: NSPrintInfo.JobDisposition](./jobdisposition-swift.struct/spool.md)
  Normal print job.
- [static let preview: NSPrintInfo.JobDisposition](./jobdisposition-swift.struct/preview.md)
  Send to Preview application.
- [static let save: NSPrintInfo.JobDisposition](./jobdisposition-swift.struct/save.md)
  Save to a file.
- [static let cancel: NSPrintInfo.JobDisposition](./jobdisposition-swift.struct/cancel.md)
  Cancel print job.
### Initializers
- [init(rawValue: String)](./jobdisposition-swift.struct/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Controlling Printing
- [var jobDisposition: NSPrintInfo.JobDisposition](./jobdisposition-swift.property.md)
  The action specified for the job.
- [func setUpPrintOperationDefaultValues()](./setupprintoperationdefaultvalues%28%29.md)
  Validates the attributes encapsulated by the print info.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintinfo/jobdisposition-swift.struct)*