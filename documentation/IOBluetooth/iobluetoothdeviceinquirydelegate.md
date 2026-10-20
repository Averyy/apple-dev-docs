# IOBluetoothDeviceInquiryDelegate

**Framework**: IOBluetooth  
**Kind**: protocol  
**Role**: Protocol

This category on NSObject describes the delegate methods for the IOBluetoothDeviceInquiry object. All methods are optional, but it is highly recommended you implement them all. Do NOT invoke remote name requests on found IOBluetoothDevice objects unless the inquiry object has been stopped. Doing so may deadlock your process.

**Availability**:
- macOS

## Declaration

```swift
protocol IOBluetoothDeviceInquiryDelegate : NSObjectProtocol
```

```objc
@protocol IOBluetoothDeviceInquiryDelegate <NSObject>
```

## Topics

### Instance Methods
- [func deviceInquiryComplete(IOBluetoothDeviceInquiry!, error: IOReturn, aborted: Bool)](./iobluetoothdeviceinquirydelegate/deviceinquirycomplete%28_,error,aborted%29.md)
- [func deviceInquiryDeviceFound(IOBluetoothDeviceInquiry!, device: IOBluetoothDevice!)](./iobluetoothdeviceinquirydelegate/deviceinquirydevicefound%28_,device%29.md)
- [func deviceInquiryDeviceNameUpdated(IOBluetoothDeviceInquiry!, device: IOBluetoothDevice!, devicesRemaining: UInt32)](./iobluetoothdeviceinquirydelegate/deviceinquirydevicenameupdated%28_,device,devicesremaining%29.md)
- [func deviceInquiryStarted(IOBluetoothDeviceInquiry!)](./iobluetoothdeviceinquirydelegate/deviceinquirystarted%28_%29.md)
- [func deviceInquiryUpdatingDeviceNamesStarted(IOBluetoothDeviceInquiry!, devicesRemaining: UInt32)](./iobluetoothdeviceinquirydelegate/deviceinquiryupdatingdevicenamesstarted%28_,devicesremaining%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Protocols
- [protocol IOBluetoothDeviceAsyncCallbacks](./iobluetoothdeviceasynccallbacks.md)
- [protocol IOBluetoothDevicePairDelegate](./iobluetoothdevicepairdelegate.md)
- [protocol IOBluetoothHandsFreeAudioGatewayDelegate](./iobluetoothhandsfreeaudiogatewaydelegate.md)
  A set of optional methods for receiving information about status changes for a connected Bluetooth hands-free phone or headset.
- [protocol IOBluetoothHandsFreeDelegate](./iobluetoothhandsfreedelegate.md)
- [protocol IOBluetoothHandsFreeDeviceDelegate](./iobluetoothhandsfreedevicedelegate.md)
  A set of optional methods for receiving status change updates and information about a connected Bluetooth hands-free phone or headset.
- [protocol IOBluetoothL2CAPChannelDelegate](./iobluetoothl2capchanneldelegate.md)
- [protocol IOBluetoothRFCOMMChannelDelegate](./iobluetoothrfcommchanneldelegate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdeviceinquirydelegate)*