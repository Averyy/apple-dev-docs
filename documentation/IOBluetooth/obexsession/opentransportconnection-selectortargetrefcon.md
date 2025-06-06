# openTransportConnection(_:selectorTarget:refCon:)

**Framework**: IOBluetooth  
**Kind**: method

Opens a transport connection to a device. A Bluetooth connection is one example of a transport.

**Availability**:
- macOS ?+

## Declaration

```swift
func openTransportConnection(_ inSelector: Selector!, selectorTarget inTarget: Any!, refCon inUserRefCon: UnsafeMutableRawPointer!) -> OBEXError
```

#### Discussion

Tranport subclasses must override this! when called you should attempt to open your transport connection, and if you are successful, return kOBEXSuccess, otherwise an interesting error code.

## Parameters

- `inSelector`: Selector to call for success, failure or timeout.
- `inTarget`: Target on which to call the selector.
- `inUserRefCon`: Caller’s reference constant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexsession/opentransportconnection(_:selectortarget:refcon:))*