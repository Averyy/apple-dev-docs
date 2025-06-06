# newReportDescriptor

**Framework**: HIDDriverKit  
**Kind**: method

Returns the data in the HID device’s report descriptor.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
OSData * newReportDescriptor();
```

#### Return Value

An [`OSData`](https://developer.apple.com/documentation/DriverKit/OSData) object containing the report descriptor for the device.

#### Discussion

Override this method and use it to fetch the report descriptor from the device. Return the raw bytes for that report in an [`OSData`](https://developer.apple.com/documentation/DriverKit/OSData) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserhiddevice/newreportdescriptor)*