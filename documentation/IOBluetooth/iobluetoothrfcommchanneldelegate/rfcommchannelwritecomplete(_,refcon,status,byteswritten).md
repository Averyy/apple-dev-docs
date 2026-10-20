# rfcommChannelWriteComplete(_:refcon:status:bytesWritten:)

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS

## Declaration

```swift
optional func rfcommChannelWriteComplete(_ rfcommChannel: IOBluetoothRFCOMMChannel!, refcon: UnsafeMutableRawPointer!, status error: IOReturn, bytesWritten length: Int)
```

```objc
- (void) rfcommChannelWriteComplete:(IOBluetoothRFCOMMChannel *) rfcommChannel refcon:(void *) refcon status:(IOReturn) error bytesWritten:(size_t) length;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothrfcommchanneldelegate/rfcommchannelwritecomplete(_:refcon:status:byteswritten:))*