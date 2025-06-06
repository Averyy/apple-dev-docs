# serviceClassMajor

**Framework**: IOBluetooth  
**Kind**: property

Get the major service class of the device.

**Availability**:
- macOS ?+

## Declaration

```swift
var serviceClassMajor: BluetoothServiceClassMajor { get }
```

#### Discussion

This value is only meaningful if the target device has been seen during an inquiry. This can be by checking the result of -getLastInquiryUpdate. If nil is returned, then the device hasn’t been seen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/serviceclassmajor)*