# withObjectID(_:)

**Framework**: IOBluetooth  
**Kind**: method

Returns the IObluetoothL2CAPChannel with the given IOBluetoothObjectID.

**Availability**:
- macOS ?+

## Declaration

```swift
class func withObjectID(_ objectID: IOBluetoothObjectID) -> Self!
```

#### Return Value

Returns the IOBluetoothL2CAPChannel that matches the given IOBluetoothObjectID if one exists. If no matching L2CAP channel exists, nil is returned.

#### Discussion

The IOBluetoothObjectID can be used as a global reference for a given IOBluetoothL2CAPChannel. It allows two separate applications to refer to the same IOBluetoothL2CAPChannel object.

## Parameters

- `objectID`: IOBluetoothObjectID of the desired IOBluetoothL2CAPChannel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannel/withobjectid(_:))*