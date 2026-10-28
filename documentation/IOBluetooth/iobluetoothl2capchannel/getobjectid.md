# getObjectID

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Returns the IOBluetoothObjectID of the given IOBluetoothL2CAPChannel.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```objc
- (IOBluetoothObjectID) getObjectID;
```

## Return Value

Returns the IOBluetoothObjectID of the given IOBluetoothL2CAPChannel.

## Discussion

The IOBluetoothObjectID can be used as a global reference for a given IOBluetoothL2CAPChannel. It allows two separate applications to refer to the same IOBluetoothL2CAPChannel.

## See Also

### Related Documentation
- [var objectID: IOBluetoothObjectID](./objectid.md)
  Returns the IOBluetoothObjectID of the given IOBluetoothL2CAPChannel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannel/getobjectid)*