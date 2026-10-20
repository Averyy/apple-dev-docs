# setOBEXSessionOpenConnectionCallback(_:refCon:)

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

For C API support. Allows you to set the callback to be invoked when the OBEX connection is actually opened.

**Availability**:
- macOS

## Declaration

```swift
func setOBEXSessionOpenConnectionCallback(_ inCallback: IOBluetoothOBEXSessionOpenConnectionCallback!, refCon inUserRefCon: UnsafeMutableRawPointer!)
```

```objc
- (void) setOBEXSessionOpenConnectionCallback:(IOBluetoothOBEXSessionOpenConnectionCallback) inCallback refCon:(void *) inUserRefCon;
```

## Parameters

- `inCallback`: Function to call on the target.
- `inUserRefCon`: User’s reference constant, will be returned on the callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothobexsession/setobexsessionopenconnectioncallback(_:refcon:))*