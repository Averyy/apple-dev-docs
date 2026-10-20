# IOBluetoothSDPServiceRecord

**Framework**: IOBluetooth  
**Kind**: class  
**Role**: Class

An instance of this class represents a single SDP service record.

**Availability**:
- macOS

## Declaration

```swift
class IOBluetoothSDPServiceRecord
```

```objc
@interface IOBluetoothSDPServiceRecord : NSObject
```

#### Overview

As a service record, an instance of this class has an NSDictionary of service attributes. It also has a link to the IOBluetoothDevice that the service belongs to. The service dictionary is keyed off of the attribute ID of each attribute represented as an NSNumber.

## Topics

### Initializers
- [init!(serviceDictionary: [AnyHashable : Any]!, device: IOBluetoothDevice!)](./iobluetoothsdpservicerecord/init%28servicedictionary,device%29.md)
  Returns an initialized IOBluetoothSDPServiceRecord * with the attributes specified in the provided service dictionary. Provide a pointer to an IOBlueotothDevice if you wish to associate the record to a specific IOBluetoothDevice.
- [init?(coder: NSCoder)](./iobluetoothsdpservicerecord/init%28coder%29.md)
### Instance Properties
- [var attributes: [AnyHashable : Any]!](./iobluetoothsdpservicerecord/attributes.md)
  Returns an NSDictionary containing the attributes for the service.
- [var device: IOBluetoothDevice!](./iobluetoothsdpservicerecord/device.md)
  Returns the IOBluetoothDevice that the target service belongs to.
- [var sortedAttributes: [Any]!](./iobluetoothsdpservicerecord/sortedattributes-swift.property.md)
  Returns a sorted array of SDP attributes
### Instance Methods
- [func getAttributeDataElement(BluetoothSDPServiceAttributeID) -> IOBluetoothSDPDataElement!](./iobluetoothsdpservicerecord/getattributedataelement%28_%29.md)
  Returns the data element for the given attribute ID in the target service.
- [func getHandle(UnsafeMutablePointer<BluetoothSDPServiceRecordHandle>!) -> IOReturn](./iobluetoothsdpservicerecord/gethandle%28_%29.md)
  Allows the discovery of the service record handle assigned to the service.
- [func getL2CAPPSM(UnsafeMutablePointer<BluetoothL2CAPPSM>!) -> IOReturn](./iobluetoothsdpservicerecord/getl2cappsm%28_%29.md)
  Allows the discovery of the L2CAP PSM assigned to the service.
- [func getRFCOMMChannelID(UnsafeMutablePointer<BluetoothRFCOMMChannelID>!) -> IOReturn](./iobluetoothsdpservicerecord/getrfcommchannelid%28_%29.md)
  Allows the discovery of the RFCOMM channel ID assigned to the service.
- [func getRef() -> Unmanaged<IOBluetoothSDPServiceRecordRef>!](./iobluetoothsdpservicerecord/getref%28%29.md)
  Returns an IOBluetoothSDPServiceRecordRef representation of the target IOBluetoothSDPServiceRecord object.
- [func getServiceName() -> String!](./iobluetoothsdpservicerecord/getservicename%28%29.md)
  Returns the name of the service.
- [func handsFreeSupportedFeatures() -> UInt16](./iobluetoothsdpservicerecord/handsfreesupportedfeatures%28%29.md)
- [func hasService(from: [Any]!) -> Bool](./iobluetoothsdpservicerecord/hasservice%28from%29.md)
  Returns TRUE if any one of the UUIDs in the given array is found in the target service.
- [func matchesSearch([Any]!) -> Bool](./iobluetoothsdpservicerecord/matchessearch%28_%29.md)
  Returns TRUE any of the UUID arrays in the search array match the target service.
- [func matchesUUID16(BluetoothSDPUUID16) -> Bool](./iobluetoothsdpservicerecord/matchesuuid16%28_%29.md)
  Returns TRUE the UUID16 is found in the target service.
- [func matchesUUIDArray([Any]!) -> Bool](./iobluetoothsdpservicerecord/matchesuuidarray%28_%29.md)
  Returns TRUE if ALL of the UUIDs in the given array is found in the target service.
- [func remove() -> IOReturn](./iobluetoothsdpservicerecord/remove%28%29.md)
  Removes the service from the local SDP server.
### Type Methods
- [class func publishedServiceRecord(with: [AnyHashable : Any]!) -> Self!](./iobluetoothsdpservicerecord/publishedservicerecord%28with%29.md)
  Adds a service to the local SDP server.
- [class func withSDPServiceRecordRef(IOBluetoothSDPServiceRecordRef!) -> Self!](./iobluetoothsdpservicerecord/withsdpservicerecordref%28_%29.md)
  Method call to convert an IOBluetoothSDPServiceRecordRef into an IOBluetoothSDPServiceRecord *.
- [class func withServiceDictionary([AnyHashable : Any]!, device: IOBluetoothDevice!) -> Self!](./iobluetoothsdpservicerecord/withservicedictionary%28_,device%29.md)
  Returns an IOBluetoothSDPServiceRecord * with the attributes specified in the provided service dictionary. Provide a pointer to an IOBlueotothDevice if you wish to associate the record to a specific IOBluetoothDevice.

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

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpservicerecord)*