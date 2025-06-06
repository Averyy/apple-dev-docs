# getLastInquiryUpdate()

**Framework**: IOBluetooth  
**Kind**: method

Get the date/time of the last time the device was returned during an inquiry.

**Availability**:
- macOS ?+

## Declaration

```swift
func getLastInquiryUpdate() -> Date!
```

#### Return Value

Returns the date/time of the last time the device was seen during an inquiry. If the device has never been seen during an inquiry, nil is returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/getlastinquiryupdate())*