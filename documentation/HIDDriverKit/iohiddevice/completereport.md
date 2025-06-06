# CompleteReport

**Framework**: HIDDriverKit  
**Kind**: method

Completes all async requests made when getting or setting a report.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
void CompleteReport(OSAction * action, IOReturn status, uint32_t actualByteCount);
```

#### Discussion

Call this method upon completion of the [`getReport`](iohiddevice/getreport.md) and [`setReport`](iohiddevice/setreport.md) methods.

## Parameters

- `action`: The action passed to the   or   methods.
- `status`: The completion status.
- `actualByteCount`: The size of the buffer sent to the   or   methods.

## See Also

- [handleReport](iohiddevice/handlereport.md)
  Handles an asynchronous report received from the HID device.
- [getReport](iohiddevice/getreport.md)
  Gets a report from the HID device.
- [setReport](iohiddevice/setreport.md)
  Sends a report to the HID device.
- [Report Options](report-options-enum.md)
  The enumerated report options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohiddevice/completereport)*