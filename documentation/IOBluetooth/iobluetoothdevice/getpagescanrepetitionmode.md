# getPageScanRepetitionMode()

**Framework**: IOBluetooth  
**Kind**: method

Get the value of the page scan repetition mode for the device.

**Availability**:
- macOS ?+

## Declaration

```swift
func getPageScanRepetitionMode() -> BluetoothPageScanRepetitionMode
```

#### Return Value

Returns the page scan repetition mode value for this device.

#### Discussion

This value is only meaningful if the target device has been seen during an inquiry. This can be by checking the result of -getLastInquiryUpdate. If nil is returned, then the device hasn’t been seen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/getpagescanrepetitionmode())*