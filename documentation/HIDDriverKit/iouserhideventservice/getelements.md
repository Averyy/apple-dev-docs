# getElements

**Framework**: HIDDriverKit  
**Kind**: method

Returns an array of elements that contain the parsed data from the HID device’s report.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
OSArray * getElements();
```

#### Return Value

An array of [`IOHIDElement`](iohidelement.md) objects containing the parsed data from the report.

#### Discussion

Use this method to get the array of [`IOHIDElement`](iohidelement.md) objects that contain the data for the most recent device report. Each element contains data for a single aspect of the device’s state. For example, a report from a stylus contains separate elements for the horizontal and vertical position of the stylus, the pressure values, and so on. Use the [`getUsagePage`](iohidelement/getusagepage.md) and [`getUsage`](iohidelement/getusage.md) methods of the element to determine the type of information in each element.

This method creates a new set of [`IOHIDElement`](iohidelement.md) objects the first time you call it. On subequent calls, it updates the existing [`IOHIDElement`](iohidelement.md) objects with data from the most recent report.

## See Also

- [handleReport](iouserhideventservice/handlereport.md)
  Converts an incoming device report into dispatchable events.
- [ReportAvailable](iouserhideventservice/reportavailable.md)
  Notifies the event service that an updated report is available from the HID device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserhideventservice/getelements)*