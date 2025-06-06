# serverHandleIncomingData(_:)

**Framework**: IOBluetooth  
**Kind**: method

Tranport subclasses need to invoke this from their own data-receive handlers. For example, when data is received over a Bluetooth RFCOMM channel in the IOBluetoothOBEXSession, it in turn calls this to dispatch the data. If you do not handle this case, your server session will not work, guaranteed.

**Availability**:
- macOS ?+

## Declaration

```swift
func serverHandleIncomingData(_ event: UnsafeMutablePointer<OBEXTransportEvent>!)
```

#### Discussion

Tranport subclasses must call this for OBEX server sessions to work!

## Parameters

- `event`: New event received from the transport.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexsession/serverhandleincomingdata(_:))*