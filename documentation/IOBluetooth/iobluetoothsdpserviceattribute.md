# IOBluetoothSDPServiceAttribute

**Framework**: IOBluetooth  
**Kind**: class  
**Role**: Class

IOBluetoothSDPServiceAttribute represents a single SDP service attribute.

**Availability**:
- macOS

## Declaration

```swift
class IOBluetoothSDPServiceAttribute
```

```objc
@interface IOBluetoothSDPServiceAttribute : NSObject
```

## Overview

A service attribute contains two components: an attribute ID and a data element.

## Topics

### Initializers
- [init!(id: BluetoothSDPServiceAttributeID, attributeElement: IOBluetoothSDPDataElement!)](./iobluetoothsdpserviceattribute/init%28id,attributeelement%29-7oebi.md)
  Initializes a new service attribute with the given ID and data element.
- [init!(id: BluetoothSDPServiceAttributeID, attributeElementValue: NSObject!)](./iobluetoothsdpserviceattribute/init%28id,attributeelementvalue%29-84b3r.md)
  Initializes a new service attribute with the given ID and element value.
- [init!(ID: BluetoothSDPServiceAttributeID, attributeElement: IOBluetoothSDPDataElement!)](./iobluetoothsdpserviceattribute/init%28id,attributeelement%29-3g9jw.md)
- [init!(ID: BluetoothSDPServiceAttributeID, attributeElementValue: NSObject!)](./iobluetoothsdpserviceattribute/init%28id,attributeelementvalue%29-1o9lv.md)
- [init?(coder: NSCoder)](./iobluetoothsdpserviceattribute/init%28coder%29.md)
### Instance Methods
- [func getDataElement() -> IOBluetoothSDPDataElement!](./iobluetoothsdpserviceattribute/getdataelement%28%29.md)
  Returns the data element for the target service attribute.
- [func getID() -> BluetoothSDPServiceAttributeID](./iobluetoothsdpserviceattribute/getid%28%29.md)
  Returns the attribute ID for the target service attribute.
- [func getIDDataElement() -> IOBluetoothSDPDataElement!](./iobluetoothsdpserviceattribute/getiddataelement%28%29.md)
  Returns the data element representing the attribute ID for the target service attribute.
### Type Methods
- [class func withID(BluetoothSDPServiceAttributeID, attributeElement: IOBluetoothSDPDataElement!) -> Self!](./iobluetoothsdpserviceattribute/withid%28_,attributeelement%29.md)
  Creates a new service attribute with the given ID and data element.
- [class func withID(BluetoothSDPServiceAttributeID, attributeElementValue: NSObject!) -> Self!](./iobluetoothsdpserviceattribute/withid%28_,attributeelementvalue%29.md)
  Creates a new service attribute with the given ID and element value.
### Instance Variables
- [mAttributeDataElement](./iobluetoothsdpserviceattribute/mattributedataelement.md)
- [mAttributeID](./iobluetoothsdpserviceattribute/mattributeid.md)
- [mAttributeIDDataElement](./iobluetoothsdpserviceattribute/mattributeiddataelement.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Classes
- [class IOBluetoothDevice](./iobluetoothdevice.md)
  An instance of IOBluetoothDevice represents a single remote Bluetooth device.
- [class IOBluetoothDeviceInquiry](./iobluetoothdeviceinquiry.md)
  Object representing a device inquiry that finds Bluetooth devices in-range of the computer, and (optionally) retrieves name information for them.
- [class IOBluetoothDevicePair](./iobluetoothdevicepair.md)
  An instance of IOBluetoothDevicePair represents a pairing attempt to a remote Bluetooth device.
- [class IOBluetoothDeviceRef](./iobluetoothdeviceref.md)
  An object that represents a Bluetooth I/O device.
- [class IOBluetoothHandsFree](./iobluetoothhandsfree.md)
  Hands free profile class.
- [class IOBluetoothHandsFreeAudioGateway](./iobluetoothhandsfreeaudiogateway.md)
  An object that sends data to a connected Bluetooth hands-free phone or headset and processes commands from it.
- [class IOBluetoothHandsFreeDevice](./iobluetoothhandsfreedevice.md)
  An object you use to manage phone calls on a connected Bluetooth hands-free phone or headset.
- [class IOBluetoothHostController](./iobluetoothhostcontroller.md)
  This class is a representation of a Bluetooth Host Controller Interface that is present on the local computer (either plugged in externally or available internally).
- [class IOBluetoothL2CAPChannel](./iobluetoothl2capchannel.md)
  An instance of IOBluetoothL2CAPChannel represents a single open L2CAP channel.
- [class IOBluetoothL2CAPChannelRef](./iobluetoothl2capchannelref.md)
- [class IOBluetoothOBEXSession](./iobluetoothobexsession.md)
  An OBEX Session with a Bluetooth RFCOMM channel as the transport.
- [class IOBluetoothObject](./iobluetoothobject.md)
- [class IOBluetoothObjectRef](./iobluetoothobjectref.md)
- [class IOBluetoothRFCOMMChannel](./iobluetoothrfcommchannel.md)
  An instance of this class represents an RFCOMM channel as defined by the Bluetooth SDP spec..
- [class IOBluetoothRFCOMMChannelRef](./iobluetoothrfcommchannelref.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpserviceattribute)*