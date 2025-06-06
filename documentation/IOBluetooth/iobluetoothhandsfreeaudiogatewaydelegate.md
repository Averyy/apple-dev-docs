# IOBluetoothHandsFreeAudioGatewayDelegate

**Framework**: IOBluetooth  
**Kind**: protocol

A set of optional methods for receiving information about status changes for a connected Bluetooth hands-free phone or headset.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol IOBluetoothHandsFreeAudioGatewayDelegate
```

## Topics

### Receiving Status Change Information
- [func handsFree(IOBluetoothHandsFreeAudioGateway!, hangup: NSNumber!)](iobluetoothhandsfreeaudiogatewaydelegate/handsfree(_:hangup:).md)
  Tells the delegate the connected Bluetooth hands-free phone or headset is sending a hang-up signal.
- [func handsFree(IOBluetoothHandsFreeAudioGateway!, redial: NSNumber!)](iobluetoothhandsfreeaudiogatewaydelegate/handsfree(_:redial:).md)
  Tells the delegate the connected Bluetooth hands-free phone or headset is redialing the last phone number.

## See Also

- [protocol IOBluetoothDeviceAsyncCallbacks](iobluetoothdeviceasynccallbacks.md)
- [protocol IOBluetoothDeviceInquiryDelegate](iobluetoothdeviceinquirydelegate.md)
  This category on NSObject describes the delegate methods for the IOBluetoothDeviceInquiry object. All methods are optional, but it is highly recommended you implement them all. Do NOT invoke remote name requests on found IOBluetoothDevice objects unless the inquiry object has been stopped. Doing so may deadlock your process.
- [protocol IOBluetoothDevicePairDelegate](iobluetoothdevicepairdelegate.md)
- [protocol IOBluetoothHandsFreeDelegate](iobluetoothhandsfreedelegate.md)
- [protocol IOBluetoothHandsFreeDeviceDelegate](iobluetoothhandsfreedevicedelegate.md)
  A set of optional methods for receiving status change updates and information about a connected Bluetooth hands-free phone or headset.
- [protocol IOBluetoothL2CAPChannelDelegate](iobluetoothl2capchanneldelegate.md)
- [protocol IOBluetoothRFCOMMChannelDelegate](iobluetoothrfcommchanneldelegate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogatewaydelegate)*