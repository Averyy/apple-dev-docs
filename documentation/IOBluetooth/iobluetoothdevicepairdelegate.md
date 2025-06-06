# IOBluetoothDevicePairDelegate

**Framework**: IOBluetooth  
**Kind**: protocol

**Availability**:
- macOS ?+

## Declaration

```swift
protocol IOBluetoothDevicePairDelegate : NSObjectProtocol
```

## Topics

### Instance Methods
- [func devicePairingConnected(Any!)](iobluetoothdevicepairdelegate/devicepairingconnected(_:).md)
- [func devicePairingConnecting(Any!)](iobluetoothdevicepairdelegate/devicepairingconnecting(_:).md)
- [func devicePairingFinished(Any!, error: IOReturn)](iobluetoothdevicepairdelegate/devicepairingfinished(_:error:).md)
- [func devicePairingPINCodeRequest(Any!)](iobluetoothdevicepairdelegate/devicepairingpincoderequest(_:).md)
- [func devicePairingStarted(Any!)](iobluetoothdevicepairdelegate/devicepairingstarted(_:).md)
- [func devicePairingUserConfirmationRequest(Any!, numericValue: BluetoothNumericValue)](iobluetoothdevicepairdelegate/devicepairinguserconfirmationrequest(_:numericvalue:).md)
- [func devicePairingUserPasskeyNotification(Any!, passkey: BluetoothPasskey)](iobluetoothdevicepairdelegate/devicepairinguserpasskeynotification(_:passkey:).md)
- [func deviceSimplePairingComplete(Any!, status: BluetoothHCIEventStatus)](iobluetoothdevicepairdelegate/devicesimplepairingcomplete(_:status:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol IOBluetoothDeviceAsyncCallbacks](iobluetoothdeviceasynccallbacks.md)
- [protocol IOBluetoothDeviceInquiryDelegate](iobluetoothdeviceinquirydelegate.md)
  This category on NSObject describes the delegate methods for the IOBluetoothDeviceInquiry object. All methods are optional, but it is highly recommended you implement them all. Do NOT invoke remote name requests on found IOBluetoothDevice objects unless the inquiry object has been stopped. Doing so may deadlock your process.
- [protocol IOBluetoothHandsFreeAudioGatewayDelegate](iobluetoothhandsfreeaudiogatewaydelegate.md)
  A set of optional methods for receiving information about status changes for a connected Bluetooth hands-free phone or headset.
- [protocol IOBluetoothHandsFreeDelegate](iobluetoothhandsfreedelegate.md)
- [protocol IOBluetoothHandsFreeDeviceDelegate](iobluetoothhandsfreedevicedelegate.md)
  A set of optional methods for receiving status change updates and information about a connected Bluetooth hands-free phone or headset.
- [protocol IOBluetoothL2CAPChannelDelegate](iobluetoothl2capchanneldelegate.md)
- [protocol IOBluetoothRFCOMMChannelDelegate](iobluetoothrfcommchanneldelegate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevicepairdelegate)*