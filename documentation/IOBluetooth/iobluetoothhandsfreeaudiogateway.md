# IOBluetoothHandsFreeAudioGateway

**Framework**: IOBluetooth  
**Kind**: class

An object that sends data to a connected Bluetooth hands-free phone or headset and processes commands from it.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class IOBluetoothHandsFreeAudioGateway
```

#### Overview

This class represents the audio gateway portion of a Bluetooth audio profile.

## Topics

### Creating a Gateway
- [init!(device: IOBluetoothDevice!, delegate: Any!)](iobluetoothhandsfreeaudiogateway/init(device:delegate:).md)
  Creates an object that controls a connected Bluetooth hands-free phone or headset.
### Showing Status Indicators
- [func createIndicator(String!, min: Int32, max: Int32, currentValue: Int32)](iobluetoothhandsfreeaudiogateway/createindicator(_:min:max:currentvalue:).md)
  Sends a request to the Bluetooth device to show or update a status indicator.
- [Status Indicator Constants](status-indicator-constants.md)
  Send commands to modify the status indicators of a hands-free Bluetooth device.
### Sending and Receiving Commands
- [func sendResponse(String!)](iobluetoothhandsfreeaudiogateway/sendresponse(_:).md)
  Sends data followed by a success message to a connected Bluetooth hands-free phone or headset.
- [func sendResponse(String!, withOK: Bool)](iobluetoothhandsfreeaudiogateway/sendresponse(_:withok:).md)
  Sends data followed by an optional success message to a connected Bluetooth hands-free phone or headset.
- [func sendOKResponse()](iobluetoothhandsfreeaudiogateway/sendokresponse.md)
  Sends a success message to a connected Bluetooth hands-free phone or headset.
- [func process(atCommand: String!)](iobluetoothhandsfreeaudiogateway/process(atcommand:).md)
  Processes a command from a connected Bluetooth hands-free phone or headset.

## Relationships

### Inherits From
- [IOBluetoothHandsFree](iobluetoothhandsfree.md)
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
- [class IOBluetoothHandsFree](iobluetoothhandsfree.md)
  Hands free profile class.
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

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogateway)*