# connectionHandle

**Framework**: IOBluetooth  
**Kind**: property  
**Role**: Instance Property

Get the connection handle for the baseband connection.

**Availability**:
- macOS

## Declaration

```swift
var connectionHandle: BluetoothConnectionHandle { get }
```

```objc
@property (assign, readonly) BluetoothConnectionHandle connectionHandle;
```

#### Discussion

This method only returns a valid result if a baseband connection is present (-isConnected returns TRUE).


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/connectionhandle)*