# IOBluetoothDeviceAsyncCallbacks

**Framework**: IOBluetooth  
**Kind**: protocol

**Availability**:
- macOS ?+

## Declaration

```swift
protocol IOBluetoothDeviceAsyncCallbacks
```

## Topics

### Instance Methods
- [func connectionComplete(IOBluetoothDevice!, status: IOReturn)](iobluetoothdeviceasynccallbacks/connectioncomplete(_:status:).md)
- [func remoteNameRequestComplete(IOBluetoothDevice!, status: IOReturn)](iobluetoothdeviceasynccallbacks/remotenamerequestcomplete(_:status:).md)
- [func sdpQueryComplete(IOBluetoothDevice!, status: IOReturn)](iobluetoothdeviceasynccallbacks/sdpquerycomplete(_:status:).md)

## See Also

- [protocol IOBluetoothDeviceInquiryDelegate](iobluetoothdeviceinquirydelegate.md)
  This category on NSObject describes the delegate methods for the IOBluetoothDeviceInquiry object. All methods are optional, but it is highly recommended you implement them all. Do NOT invoke remote name requests on found IOBluetoothDevice objects unless the inquiry object has been stopped. Doing so may deadlock your process.
- [protocol IOBluetoothDevicePairDelegate](iobluetoothdevicepairdelegate.md)
- [protocol IOBluetoothHandsFreeAudioGatewayDelegate](iobluetoothhandsfreeaudiogatewaydelegate.md)
  A set of optional methods for receiving information about status changes for a connected Bluetooth hands-free phone or headset.
- [protocol IOBluetoothHandsFreeDelegate](iobluetoothhandsfreedelegate.md)
- [protocol IOBluetoothHandsFreeDeviceDelegate](iobluetoothhandsfreedevicedelegate.md)
  A set of optional methods for receiving status change updates and information about a connected Bluetooth hands-free phone or headset.
- [protocol IOBluetoothL2CAPChannelDelegate](iobluetoothl2capchanneldelegate.md)
- [protocol IOBluetoothRFCOMMChannelDelegate](iobluetoothrfcommchanneldelegate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdeviceasynccallbacks)*