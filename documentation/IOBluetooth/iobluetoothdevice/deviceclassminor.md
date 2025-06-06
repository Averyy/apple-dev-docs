# deviceClassMinor

**Framework**: IOBluetooth  
**Kind**: property

Get the minor service class of the device.

**Availability**:
- macOS ?+

## Declaration

```swift
var deviceClassMinor: BluetoothDeviceClassMinor { get }
```

#### Discussion

This value is only meaningful if the target device has been seen during an inquiry. This can be by checking the result of -getLastInquiryUpdate. If nil is returned, then the device hasn’t been seen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/deviceclassminor)*