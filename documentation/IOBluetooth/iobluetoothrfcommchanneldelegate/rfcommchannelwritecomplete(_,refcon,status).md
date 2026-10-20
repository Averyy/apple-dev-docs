# rfcommChannelWriteComplete(_:refcon:status:)

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS

## Declaration

```swift
optional func rfcommChannelWriteComplete(_ rfcommChannel: IOBluetoothRFCOMMChannel!, refcon: UnsafeMutableRawPointer!, status error: IOReturn)
```

```objc
- (void) rfcommChannelWriteComplete:(IOBluetoothRFCOMMChannel *) rfcommChannel refcon:(void *) refcon status:(IOReturn) error;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothrfcommchanneldelegate/rfcommchannelwritecomplete(_:refcon:status:))*