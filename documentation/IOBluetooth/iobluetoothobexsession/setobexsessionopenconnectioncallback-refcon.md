# setOBEXSessionOpenConnectionCallback(_:refCon:)

**Framework**: IOBluetooth  
**Kind**: method

For C API support. Allows you to set the callback to be invoked when the OBEX connection is actually opened.

**Availability**:
- macOS ?+

## Declaration

```swift
func setOBEXSessionOpenConnectionCallback(_ inCallback: IOBluetoothOBEXSessionOpenConnectionCallback!, refCon inUserRefCon: UnsafeMutableRawPointer!)
```

## Parameters

- `inCallback`: Function to call on the target.
- `inUserRefCon`: User’s reference constant, will be returned on the callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothobexsession/setobexsessionopenconnectioncallback(_:refcon:))*