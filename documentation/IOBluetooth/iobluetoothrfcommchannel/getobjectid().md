# getObjectID()

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Returns the IOBluetoothObjectID of the given IOBluetoothRFCOMMChannel.

**Availability**:
- macOS

## Declaration

```swift
func getObjectID() -> IOBluetoothObjectID
```

```objc
- (IOBluetoothObjectID) getObjectID;
```

#### Return Value

Returns the IOBluetoothObjectID of the given IOBluetoothRFCOMMChannel.

#### Discussion

The IOBluetoothObjectID can be used as a global reference for a given IOBluetoothRFCOMMChannel. It allows two separate applications to refer to the same IOBluetoothRFCOMMChannel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothrfcommchannel/getobjectid())*