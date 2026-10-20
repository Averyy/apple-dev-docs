# IOBluetoothL2CAPChannelDelegate

**Framework**: IOBluetooth  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- macOS

## Declaration

```swift
protocol IOBluetoothL2CAPChannelDelegate
```

```objc
@protocol IOBluetoothL2CAPChannelDelegate
```

## Topics

### Instance Methods
- [func l2capChannelClosed(IOBluetoothL2CAPChannel!)](./iobluetoothl2capchanneldelegate/l2capchannelclosed%28_%29.md)
- [func l2capChannelData(IOBluetoothL2CAPChannel!, data: UnsafeMutableRawPointer!, length: Int)](./iobluetoothl2capchanneldelegate/l2capchanneldata%28_,data,length%29.md)
- [func l2capChannelOpenComplete(IOBluetoothL2CAPChannel!, status: IOReturn)](./iobluetoothl2capchanneldelegate/l2capchannelopencomplete%28_,status%29.md)
- [func l2capChannelQueueSpaceAvailable(IOBluetoothL2CAPChannel!)](./iobluetoothl2capchanneldelegate/l2capchannelqueuespaceavailable%28_%29.md)
- [func l2capChannelReconfigured(IOBluetoothL2CAPChannel!)](./iobluetoothl2capchanneldelegate/l2capchannelreconfigured%28_%29.md)
- [func l2capChannelWriteComplete(IOBluetoothL2CAPChannel!, refcon: UnsafeMutableRawPointer!, status: IOReturn)](./iobluetoothl2capchanneldelegate/l2capchannelwritecomplete%28_,refcon,status%29.md)

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
- [protocol IOBluetoothRFCOMMChannelDelegate](./iobluetoothrfcommchanneldelegate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchanneldelegate)*