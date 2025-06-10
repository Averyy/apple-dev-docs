# IOBluetoothSDPUUID

**Framework**: IOBluetooth  
**Kind**: class

An NSData subclass that represents a UUID as defined in the Bluetooth SDP spec.

**Availability**:
- macOS ?+

## Declaration

```swift
class IOBluetoothSDPUUID
```

#### Overview

The IOBluetoothSDPUUID class can represent a UUID of any valid size (16, 32 or 128 bits). It provides the ability to compare two UUIDs no matter what their size as well as the ability to promote the size of a UUID to a larger one.

## Topics

### Initializers
- [convenience init!(bytes: UnsafeRawPointer!, length: UInt32)](iobluetoothsdpuuid/init(bytes:length:).md)
  Creates a new IOBluetoothSDPUUID object with the given bytes of the given length.
- [convenience init!(data: Data!)](iobluetoothsdpuuid/init(data:).md)
  Creates a new IOBluetoothSDPUUID object from the given NSData.
- [init!(uuid16: BluetoothSDPUUID16)](iobluetoothsdpuuid/init(uuid16:).md)
  Initializes a new 16-bit IOBluetoothSDPUUID with the given UUID16
- [init!(uuid32: BluetoothSDPUUID32)](iobluetoothsdpuuid/init(uuid32:).md)
  Creates a new 32-bit IOBluetoothSDPUUID with the given UUID32
### Instance Methods
- [func classForArchiver() -> AnyClass!](iobluetoothsdpuuid/classforarchiver.md)
- [func classForCoder() -> AnyClass!](iobluetoothsdpuuid/classforcoder.md)
- [func classForPortCoder() -> AnyClass!](iobluetoothsdpuuid/classforportcoder.md)
- [func getWithLength(UInt32) -> Self!](iobluetoothsdpuuid/getwithlength(_:).md)
  Returns an IOBluetoothSDPUUID object matching the target UUID, but with the given number of bytes.
- [func isEqual(to: IOBluetoothSDPUUID!) -> Bool](iobluetoothsdpuuid/isequal(to:).md)
  Compares the target IOBluetoothSDPUUID object with the given otherUUID object.
### Type Methods
- [class func uuid16(BluetoothSDPUUID16) -> Self!](iobluetoothsdpuuid/uuid16(_:).md)
  Creates a new 16-bit IOBluetoothSDPUUID with the given UUID16
- [class func uuid32(BluetoothSDPUUID32) -> Self!](iobluetoothsdpuuid/uuid32(_:).md)
  Creates a new 32-bit IOBluetoothSDPUUID with the given UUID32

## Relationships

### Inherits From
- [NSData](../Foundation/NSData.md)
### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [CVarArg](../Swift/CVarArg.md)
- [Collection](../Swift/Collection.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [DataProtocol](../Foundation/DataProtocol.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSMutableCopying](../Foundation/NSMutableCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Sequence](../Swift/Sequence.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpuuid)*