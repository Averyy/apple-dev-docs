# IOBluetoothDevicePairDelegate

**Framework**: IOBluetooth  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- macOS

## Declaration

```swift
protocol IOBluetoothDevicePairDelegate : NSObjectProtocol
```

```objc
@protocol IOBluetoothDevicePairDelegate <NSObject>
```

## Topics

### Instance Methods
- [func devicePairingConnected(Any!)](./iobluetoothdevicepairdelegate/devicepairingconnected%28_%29.md)
- [func devicePairingConnecting(Any!)](./iobluetoothdevicepairdelegate/devicepairingconnecting%28_%29.md)
- [func devicePairingFinished(Any!, error: IOReturn)](./iobluetoothdevicepairdelegate/devicepairingfinished%28_,error%29.md)
- [func devicePairingPINCodeRequest(Any!)](./iobluetoothdevicepairdelegate/devicepairingpincoderequest%28_%29.md)
- [func devicePairingStarted(Any!)](./iobluetoothdevicepairdelegate/devicepairingstarted%28_%29.md)
- [func devicePairingUserConfirmationRequest(Any!, numericValue: BluetoothNumericValue)](./iobluetoothdevicepairdelegate/devicepairinguserconfirmationrequest%28_,numericvalue%29.md)
- [func devicePairingUserPasskeyNotification(Any!, passkey: BluetoothPasskey)](./iobluetoothdevicepairdelegate/devicepairinguserpasskeynotification%28_,passkey%29.md)
- [func deviceSimplePairingComplete(Any!, status: BluetoothHCIEventStatus)](./iobluetoothdevicepairdelegate/devicesimplepairingcomplete%28_,status%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Protocols
- [protocol IOBluetoothDeviceAsyncCallbacks](./iobluetoothdeviceasynccallbacks.md)
- [protocol IOBluetoothDeviceInquiryDelegate](./iobluetoothdeviceinquirydelegate.md)
  This category on NSObject describes the delegate methods for the IOBluetoothDeviceInquiry object. All methods are optional, but it is highly recommended you implement them all. Do NOT invoke remote name requests on found IOBluetoothDevice objects unless the inquiry object has been stopped. Doing so may deadlock your process.
- [protocol IOBluetoothHandsFreeAudioGatewayDelegate](./iobluetoothhandsfreeaudiogatewaydelegate.md)
  A set of optional methods for receiving information about status changes for a connected Bluetooth hands-free phone or headset.
- [protocol IOBluetoothHandsFreeDelegate](./iobluetoothhandsfreedelegate.md)
- [protocol IOBluetoothHandsFreeDeviceDelegate](./iobluetoothhandsfreedevicedelegate.md)
  A set of optional methods for receiving status change updates and information about a connected Bluetooth hands-free phone or headset.
- [protocol IOBluetoothL2CAPChannelDelegate](./iobluetoothl2capchanneldelegate.md)
- [protocol IOBluetoothRFCOMMChannelDelegate](./iobluetoothrfcommchanneldelegate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevicepairdelegate)*