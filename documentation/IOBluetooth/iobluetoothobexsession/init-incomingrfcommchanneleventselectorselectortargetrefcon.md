# init(incomingRFCOMMChannel:eventSelector:selectorTarget:refCon:)

**Framework**: IOBluetooth  
**Kind**: init

Initializes a Bluetooth-based OBEX Session using an incoming RFCOMM channel.

**Availability**:
- macOS ?+

## Declaration

```swift
init!(incomingRFCOMMChannel inChannel: IOBluetoothRFCOMMChannel!, eventSelector inEventSelector: Selector!, selectorTarget inEventSelectorTarget: Any!, refCon inUserRefCon: UnsafeMutableRawPointer!)
```

## Parameters

- `inChannel`: RFCOMM channel ID of the desired channel to be used.
- `inEventSelector`: The selector to be called when an event is received.
- `inEventSelectorTarget`: The target object that get the selector message.
- `inUserRefCon`: Caller reference constant, pass whatever you want, it will be returned to you in the selector.

## See Also

- [init!(device: IOBluetoothDevice!, channelID: BluetoothRFCOMMChannelID)](iobluetoothobexsession/init(device:channelid:).md)
  Initializes a Bluetooth-based OBEX Session using a Bluetooth device.
- [init!(sdpServiceRecord: IOBluetoothSDPServiceRecord!)](iobluetoothobexsession/init(sdpservicerecord:).md)
  Initializes a Bluetooth-based OBEX Session using an SDP service record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothobexsession/init(incomingrfcommchannel:eventselector:selectortarget:refcon:))*