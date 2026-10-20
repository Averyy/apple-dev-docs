# IOBluetoothHandsFreeDeviceDelegate

**Framework**: IOBluetooth  
**Kind**: protocol  
**Role**: Protocol

A set of optional methods for receiving status change updates and information about a connected Bluetooth hands-free phone or headset.

**Availability**:
- macOS

## Declaration

```swift
protocol IOBluetoothHandsFreeDeviceDelegate : IOBluetoothHandsFreeDelegate
```

```objc
@protocol IOBluetoothHandsFreeDeviceDelegate <IOBluetoothHandsFreeDelegate>
```

## Topics

### Receiving Status Indicator Changes
- [func handsFree(IOBluetoothHandsFreeDevice!, callSetupMode: NSNumber!)](./iobluetoothhandsfreedevicedelegate/handsfree%28_,callsetupmode%29.md)
  Tells the delegate the call setup indicator of the connected Bluetooth hands-free phone or headset has changed.
- [func handsFree(IOBluetoothHandsFreeDevice!, isCallActive: NSNumber!)](./iobluetoothhandsfreedevicedelegate/handsfree%28_,iscallactive%29.md)
  Tells the delegate the active call indicator of the connected Bluetooth hands-free phone or headset has changed.
- [func handsFree(IOBluetoothHandsFreeDevice!, isServiceAvailable: NSNumber!)](./iobluetoothhandsfreedevicedelegate/handsfree%28_,isserviceavailable%29.md)
  Tells the delegate the service level indicator of the connected Bluetooth hands-free phone or headset has changed.
- [func handsFree(IOBluetoothHandsFreeDevice!, signalStrength: NSNumber!)](./iobluetoothhandsfreedevicedelegate/handsfree%28_,signalstrength%29.md)
  Tells the delegate the call setup signal strength indicator of the connected Bluetooth hands-free phone or headset has changed.
- [func handsFree(IOBluetoothHandsFreeDevice!, callHoldState: NSNumber!)](./iobluetoothhandsfreedevicedelegate/handsfree%28_,callholdstate%29.md)
  Tells the delegate the call held indicator of the connected Bluetooth hands-free phone or headset has changed.
- [func handsFree(IOBluetoothHandsFreeDevice!, isRoaming: NSNumber!)](./iobluetoothhandsfreedevicedelegate/handsfree%28_,isroaming%29.md)
  Tells the delegate the roaming indicator of the connected Bluetooth hands-free phone or headset has changed.
- [func handsFree(IOBluetoothHandsFreeDevice!, batteryCharge: NSNumber!)](./iobluetoothhandsfreedevicedelegate/handsfree%28_,batterycharge%29.md)
  Tells the delegate the battery level indicator of the connected Bluetooth hands-free phone or headset has changed.
### Receiving Call Status
- [func handsFree(IOBluetoothHandsFreeDevice!, incomingCallFrom: String!)](./iobluetoothhandsfreedevicedelegate/handsfree%28_,incomingcallfrom%29.md)
  Tells the delegate there’s an incoming call on the connected Bluetooth hands-free phone or headset.
- [func handsFree(IOBluetoothHandsFreeDevice!, currentCall: [AnyHashable : Any]!)](./iobluetoothhandsfreedevicedelegate/handsfree%28_,currentcall%29.md)
  Sends the delegate information about the current call.
- [Current Call Information Constants](./current-call-information-constants.md)
  Get information about a phone call on a hands-free Bluetooth device.
### Receiving SMS Information
- [func handsFree(IOBluetoothHandsFreeDevice!, incomingSMS: [AnyHashable : Any]!)](./iobluetoothhandsfreedevicedelegate/handsfree%28_,incomingsms%29.md)
  Tells the delegate there’s an incoming text message.
- [SMS Dictionary Key Constants](./sms-dictionary-key-constants.md)
  Read the parts of an SMS message.
### Receiving Other Information
- [func handsFree(IOBluetoothHandsFreeDevice!, subscriberNumber: String!)](./iobluetoothhandsfreedevicedelegate/handsfree%28_,subscribernumber%29.md)
  Tells the delegate the subscriber number of a call.
- [func handsFree(IOBluetoothHandsFreeDevice!, ringAttempt: NSNumber!)](./iobluetoothhandsfreedevicedelegate/handsfree%28_,ringattempt%29.md)
  Tells the delegate the phone is ringing.
- [func handsFree(IOBluetoothHandsFreeDevice!, unhandledResultCode: String!)](./iobluetoothhandsfreedevicedelegate/handsfree%28_,unhandledresultcode%29.md)
  Tells the delegate the phone sent an unknown code.

## Relationships

### Inherits From
- [IOBluetoothHandsFreeDelegate](./iobluetoothhandsfreedelegate.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Protocols
- [protocol IOBluetoothDeviceAsyncCallbacks](./iobluetoothdeviceasynccallbacks.md)
- [protocol IOBluetoothDeviceInquiryDelegate](./iobluetoothdeviceinquirydelegate.md)
  This category on NSObject describes the delegate methods for the IOBluetoothDeviceInquiry object. All methods are optional, but it is highly recommended you implement them all. Do NOT invoke remote name requests on found IOBluetoothDevice objects unless the inquiry object has been stopped. Doing so may deadlock your process.
- [protocol IOBluetoothDevicePairDelegate](./iobluetoothdevicepairdelegate.md)
- [protocol IOBluetoothHandsFreeAudioGatewayDelegate](./iobluetoothhandsfreeaudiogatewaydelegate.md)
  A set of optional methods for receiving information about status changes for a connected Bluetooth hands-free phone or headset.
- [protocol IOBluetoothHandsFreeDelegate](./iobluetoothhandsfreedelegate.md)
- [protocol IOBluetoothL2CAPChannelDelegate](./iobluetoothl2capchanneldelegate.md)
- [protocol IOBluetoothRFCOMMChannelDelegate](./iobluetoothrfcommchanneldelegate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate)*