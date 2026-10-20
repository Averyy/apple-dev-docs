# init(sdpServiceRecord:)

**Framework**: IOBluetooth  
**Kind**: init  
**Role**: Initializer

Initializes a Bluetooth-based OBEX Session using an SDP service record.

**Availability**:
- macOS

## Declaration

```swift
init!(sdpServiceRecord inSDPServiceRecord: IOBluetoothSDPServiceRecord!)
```

```objc
- (instancetype) initWithSDPServiceRecord:(IOBluetoothSDPServiceRecord *) inSDPServiceRecord;
```

## Parameters

- `inSDPServiceRecord`: 

## See Also

### Initializers
- [init!(device: IOBluetoothDevice!, channelID: BluetoothRFCOMMChannelID)](./init%28device,channelid%29.md)
  Initializes a Bluetooth-based OBEX Session using a Bluetooth device.
- [init!(incomingRFCOMMChannel: IOBluetoothRFCOMMChannel!, eventSelector: Selector!, selectorTarget: Any!, refCon: UnsafeMutableRawPointer!)](./init%28incomingrfcommchannel,eventselector,selectortarget,refcon%29.md)
  Initializes a Bluetooth-based OBEX Session using an incoming RFCOMM channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothobexsession/init(sdpservicerecord:)-h1xg)*