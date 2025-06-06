# connectionHandle

**Framework**: IOBluetooth  
**Kind**: property

Get the connection handle for the baseband connection.

**Availability**:
- macOS ?+

## Declaration

```swift
var connectionHandle: BluetoothConnectionHandle { get }
```

#### Discussion

This method only returns a valid result if a baseband connection is present (-isConnected returns TRUE).


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/connectionhandle)*