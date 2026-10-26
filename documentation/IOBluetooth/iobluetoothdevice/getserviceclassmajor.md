# getServiceClassMajor

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Get the major service class of the device.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```objc
- (BluetoothServiceClassMajor) getServiceClassMajor;
```

#### Return Value

Returns the major service class of the device.

#### Discussion

This value is only meaningful if the target device has been seen during an inquiry. This can be by checking the result of -getLastInquiryUpdate. If nil is returned, then the device hasn’t been seen.

## See Also

### Related Documentation
- [var serviceClassMajor: BluetoothServiceClassMajor](./serviceclassmajor.md)
  Get the major service class of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/getserviceclassmajor)*