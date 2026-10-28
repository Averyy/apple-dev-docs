# CompleteReport

**Framework**: HIDDriverKit  
**Kind**: method  
**Role**: Instance Method

Completes all async requests made when getting or setting a report.

**Availability**:
- DriverKit 19.0+
- macOS

## Declaration

```cpp
virtual void CompleteReport(OSAction *action, IOReturn status, uint32_t actualByteCount);
```

## Discussion

Call this method upon completion of the [`getReport`](./getreport.md) and [`setReport`](./setreport.md) methods.

## Parameters

- `action`: The action passed to the `getReport` or `setReport` methods.
- `status`: The completion status.
- `actualByteCount`: The size of the buffer sent to the `getReport` or `setReport` methods.

## See Also

### Processing Device Reports
- [handleReport](./handlereport.md)
  Handles an asynchronous report received from the HID device.
- [getReport](./getreport.md)
  Gets a report from the HID device.
- [setReport](./setreport.md)
  Sends a report to the HID device.
- [Report Options](../report-options-enum.md)
  The enumerated report options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohiddevice/completereport)*