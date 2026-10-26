# deviceClassMinor

**Framework**: IOBluetooth  
**Kind**: property  
**Role**: Instance Property

Get the minor service class of the device.

**Availability**:
- macOS

## Declaration

```swift
var deviceClassMinor: BluetoothDeviceClassMinor { get }
```

```objc
@property (readonly) BluetoothDeviceClassMinor deviceClassMinor;
```

#### Discussion

This value is only meaningful if the target device has been seen during an inquiry. This can be by checking the result of -getLastInquiryUpdate. If nil is returned, then the device hasn’t been seen.

## See Also

### Related Documentation
- [- getDeviceClassMinor](./getdeviceclassminor.md)
  Get the minor service class of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/deviceclassminor)*