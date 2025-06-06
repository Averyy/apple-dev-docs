# IOBluetoothHostController

**Framework**: IOBluetooth  
**Kind**: class

This class is a representation of a Bluetooth Host Controller Interface that is present on the local computer (either plugged in externally or available internally).

**Availability**:
- macOS ?+

## Declaration

```swift
class IOBluetoothHostController
```

#### Overview

This object can be used to ask a Bluetooth HCI for certain pieces of information, and be used to make it perform certain functions.

## Topics

### Instance Properties
- [var delegate: AnyObject!](iobluetoothhostcontroller/delegate.md)
- [var powerState: BluetoothHCIPowerState](iobluetoothhostcontroller/powerstate.md)
  Gets the controller power state
### Instance Methods
- [func addressAsString() -> String!](iobluetoothhostcontroller/addressasstring.md)
  Convience routine to get the HCI controller’s Bluetooth address as an NSString object.
- [func classOfDevice() -> BluetoothClassOfDevice](iobluetoothhostcontroller/classofdevice.md)
  Gets the current class of device value.
- [func nameAsString() -> String!](iobluetoothhostcontroller/nameasstring.md)
  Gets the “friendly” name of HCI controller.
- [func setClassOfDevice(BluetoothClassOfDevice, forTimeInterval: TimeInterval) -> IOReturn](iobluetoothhostcontroller/setclassofdevice(_:fortimeinterval:).md)
  Sets the current class of device value, for the specified amount of time. Note that the time interval  be set and valid. The range of acceptable values is 30-120 seconds. Anything above or below will be rounded up, or down, as appropriate.
### Type Methods
- [class func `default`() -> Self!](iobluetoothhostcontroller/default.md)
  Gets the default HCI controller object.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
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
- [class IOBluetoothHandsFreeAudioGateway](iobluetoothhandsfreeaudiogateway.md)
  An object that sends data to a connected Bluetooth hands-free phone or headset and processes commands from it.
- [class IOBluetoothHandsFreeDevice](iobluetoothhandsfreedevice.md)
  An object you use to manage phone calls on a connected Bluetooth hands-free phone or headset.
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

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhostcontroller)*