# getClassOfDevice

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Gets the full class of device value for the remote device.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```objc
- (BluetoothClassOfDevice) getClassOfDevice;
```

#### Return Value

Returns the class of device for the remote device.

#### Discussion

This value is only meaningful if the target device has been seen during an inquiry. This can be by checking the result of -getLastInquiryUpdate. If nil is returned, then the device hasn’t been seen.

## See Also

### Related Documentation
- [var classOfDevice: BluetoothClassOfDevice](./classofdevice.md)
  Gets the full class of device value for the remote device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/getclassofdevice)*