# IOBluetoothRFCOMMChannelDelegate

**Framework**: IOBluetooth  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- macOS

## Declaration

```swift
protocol IOBluetoothRFCOMMChannelDelegate
```

```objc
@protocol IOBluetoothRFCOMMChannelDelegate
```

## Topics

### Instance Methods
- [func rfcommChannelClosed(IOBluetoothRFCOMMChannel!)](./iobluetoothrfcommchanneldelegate/rfcommchannelclosed%28_%29.md)
- [func rfcommChannelControlSignalsChanged(IOBluetoothRFCOMMChannel!)](./iobluetoothrfcommchanneldelegate/rfcommchannelcontrolsignalschanged%28_%29.md)
- [func rfcommChannelData(IOBluetoothRFCOMMChannel!, data: UnsafeMutableRawPointer!, length: Int)](./iobluetoothrfcommchanneldelegate/rfcommchanneldata%28_,data,length%29.md)
- [func rfcommChannelFlowControlChanged(IOBluetoothRFCOMMChannel!)](./iobluetoothrfcommchanneldelegate/rfcommchannelflowcontrolchanged%28_%29.md)
- [func rfcommChannelOpenComplete(IOBluetoothRFCOMMChannel!, status: IOReturn)](./iobluetoothrfcommchanneldelegate/rfcommchannelopencomplete%28_,status%29.md)
- [func rfcommChannelQueueSpaceAvailable(IOBluetoothRFCOMMChannel!)](./iobluetoothrfcommchanneldelegate/rfcommchannelqueuespaceavailable%28_%29.md)
- [func rfcommChannelWriteComplete(IOBluetoothRFCOMMChannel!, refcon: UnsafeMutableRawPointer!, status: IOReturn)](./iobluetoothrfcommchanneldelegate/rfcommchannelwritecomplete%28_,refcon,status%29.md)
- [func rfcommChannelWriteComplete(IOBluetoothRFCOMMChannel!, refcon: UnsafeMutableRawPointer!, status: IOReturn, bytesWritten: Int)](./iobluetoothrfcommchanneldelegate/rfcommchannelwritecomplete%28_,refcon,status,byteswritten%29.md)

## Relationships

### Conforming Types
- [IOBluetoothOBEXSession](./iobluetoothobexsession.md)

## See Also

### Protocols
- [protocol IOBluetoothDeviceAsyncCallbacks](./iobluetoothdeviceasynccallbacks.md)
- [protocol IOBluetoothDeviceInquiryDelegate](./iobluetoothdeviceinquirydelegate.md)
  This category on NSObject describes the delegate methods for the IOBluetoothDeviceInquiry object. All methods are optional, but it is highly recommended you implement them all. Do NOT invoke remote name requests on found IOBluetoothDevice objects unless the inquiry object has been stopped. Doing so may deadlock your process.
- [protocol IOBluetoothDevicePairDelegate](./iobluetoothdevicepairdelegate.md)
- [protocol IOBluetoothHandsFreeAudioGatewayDelegate](./iobluetoothhandsfreeaudiogatewaydelegate.md)
  A set of optional methods for receiving information about status changes for a connected Bluetooth hands-free phone or headset.
- [protocol IOBluetoothHandsFreeDelegate](./iobluetoothhandsfreedelegate.md)
- [protocol IOBluetoothHandsFreeDeviceDelegate](./iobluetoothhandsfreedevicedelegate.md)
  A set of optional methods for receiving status change updates and information about a connected Bluetooth hands-free phone or headset.
- [protocol IOBluetoothL2CAPChannelDelegate](./iobluetoothl2capchanneldelegate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothrfcommchanneldelegate)*