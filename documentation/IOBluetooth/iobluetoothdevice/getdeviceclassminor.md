# getDeviceClassMinor

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Get the minor service class of the device.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```objc
- (BluetoothDeviceClassMinor) getDeviceClassMinor;
```

#### Return Value

Returns the minor device class of the remote device.

#### Discussion

This value is only meaningful if the target device has been seen during an inquiry. This can be by checking the result of -getLastInquiryUpdate. If nil is returned, then the device hasn’t been seen.

## See Also

### Related Documentation
- [var deviceClassMinor: BluetoothDeviceClassMinor](./deviceclassminor.md)
  Get the minor service class of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/getdeviceclassminor)*