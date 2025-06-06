# sendRemoteLineStatus(_:)

**Framework**: IOBluetooth  
**Kind**: method

Sends an error to the remote side.

**Availability**:
- macOS ?+

## Declaration

```swift
func sendRemoteLineStatus(_ lineStatus: BluetoothRFCOMMLineStatus) -> IOReturn
```

#### Return Value

An error code value. 0 if successful.

## Parameters

- `lineStatus`: The error type. The error code can be NoError, OverrunError, ParityError or FramingError.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothrfcommchannel/sendremotelinestatus(_:))*