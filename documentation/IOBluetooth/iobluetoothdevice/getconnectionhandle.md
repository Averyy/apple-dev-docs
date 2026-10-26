# getConnectionHandle

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Get the connection handle for the baseband connection.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```objc
- (BluetoothConnectionHandle) getConnectionHandle;
```

#### Return Value

Returns the connection handle for the baseband connection. If no baseband connection is present, kBluetoothConnectionHandleNone is returned.

#### Discussion

This method only returns a valid result if a baseband connection is present (-isConnected returns TRUE).

## See Also

### Related Documentation
- [var connectionHandle: BluetoothConnectionHandle](./connectionhandle.md)
  Get the connection handle for the baseband connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/getconnectionhandle)*