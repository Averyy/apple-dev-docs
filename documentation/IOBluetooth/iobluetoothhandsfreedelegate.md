# IOBluetoothHandsFreeDelegate

**Framework**: IOBluetooth  
**Kind**: protocol

**Availability**:
- macOS ?+

## Declaration

```swift
protocol IOBluetoothHandsFreeDelegate : NSObjectProtocol
```

## Topics

### Instance Methods
- [func handsFree(IOBluetoothHandsFree!, connected: NSNumber!)](iobluetoothhandsfreedelegate/handsfree(_:connected:).md)
- [func handsFree(IOBluetoothHandsFree!, disconnected: NSNumber!)](iobluetoothhandsfreedelegate/handsfree(_:disconnected:).md)
- [func handsFree(IOBluetoothHandsFree!, scoConnectionClosed: NSNumber!)](iobluetoothhandsfreedelegate/handsfree(_:scoconnectionclosed:).md)
- [func handsFree(IOBluetoothHandsFree!, scoConnectionOpened: NSNumber!)](iobluetoothhandsfreedelegate/handsfree(_:scoconnectionopened:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [IOBluetoothHandsFreeDeviceDelegate](iobluetoothhandsfreedevicedelegate.md)

## See Also

- [protocol IOBluetoothDeviceAsyncCallbacks](iobluetoothdeviceasynccallbacks.md)
- [protocol IOBluetoothDeviceInquiryDelegate](iobluetoothdeviceinquirydelegate.md)
  This category on NSObject describes the delegate methods for the IOBluetoothDeviceInquiry object. All methods are optional, but it is highly recommended you implement them all. Do NOT invoke remote name requests on found IOBluetoothDevice objects unless the inquiry object has been stopped. Doing so may deadlock your process.
- [protocol IOBluetoothDevicePairDelegate](iobluetoothdevicepairdelegate.md)
- [protocol IOBluetoothHandsFreeAudioGatewayDelegate](iobluetoothhandsfreeaudiogatewaydelegate.md)
  A set of optional methods for receiving information about status changes for a connected Bluetooth hands-free phone or headset.
- [protocol IOBluetoothHandsFreeDeviceDelegate](iobluetoothhandsfreedevicedelegate.md)
  A set of optional methods for receiving status change updates and information about a connected Bluetooth hands-free phone or headset.
- [protocol IOBluetoothL2CAPChannelDelegate](iobluetoothl2capchanneldelegate.md)
- [protocol IOBluetoothRFCOMMChannelDelegate](iobluetoothrfcommchanneldelegate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedelegate)*