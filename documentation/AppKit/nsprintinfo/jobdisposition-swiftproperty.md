# jobDisposition

**Framework**: AppKit  
**Kind**: property

The action specified for the job.

**Availability**:
- macOS ?+

## Declaration

```swift
var jobDisposition: NSPrintInfo.JobDisposition { get set }
```

#### Discussion

One of the following value:

- [`spool`](nsprintinfo/jobdisposition-swift.struct/spool.md) is a normal print job.
- [`preview`](nsprintinfo/jobdisposition-swift.struct/preview.md) sends the print job to the Preview application.
- [`save`](nsprintinfo/jobdisposition-swift.struct/save.md) saves the print job to a file.
- [`cancel`](nsprintinfo/jobdisposition-swift.struct/cancel.md) aborts the print job.

## See Also

- [NSPrintInfo.JobDisposition](nsprintinfo/jobdisposition-swift.struct.md)
  Constants that specify values for the print job disposition.
- [func setUpPrintOperationDefaultValues()](nsprintinfo/setupprintoperationdefaultvalues.md)
  Validates the attributes encapsulated by the print info.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintinfo/jobdisposition-swift.property)*