# getName

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Get the human readable name of the remote device.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```objc
- (NSString *) getName;
```

## Return Value

Returns the name of the remote device name. This value is an NSString generated from the UTF-8 format of the most recent remote name request.

## Discussion

This only returns a value if a remote name request has been performed on the target device. If a successful remote name request has not been completed, nil is returned. To perform a remote name request, call -remoteNameRequest. If a remote name request has been successfully completed, the method -getLastNameUpdate will return the date/time of the last successful request.

## See Also

### Related Documentation
- [var name: String!](./name.md)
  Get the human readable name of the remote device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/getname)*