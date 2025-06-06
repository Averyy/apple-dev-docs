# IOBluetoothHandsFreeDeviceDelegate

**Framework**: IOBluetooth  
**Kind**: protocol

A set of optional methods for receiving status change updates and information about a connected Bluetooth hands-free phone or headset.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol IOBluetoothHandsFreeDeviceDelegate : IOBluetoothHandsFreeDelegate
```

## Topics

### Receiving Status Indicator Changes
- [func handsFree(IOBluetoothHandsFreeDevice!, callSetupMode: NSNumber!)](iobluetoothhandsfreedevicedelegate/handsfree(_:callsetupmode:).md)
  Tells the delegate the call setup indicator of the connected Bluetooth hands-free phone or headset has changed.
- [func handsFree(IOBluetoothHandsFreeDevice!, isCallActive: NSNumber!)](iobluetoothhandsfreedevicedelegate/handsfree(_:iscallactive:).md)
  Tells the delegate the active call indicator of the connected Bluetooth hands-free phone or headset has changed.
- [func handsFree(IOBluetoothHandsFreeDevice!, isServiceAvailable: NSNumber!)](iobluetoothhandsfreedevicedelegate/handsfree(_:isserviceavailable:).md)
  Tells the delegate the service level indicator of the connected Bluetooth hands-free phone or headset has changed.
- [func handsFree(IOBluetoothHandsFreeDevice!, signalStrength: NSNumber!)](iobluetoothhandsfreedevicedelegate/handsfree(_:signalstrength:).md)
  Tells the delegate the call setup signal strength indicator of the connected Bluetooth hands-free phone or headset has changed.
- [func handsFree(IOBluetoothHandsFreeDevice!, callHoldState: NSNumber!)](iobluetoothhandsfreedevicedelegate/handsfree(_:callholdstate:).md)
  Tells the delegate the call held indicator of the connected Bluetooth hands-free phone or headset has changed.
- [func handsFree(IOBluetoothHandsFreeDevice!, isRoaming: NSNumber!)](iobluetoothhandsfreedevicedelegate/handsfree(_:isroaming:).md)
  Tells the delegate the roaming indicator of the connected Bluetooth hands-free phone or headset has changed.
- [func handsFree(IOBluetoothHandsFreeDevice!, batteryCharge: NSNumber!)](iobluetoothhandsfreedevicedelegate/handsfree(_:batterycharge:).md)
  Tells the delegate the battery level indicator of the connected Bluetooth hands-free phone or headset has changed.
### Receiving Call Status
- [func handsFree(IOBluetoothHandsFreeDevice!, incomingCallFrom: String!)](iobluetoothhandsfreedevicedelegate/handsfree(_:incomingcallfrom:).md)
  Tells the delegate there’s an incoming call on the connected Bluetooth hands-free phone or headset.
- [func handsFree(IOBluetoothHandsFreeDevice!, currentCall: [AnyHashable : Any]!)](iobluetoothhandsfreedevicedelegate/handsfree(_:currentcall:).md)
  Sends the delegate information about the current call.
- [Current Call Information Constants](current-call-information-constants.md)
  Get information about a phone call on a hands-free Bluetooth device.
### Receiving SMS Information
- [func handsFree(IOBluetoothHandsFreeDevice!, incomingSMS: [AnyHashable : Any]!)](iobluetoothhandsfreedevicedelegate/handsfree(_:incomingsms:).md)
  Tells the delegate there’s an incoming text message.
- [SMS Dictionary Key Constants](sms-dictionary-key-constants.md)
  Read the parts of an SMS message.
### Receiving Other Information
- [func handsFree(IOBluetoothHandsFreeDevice!, subscriberNumber: String!)](iobluetoothhandsfreedevicedelegate/handsfree(_:subscribernumber:).md)
  Tells the delegate the subscriber number of a call.
- [func handsFree(IOBluetoothHandsFreeDevice!, ringAttempt: NSNumber!)](iobluetoothhandsfreedevicedelegate/handsfree(_:ringattempt:).md)
  Tells the delegate the phone is ringing.
- [func handsFree(IOBluetoothHandsFreeDevice!, unhandledResultCode: String!)](iobluetoothhandsfreedevicedelegate/handsfree(_:unhandledresultcode:).md)
  Tells the delegate the phone sent an unknown code.

## Relationships

### Inherits From
- [IOBluetoothHandsFreeDelegate](iobluetoothhandsfreedelegate.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol IOBluetoothDeviceAsyncCallbacks](iobluetoothdeviceasynccallbacks.md)
- [protocol IOBluetoothDeviceInquiryDelegate](iobluetoothdeviceinquirydelegate.md)
  This category on NSObject describes the delegate methods for the IOBluetoothDeviceInquiry object. All methods are optional, but it is highly recommended you implement them all. Do NOT invoke remote name requests on found IOBluetoothDevice objects unless the inquiry object has been stopped. Doing so may deadlock your process.
- [protocol IOBluetoothDevicePairDelegate](iobluetoothdevicepairdelegate.md)
- [protocol IOBluetoothHandsFreeAudioGatewayDelegate](iobluetoothhandsfreeaudiogatewaydelegate.md)
  A set of optional methods for receiving information about status changes for a connected Bluetooth hands-free phone or headset.
- [protocol IOBluetoothHandsFreeDelegate](iobluetoothhandsfreedelegate.md)
- [protocol IOBluetoothL2CAPChannelDelegate](iobluetoothl2capchanneldelegate.md)
- [protocol IOBluetoothRFCOMMChannelDelegate](iobluetoothrfcommchanneldelegate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate)*