# IOBluetoothSDPServiceAttribute

**Framework**: IOBluetooth  
**Kind**: class

IOBluetoothSDPServiceAttribute represents a single SDP service attribute.

**Availability**:
- macOS ?+

## Declaration

```swift
class IOBluetoothSDPServiceAttribute
```

#### Overview

A service attribute contains two components: an attribute ID and a data element.

## Topics

### Initializers
- [init!(id: BluetoothSDPServiceAttributeID, attributeElement: IOBluetoothSDPDataElement!)](iobluetoothsdpserviceattribute/init(id:attributeelement:).md)
  Initializes a new service attribute with the given ID and data element.
- [init!(id: BluetoothSDPServiceAttributeID, attributeElementValue: NSObject!)](iobluetoothsdpserviceattribute/init(id:attributeelementvalue:).md)
  Initializes a new service attribute with the given ID and element value.
### Instance Methods
- [func getDataElement() -> IOBluetoothSDPDataElement!](iobluetoothsdpserviceattribute/getdataelement.md)
  Returns the data element for the target service attribute.
- [func getID() -> BluetoothSDPServiceAttributeID](iobluetoothsdpserviceattribute/getid.md)
  Returns the attribute ID for the target service attribute.
- [func getIDDataElement() -> IOBluetoothSDPDataElement!](iobluetoothsdpserviceattribute/getiddataelement.md)
  Returns the data element representing the attribute ID for the target service attribute.
### Type Methods
- [class func withID(BluetoothSDPServiceAttributeID, attributeElement: IOBluetoothSDPDataElement!) -> Self!](iobluetoothsdpserviceattribute/withid(_:attributeelement:).md)
  Creates a new service attribute with the given ID and data element.
- [class func withID(BluetoothSDPServiceAttributeID, attributeElementValue: NSObject!) -> Self!](iobluetoothsdpserviceattribute/withid(_:attributeelementvalue:).md)
  Creates a new service attribute with the given ID and element value.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpserviceattribute)*