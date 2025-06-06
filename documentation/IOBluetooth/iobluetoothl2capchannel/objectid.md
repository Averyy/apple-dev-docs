# objectID

**Framework**: IOBluetooth  
**Kind**: property

Returns the IOBluetoothObjectID of the given IOBluetoothL2CAPChannel.

**Availability**:
- macOS ?+

## Declaration

```swift
var objectID: IOBluetoothObjectID { get }
```

#### Discussion

The IOBluetoothObjectID can be used as a global reference for a given IOBluetoothL2CAPChannel. It allows two separate applications to refer to the same IOBluetoothL2CAPChannel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannel/objectid)*