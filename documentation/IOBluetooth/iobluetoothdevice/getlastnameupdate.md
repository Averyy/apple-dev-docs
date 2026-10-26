# getLastNameUpdate

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Get the date/time of the last successful remote name request.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```objc
- (NSDate *) getLastNameUpdate;
```

#### Return Value

Returns the date/time of the last successful remote name request. If no remote name request has been completed on the target device, nil is returned.

## See Also

### Related Documentation
- [var lastNameUpdate: Date!](./lastnameupdate.md)
  Get the date/time of the last successful remote name request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/getlastnameupdate)*