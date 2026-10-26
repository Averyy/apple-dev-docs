# deviceClassMajor

**Framework**: IOBluetooth  
**Kind**: property  
**Role**: Instance Property

Get the major device class of the device.

**Availability**:
- macOS

## Declaration

```swift
var deviceClassMajor: BluetoothDeviceClassMajor { get }
```

```objc
@property (readonly) BluetoothDeviceClassMajor deviceClassMajor;
```

#### Discussion

This value is only meaningful if the target device has been seen during an inquiry. This can be by checking the result of -getLastInquiryUpdate. If nil is returned, then the device hasn’t been seen.

## See Also

### Related Documentation
- [- getDeviceClassMajor](./getdeviceclassmajor.md)
  Get the major device class of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/deviceclassmajor)*