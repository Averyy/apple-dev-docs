# getAddressString

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Get a string representation of the Bluetooth device address for the target device. The format of the string is the same as returned by IOBluetoothNSStringFromDeviceAddress().

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```objc
- (NSString *) getAddressString;
```

## Return Value

Returns an NSString containing the Bluetooth device address of the target device.

## Discussion

NOTE: This method is only available in macOS 10.2.4 (Bluetooth v1.1) or later.

## See Also

### Related Documentation
- [var addressString: String!](./addressstring.md)
  Get a string representation of the Bluetooth device address for the target device. The format of the string is the same as returned by IOBluetoothNSStringFromDeviceAddress().


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/getaddressstring)*