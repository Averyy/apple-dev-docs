# setUpPrintOperationDefaultValues()

**Framework**: AppKit  
**Kind**: method

Validates the attributes encapsulated by the print info.

**Availability**:
- macOS ?+

## Declaration

```swift
func setUpPrintOperationDefaultValues()
```

#### Discussion

Invoked when the print operation is about to start. Subclasses may override this method to set default values for any attributes that are not set.

## See Also

- [var jobDisposition: NSPrintInfo.JobDisposition](nsprintinfo/jobdisposition-swift.property.md)
  The action specified for the job.
- [NSPrintInfo.JobDisposition](nsprintinfo/jobdisposition-swift.struct.md)
  Constants that specify values for the print job disposition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintinfo/setupprintoperationdefaultvalues())*