# init(device:channelID:)

**Framework**: IOBluetooth  
**Kind**: init

Initializes a Bluetooth-based OBEX Session using a Bluetooth device.

**Availability**:
- macOS ?+

## Declaration

```swift
init!(device inDevice: IOBluetoothDevice!, channelID inChannelID: BluetoothRFCOMMChannelID)
```

## Parameters

- `inDevice`: The bluetooth device on which to open the OBEXSession.
- `inChannelID`: The RFCOMM channel ID to use when opening the connection.

## See Also

- [init!(incomingRFCOMMChannel: IOBluetoothRFCOMMChannel!, eventSelector: Selector!, selectorTarget: Any!, refCon: UnsafeMutableRawPointer!)](iobluetoothobexsession/init(incomingrfcommchannel:eventselector:selectortarget:refcon:).md)
  Initializes a Bluetooth-based OBEX Session using an incoming RFCOMM channel.
- [init!(sdpServiceRecord: IOBluetoothSDPServiceRecord!)](iobluetoothobexsession/init(sdpservicerecord:).md)
  Initializes a Bluetooth-based OBEX Session using an SDP service record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothobexsession/init(device:channelid:))*