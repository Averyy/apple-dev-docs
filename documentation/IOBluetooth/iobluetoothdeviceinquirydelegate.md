# IOBluetoothDeviceInquiryDelegate

**Framework**: IOBluetooth  
**Kind**: protocol

This category on NSObject describes the delegate methods for the IOBluetoothDeviceInquiry object. All methods are optional, but it is highly recommended you implement them all. Do NOT invoke remote name requests on found IOBluetoothDevice objects unless the inquiry object has been stopped. Doing so may deadlock your process.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol IOBluetoothDeviceInquiryDelegate : NSObjectProtocol
```

## Topics

### Instance Methods
- [func deviceInquiryComplete(IOBluetoothDeviceInquiry!, error: IOReturn, aborted: Bool)](iobluetoothdeviceinquirydelegate/deviceinquirycomplete(_:error:aborted:).md)
- [func deviceInquiryDeviceFound(IOBluetoothDeviceInquiry!, device: IOBluetoothDevice!)](iobluetoothdeviceinquirydelegate/deviceinquirydevicefound(_:device:).md)
- [func deviceInquiryDeviceNameUpdated(IOBluetoothDeviceInquiry!, device: IOBluetoothDevice!, devicesRemaining: UInt32)](iobluetoothdeviceinquirydelegate/deviceinquirydevicenameupdated(_:device:devicesremaining:).md)
- [func deviceInquiryStarted(IOBluetoothDeviceInquiry!)](iobluetoothdeviceinquirydelegate/deviceinquirystarted(_:).md)
- [func deviceInquiryUpdatingDeviceNamesStarted(IOBluetoothDeviceInquiry!, devicesRemaining: UInt32)](iobluetoothdeviceinquirydelegate/deviceinquiryupdatingdevicenamesstarted(_:devicesremaining:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol IOBluetoothDeviceAsyncCallbacks](iobluetoothdeviceasynccallbacks.md)
- [protocol IOBluetoothDevicePairDelegate](iobluetoothdevicepairdelegate.md)
- [protocol IOBluetoothHandsFreeAudioGatewayDelegate](iobluetoothhandsfreeaudiogatewaydelegate.md)
  A set of optional methods for receiving information about status changes for a connected Bluetooth hands-free phone or headset.
- [protocol IOBluetoothHandsFreeDelegate](iobluetoothhandsfreedelegate.md)
- [protocol IOBluetoothHandsFreeDeviceDelegate](iobluetoothhandsfreedevicedelegate.md)
  A set of optional methods for receiving status change updates and information about a connected Bluetooth hands-free phone or headset.
- [protocol IOBluetoothL2CAPChannelDelegate](iobluetoothl2capchanneldelegate.md)
- [protocol IOBluetoothRFCOMMChannelDelegate](iobluetoothrfcommchanneldelegate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdeviceinquirydelegate)*