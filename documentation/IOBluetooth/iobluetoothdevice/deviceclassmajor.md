# deviceClassMajor

**Framework**: IOBluetooth  
**Kind**: property

Get the major device class of the device.

**Availability**:
- macOS ?+

## Declaration

```swift
var deviceClassMajor: BluetoothDeviceClassMajor { get }
```

#### Discussion

This value is only meaningful if the target device has been seen during an inquiry. This can be by checking the result of -getLastInquiryUpdate. If nil is returned, then the device hasn’t been seen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/deviceclassmajor)*