# getRFCOMMChannel()

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Get the Bluetooth RFCOMM channel being used by the session object.

**Availability**:
- macOS

## Declaration

```swift
func getRFCOMMChannel() -> IOBluetoothRFCOMMChannel!
```

```objc
- (IOBluetoothRFCOMMChannel *) getRFCOMMChannel;
```

#### Return Value

A IOBluetoothRFCOMMChannel object.

#### Discussion

This could potentially be nil even though you have a valid OBEX session, because the RFCOMM channel is only valid when the session is connected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothobexsession/getrfcommchannel())*