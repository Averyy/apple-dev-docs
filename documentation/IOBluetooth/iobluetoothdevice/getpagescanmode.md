# getPageScanMode()

**Framework**: IOBluetooth  
**Kind**: method

Get the page scan mode for the device.

**Availability**:
- macOS ?+

## Declaration

```swift
func getPageScanMode() -> BluetoothPageScanMode
```

#### Return Value

Returns the value for the page scan mode for the device.

#### Discussion

This value is only meaningful if the target device has been seen during an inquiry. This can be by checking the result of -getLastInquiryUpdate. If nil is returned, then the device hasn’t been seen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/getpagescanmode())*