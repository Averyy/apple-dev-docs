# hasOpenTransportConnection()

**Framework**: IOBluetooth  
**Kind**: method

An OBEXSession override. When this is called by the session baseclass, we will return whether or not we have a transport connection established to another OBEX server/client. In our case we will tell whether or not the RFCOMM channel to a remote device is still open.

**Availability**:
- macOS ?+

## Declaration

```swift
func hasOpenTransportConnection() -> Bool
```

#### Return Value

True or false, whether there is already an open transport connection for this OBEX session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothobexsession/hasopentransportconnection())*