# getNameOrAddress

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Get the human readable name of the remote device. If the name is not present, it will return a string containing the device’s address.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```objc
- (NSString *) getNameOrAddress;
```

## Return Value

Returns the device’s name or a string containing the device’s address.

## Discussion

If a remote name request has been successfully completed, the device name will be returned. If not, a string containg the device address in the format of “XX-XX-XX-XX-XX-XX” will be returned.

## See Also

### Related Documentation
- [var nameOrAddress: String!](./nameoraddress.md)
  Get the human readable name of the remote device. If the name is not present, it will return a string containing the device’s address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/getnameoraddress)*