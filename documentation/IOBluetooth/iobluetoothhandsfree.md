# IOBluetoothHandsFree

**Framework**: IOBluetooth  
**Kind**: class

Hands free profile class.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class IOBluetoothHandsFree
```

#### Overview

Superclass of IOBluetoothHandsFreeDevice and IOBluetoothHandsFreeAudioGateway classes. Contains the common code used to support the bluetoooth hands free profile.

## Topics

### Initializers
- [init!(device: IOBluetoothDevice!, delegate: (any IOBluetoothHandsFreeDelegate)!)](iobluetoothhandsfree/init(device:delegate:).md)
  Create a new IOBluetoothHandsFree object
### Instance Properties
- [var delegate: (any IOBluetoothHandsFreeDelegate)!](iobluetoothhandsfree/delegate.md)
  Return the delegate
- [var device: IOBluetoothDevice!](iobluetoothhandsfree/device.md)
  Return the IOBluetoothDevice.
- [var deviceCallHoldModes: UInt32](iobluetoothhandsfree/devicecallholdmodes.md)
  Return the device’s supported call hold modes.
- [var deviceSupportedFeatures: UInt32](iobluetoothhandsfree/devicesupportedfeatures.md)
  Return the device’s supported features.
- [var deviceSupportedSMSServices: UInt32](iobluetoothhandsfree/devicesupportedsmsservices.md)
  Return the device’s supported SMS services.
- [var inputVolume: Float](iobluetoothhandsfree/inputvolume.md)
  Return the input volume
- [var isConnected: Bool](iobluetoothhandsfree/isconnected.md)
- [var isInputMuted: Bool](iobluetoothhandsfree/isinputmuted.md)
  Return the input mute state.
- [var isOutputMuted: Bool](iobluetoothhandsfree/isoutputmuted.md)
  Return the output mute state.
- [var isSMSEnabled: Bool](iobluetoothhandsfree/issmsenabled.md)
  Return YES if the device has SMS enabled.
- [var outputVolume: Float](iobluetoothhandsfree/outputvolume.md)
  Return the output volume
- [var smsMode: IOBluetoothSMSMode](iobluetoothhandsfree/smsmode.md)
  Return the device’s SMS mode.
- [var supportedFeatures: UInt32](iobluetoothhandsfree/supportedfeatures.md)
  Set the supported features
### Instance Methods
- [func connect()](iobluetoothhandsfree/connect.md)
  Connect to the device
- [func connectSCO()](iobluetoothhandsfree/connectsco.md)
  Open a SCO connection with the device
- [func disconnect()](iobluetoothhandsfree/disconnect.md)
  Disconnect from the device
- [func disconnectSCO()](iobluetoothhandsfree/disconnectsco.md)
  Disconnect the SCO connection with the device
- [func indicator(String!) -> Int32](iobluetoothhandsfree/indicator(_:).md)
  Return an indicator’s value
- [func isSCOConnected() -> Bool](iobluetoothhandsfree/isscoconnected.md)
  Determine if there is a SCO connection to the device
- [func setIndicator(String!, value: Int32)](iobluetoothhandsfree/setindicator(_:value:).md)
  Set an indicator’s value

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [IOBluetoothHandsFreeAudioGateway](iobluetoothhandsfreeaudiogateway.md)
- [IOBluetoothHandsFreeDevice](iobluetoothhandsfreedevice.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class IOBluetoothDevice](iobluetoothdevice.md)
  An instance of IOBluetoothDevice represents a single remote Bluetooth device.
- [class IOBluetoothDeviceInquiry](iobluetoothdeviceinquiry.md)
  Object representing a device inquiry that finds Bluetooth devices in-range of the computer, and (optionally) retrieves name information for them.
- [class IOBluetoothDevicePair](iobluetoothdevicepair.md)
  An instance of IOBluetoothDevicePair represents a pairing attempt to a remote Bluetooth device.
- [class IOBluetoothDeviceRef](iobluetoothdeviceref.md)
  An object that represents a Bluetooth I/O device.
- [class IOBluetoothHandsFreeAudioGateway](iobluetoothhandsfreeaudiogateway.md)
  An object that sends data to a connected Bluetooth hands-free phone or headset and processes commands from it.
- [class IOBluetoothHandsFreeDevice](iobluetoothhandsfreedevice.md)
  An object you use to manage phone calls on a connected Bluetooth hands-free phone or headset.
- [class IOBluetoothHostController](iobluetoothhostcontroller.md)
  This class is a representation of a Bluetooth Host Controller Interface that is present on the local computer (either plugged in externally or available internally).
- [class IOBluetoothL2CAPChannel](iobluetoothl2capchannel.md)
  An instance of IOBluetoothL2CAPChannel represents a single open L2CAP channel.
- [class IOBluetoothL2CAPChannelRef](iobluetoothl2capchannelref.md)
- [class IOBluetoothOBEXSession](iobluetoothobexsession.md)
  An OBEX Session with a Bluetooth RFCOMM channel as the transport.
- [class IOBluetoothObject](iobluetoothobject.md)
- [class IOBluetoothObjectRef](iobluetoothobjectref.md)
- [class IOBluetoothRFCOMMChannel](iobluetoothrfcommchannel.md)
  An instance of this class represents an RFCOMM channel as defined by the Bluetooth SDP spec..
- [class IOBluetoothRFCOMMChannelRef](iobluetoothrfcommchannelref.md)
- [class IOBluetoothSDPDataElement](iobluetoothsdpdataelement.md)
  An instance of this class represents a single SDP data element as defined by the Bluetooth SDP spec.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfree)*