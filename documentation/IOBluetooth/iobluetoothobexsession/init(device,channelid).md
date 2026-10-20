# init(device:channelID:)

**Framework**: IOBluetooth  
**Kind**: init  
**Role**: Initializer

Initializes a Bluetooth-based OBEX Session using a Bluetooth device.

**Availability**:
- macOS

## Declaration

```swift
init!(device inDevice: IOBluetoothDevice!, channelID inChannelID: BluetoothRFCOMMChannelID)
```

```objc
- (instancetype) initWithDevice:(IOBluetoothDevice *) inDevice channelID:(BluetoothRFCOMMChannelID) inChannelID;
```

## Parameters

- `inDevice`: The bluetooth device on which to open the OBEXSession.
- `inChannelID`: The RFCOMM channel ID to use when opening the connection.

## See Also

### Initializers
- [init!(incomingRFCOMMChannel: IOBluetoothRFCOMMChannel!, eventSelector: Selector!, selectorTarget: Any!, refCon: UnsafeMutableRawPointer!)](./init%28incomingrfcommchannel,eventselector,selectortarget,refcon%29.md)
  Initializes a Bluetooth-based OBEX Session using an incoming RFCOMM channel.
- [init!(sdpServiceRecord: IOBluetoothSDPServiceRecord!)](./init%28sdpservicerecord%29-h1xg.md)
  Initializes a Bluetooth-based OBEX Session using an SDP service record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothobexsession/init(device:channelid:))*