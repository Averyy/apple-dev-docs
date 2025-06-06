# init(sdpServiceRecord:)

**Framework**: IOBluetooth  
**Kind**: init

Initializes a Bluetooth-based OBEX Session using an SDP service record.

**Availability**:
- macOS ?+

## Declaration

```swift
init!(sdpServiceRecord inSDPServiceRecord: IOBluetoothSDPServiceRecord!)
```

## Parameters

- `inSDPServiceRecord`: 

## See Also

- [init!(device: IOBluetoothDevice!, channelID: BluetoothRFCOMMChannelID)](iobluetoothobexsession/init(device:channelid:).md)
  Initializes a Bluetooth-based OBEX Session using a Bluetooth device.
- [init!(incomingRFCOMMChannel: IOBluetoothRFCOMMChannel!, eventSelector: Selector!, selectorTarget: Any!, refCon: UnsafeMutableRawPointer!)](iobluetoothobexsession/init(incomingrfcommchannel:eventselector:selectortarget:refcon:).md)
  Initializes a Bluetooth-based OBEX Session using an incoming RFCOMM channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothobexsession/init(sdpservicerecord:))*