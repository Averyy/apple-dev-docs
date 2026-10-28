# jobDisposition

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The action specified for the job.

**Availability**:
- macOS

## Declaration

```swift
var jobDisposition: NSPrintInfo.JobDisposition { get set }
```

```objc
@property (copy) NSPrintJobDispositionValue jobDisposition;
```

## Discussion

One of the following value:

- [`spool`](./jobdisposition-swift.struct/spool.md) is a normal print job.
- [`preview`](./jobdisposition-swift.struct/preview.md) sends the print job to the Preview application.
- [`save`](./jobdisposition-swift.struct/save.md) saves the print job to a file.
- [`cancel`](./jobdisposition-swift.struct/cancel.md) aborts the print job.

## See Also

### Controlling Printing
- [NSPrintInfo.JobDisposition](./jobdisposition-swift.struct.md)
  Constants that specify values for the print job disposition.
- [func setUpPrintOperationDefaultValues()](./setupprintoperationdefaultvalues%28%29.md)
  Validates the attributes encapsulated by the print info.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintinfo/jobdisposition-swift.property)*