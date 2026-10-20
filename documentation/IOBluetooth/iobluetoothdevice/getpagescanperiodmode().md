# getPageScanPeriodMode()

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Get the value of the page scan period mode for the device.

**Availability**:
- macOS

## Declaration

```swift
func getPageScanPeriodMode() -> BluetoothPageScanPeriodMode
```

```objc
- (BluetoothPageScanPeriodMode) getPageScanPeriodMode;
```

#### Return Value

Returns page scan period mode value for the device.

#### Discussion

This value is only meaningful if the target device has been seen during an inquiry. This can be by checking the result of -getLastInquiryUpdate. If nil is returned, then the device hasn’t been seen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/getpagescanperiodmode())*