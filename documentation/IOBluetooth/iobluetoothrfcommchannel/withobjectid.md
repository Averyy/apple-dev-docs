# withObjectID(_:)

**Framework**: IOBluetooth  
**Kind**: method

Returns the IObluetoothRFCOMMChannel with the given IOBluetoothObjectID.

**Availability**:
- macOS ?+

## Declaration

```swift
class func withObjectID(_ objectID: IOBluetoothObjectID) -> Self!
```

#### Return Value

Returns the IObluetoothRFCOMMChannel that matches the given IOBluetoothObjectID if one exists. If no matching RFCOMM channel exists, nil is returned.

#### Discussion

The IOBluetoothObjectID can be used as a global reference for a given IObluetoothRFCOMMChannel. It allows two separate applications to refer to the same IObluetoothRFCOMMChannel object.

## Parameters

- `objectID`: IOBluetoothObjectID of the desired IObluetoothRFCOMMChannel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothrfcommchannel/withobjectid(_:))*