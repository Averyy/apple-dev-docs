# openTransportConnection(_:selectorTarget:refCon:)

**Framework**: IOBluetooth  
**Kind**: method

An OBEXSession override. When this is called by the session baseclass, we will attempt to open the transport connection. In our case, this would be an RFCOMM channel to another Bluetooth device.

**Availability**:
- macOS ?+

## Declaration

```swift
func openTransportConnection(_ inSelector: Selector!, selectorTarget inTarget: Any!, refCon inUserRefCon: UnsafeMutableRawPointer!) -> OBEXError
```

#### Discussion

Your selector should have the following signature:

-(void)transportConnectionSelector:(id)refcon status:(OBEXError)status;

Thus you could use it with openTransportConnection like this:

OBEXError error = [anOBEXSession openTransportConnection:@selector( transportConnectionSelector:status: ) selectorTarget:self refCon:anOBEXSession]; // or whatever you want to pass as a refCon…

Be sure to check the status code! Assume the connection was not opened unless status is kOBEXSuccess.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothobexsession/opentransportconnection(_:selectortarget:refcon:))*