# IOBluetoothSDPDataElement

**Framework**: IOBluetooth  
**Kind**: class

An instance of this class represents a single SDP data element as defined by the Bluetooth SDP spec.

**Availability**:
- macOS ?+

## Declaration

```swift
class IOBluetoothSDPDataElement
```

#### Overview

The data types described by the spec have been mapped onto the base Foundation classes NSNumber, NSArray, NSData as well as IOBluetoothSDPUUID. The number and boolean types (type descriptor 1, 2 and 5) are represented as NSNumber objects with the exception of 128-bit numbers which are represented as NSData objects in their raw format. The UUID type (type descriptor 3) is represented by IOBluetoothSDPUUID. The string and URL types (type descriptor 4 and 8) are represented by NSString. The sequence types (type descriptor 6 and 7) are represented by NSArray.

Typically, you will not need to create an IOBluetoothSDPDataElement directly, the system will do that automatically for both client and server operations. However, the current API for adding SDP services to the system does allow the use of an NSDictionary based format for creating new services. The purpose for that is to allow a service to be built up completely in a text file (a plist for example) and then easily imported into an app and added to the system without a lot of tedious code to build up the entire SDP service record.

The basis for that NSDictionary structure comes from the IOBluetoothSDPDataElement. At its simplest, a data element is made up of three parts: the type descriptor, the size (from which the size descriptor is generated) and the actual value. To provide a complete representation of a data element, an NSDictionary with three entries can be used. Each of the three entries has a key/value pair representing one of the three attributes of a data element. The first key/value pair has a key ‘DataElementType’ that contains a number value with the actual type descriptor for the data element. The second pair has a key ‘DataElementSize’ that contains the actual size of the element in bytes. The size descriptor will be calculated based on the size and type of the element. The third pair is the value itself whose key is ‘DataElementValue’ and whose type corresponds to the type mapping above.

In addition to this complete description of a data element, their are some shortcuts that can be used for some of the common types and sizes.

If the ‘DataElementType’ value is one of the numeric types (1, 2), the ‘DataElementValue’ can be an NSData instead of an NSNumber. In that case, the numeric data is taken in network byte order (MSB first). Additionally, the ‘DataElementSize’ parameter may be omitted and the size will be taken from the length of the data object.

If the ‘DataElementType’ value is the nil type (0), no ‘DataElementSize’ or ‘DataElementValue’ entries are needed.

If the ‘DataElementType’ value is any of the other types, the ‘DataElementSize’ entry is not needed since the size will be taken directly from the value (data, array, string).

In the case where the element is an unsigned, 32-bit integer (type descriptor 1, size descriptor 4), the value itself may simply be a number (instead of a dictionary as in the previous examples). In the case where the element is a UUID (type descriptor 3), the value itself may be a data object. The UUID type will be inferred and the size taken from the length of the data object.

In the case where the element is a text string (type descriptor 4), the value may be a string object. The text string type will be inferred and the size taken from the length of the string.

In the case where the element is a data element sequence, the value may be an array object. The type will be inferred and the size taken from the length of the array. Additionally, the array must contain sub-elements that will be parsed out individually.

## Topics

### Initializers
- [init!(elementValue: NSObject!)](iobluetoothsdpdataelement/init(elementvalue:).md)
  Initializes a new IOBluetoothSDPDataElement with the given value.
- [init!(type: BluetoothSDPDataElementTypeDescriptor, sizeDescriptor: BluetoothSDPDataElementSizeDescriptor, size: UInt32, value: NSObject!)](iobluetoothsdpdataelement/init(type:sizedescriptor:size:value:).md)
  Initializes a new IOBluetoothSDPDataElement with the given attributes.
### Instance Methods
- [func contains(IOBluetoothSDPDataElement!) -> Bool](iobluetoothsdpdataelement/contains(_:).md)
  Checks to see if the target data element is the same as the dataElement parameter or if it contains the dataElement parameter (if its a sequence type).
- [func containsValue(NSObject!) -> Bool](iobluetoothsdpdataelement/containsvalue(_:).md)
  Checks to see if the target data element’s value is the same as the value parameter or if it contains the value parameter.
- [func getArrayValue() -> [Any]!](iobluetoothsdpdataelement/getarrayvalue.md)
  If the data element is represented by an array object, it returns the value as an NSArray.
- [func getDataValue() -> Data!](iobluetoothsdpdataelement/getdatavalue.md)
  If the data element is represented by a data object, it returns the value as an NSData.
- [func getNumberValue() -> NSNumber!](iobluetoothsdpdataelement/getnumbervalue.md)
  If the data element is represented by a number, it returns the value as an NSNumber.
- [func getRef() -> Unmanaged<IOBluetoothSDPDataElementRef>!](iobluetoothsdpdataelement/getref.md)
  Returns an IOBluetoothSDPDataElementRef representation of the target IOBluetoothSDPDataElement object.
- [func getSize() -> UInt32](iobluetoothsdpdataelement/getsize.md)
  Returns the size in bytes of the target data element.
- [func getSizeDescriptor() -> BluetoothSDPDataElementSizeDescriptor](iobluetoothsdpdataelement/getsizedescriptor.md)
  Returns the SDP spec defined data element size descriptor for the target data element.
- [func getStringValue() -> String!](iobluetoothsdpdataelement/getstringvalue.md)
  If the data element is represented by a string object, it returns the value as an NSString.
- [func getTypeDescriptor() -> BluetoothSDPDataElementTypeDescriptor](iobluetoothsdpdataelement/gettypedescriptor.md)
  Returns the SDP spec defined data element type descriptor for the target data element.
- [func getUUIDValue() -> IOBluetoothSDPUUID!](iobluetoothsdpdataelement/getuuidvalue.md)
  If the data element is a UUID (type 3), it returns the value as an IOBluetoothSDPUUID.
- [func getValue() -> NSObject!](iobluetoothsdpdataelement/getvalue.md)
  Returns the object value of the data element.
### Type Methods
- [class func withElementValue(NSObject!) -> Self!](iobluetoothsdpdataelement/withelementvalue(_:).md)
  Creates a new IOBluetoothSDPDataElement with the given value.
- [class func withSDPDataElementRef(IOBluetoothSDPDataElementRef!) -> Self!](iobluetoothsdpdataelement/withsdpdataelementref(_:).md)
  Method call to convert an IOBluetoothSDPDataElementRef into an IOBluetoothSDPDataElement *.
- [class func withType(BluetoothSDPDataElementTypeDescriptor, sizeDescriptor: BluetoothSDPDataElementSizeDescriptor, size: UInt32, value: NSObject!) -> Self!](iobluetoothsdpdataelement/withtype(_:sizedescriptor:size:value:).md)
  Creates a new IOBluetoothSDPDataElement with the given attributes.

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

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpdataelement)*