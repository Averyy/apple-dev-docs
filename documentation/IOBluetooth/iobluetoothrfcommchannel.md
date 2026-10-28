# IOBluetoothRFCOMMChannel

**Framework**: IOBluetooth  
**Kind**: class  
**Role**: Class

An instance of this class represents an RFCOMM channel as defined by the Bluetooth SDP spec..

**Availability**:
- macOS

## Declaration

```swift
class IOBluetoothRFCOMMChannel
```

```objc
@interface IOBluetoothRFCOMMChannel : IOBluetoothObject
```

## Overview

An RFCOMM channel object can be obtained by opening an RFCOMM channel in a device, or by requesting a notification when a channel is created (this is commonly used to provide services).

## Topics

### Instance Methods
- [func close() -> IOReturn](./iobluetoothrfcommchannel/close%28%29.md)
  Close the channel.
- [func delegate() -> Any!](./iobluetoothrfcommchannel/delegate%28%29.md)
  Returns the object delegate
- [func getDevice() -> IOBluetoothDevice!](./iobluetoothrfcommchannel/getdevice%28%29.md)
  Returns the Bluetooth Device that carries the rfcomm data.
- [func getID() -> BluetoothRFCOMMChannelID](./iobluetoothrfcommchannel/getid%28%29.md)
  Returns the object rfcomm channel ID.
- [func getMTU() -> BluetoothRFCOMMMTU](./iobluetoothrfcommchannel/getmtu%28%29.md)
  Returns the channel maximum transfer unit.
- [func getObjectID() -> IOBluetoothObjectID](./iobluetoothrfcommchannel/getobjectid%28%29.md)
  Returns the IOBluetoothObjectID of the given IOBluetoothRFCOMMChannel.
- [func getRef() -> Unmanaged<IOBluetoothRFCOMMChannelRef>!](./iobluetoothrfcommchannel/getref%28%29.md)
  Returns an IOBluetoothRFCOMMChannelRef representation of the target IOBluetoothRFCOMMChannel object.
- [func isIncoming() -> Bool](./iobluetoothrfcommchannel/isincoming%28%29.md)
  Returns the direction of the channel. An incoming channel is one that was opened by the remote device.
- [func isOpen() -> Bool](./iobluetoothrfcommchannel/isopen%28%29.md)
  Returns the state of the channel.
- [func isTransmissionPaused() -> Bool](./iobluetoothrfcommchannel/istransmissionpaused%28%29.md)
  Returns TRUE if flow control is off.
- [func register(forChannelCloseNotification: Any!, selector: Selector!) -> IOBluetoothUserNotification!](./iobluetoothrfcommchannel/register%28forchannelclosenotification,selector%29.md)
  Allows a client to register for a channel close notification.
- [func sendRemoteLineStatus(BluetoothRFCOMMLineStatus) -> IOReturn](./iobluetoothrfcommchannel/sendremotelinestatus%28_%29.md)
  Sends an error to the remote side.
- [func setDelegate(Any!) -> IOReturn](./iobluetoothrfcommchannel/setdelegate%28_%29.md)
  Allows an object to register itself as a client of the RFCOMM channel.
- [func setSerialParameters(UInt32, dataBits: UInt8, parity: BluetoothRFCOMMParityType, stopBits: UInt8) -> IOReturn](./iobluetoothrfcommchannel/setserialparameters%28_,databits,parity,stopbits%29.md)
  Changes the parameters of the serial connection.
- [func writeAsync(UnsafeMutableRawPointer!, length: UInt16, refcon: UnsafeMutableRawPointer!) -> IOReturn](./iobluetoothrfcommchannel/writeasync%28_,length,refcon%29.md)
  Sends a block of data in the channel asynchronously.
- [func writeSync(UnsafeMutableRawPointer!, length: UInt16) -> IOReturn](./iobluetoothrfcommchannel/writesync%28_,length%29.md)
  Sends a block of data in the channel synchronously.
- [- write:length:sleep:](./iobluetoothrfcommchannel/write_length_sleep_.md)
  Sends a block of data in the channel syncronously.
- [- writeSimple:length:sleep:bytesSent:](./iobluetoothrfcommchannel/writesimple_length_sleep_bytessent_.md)
  Sends a block of data in the channel.
### Type Methods
- [class func register(forChannelOpenNotifications: Any!, selector: Selector!) -> IOBluetoothUserNotification!](./iobluetoothrfcommchannel/register%28forchannelopennotifications,selector%29.md)
  Allows a client to register for RFCOMM channel open notifications for any RFCOMM channel.
- [class func register(forChannelOpenNotifications: Any!, selector: Selector!, withChannelID: BluetoothRFCOMMChannelID, direction: IOBluetoothUserNotificationChannelDirection) -> IOBluetoothUserNotification!](./iobluetoothrfcommchannel/register%28forchannelopennotifications,selector,withchannelid,direction%29.md)
  Allows a client to register for RFCOMM channel open notifications for certain types of RFCOMM channels.
- [class func withObjectID(IOBluetoothObjectID) -> Self!](./iobluetoothrfcommchannel/withobjectid%28_%29.md)
  Returns the IObluetoothRFCOMMChannel with the given IOBluetoothObjectID.
- [class func withRFCOMMChannelRef(IOBluetoothRFCOMMChannelRef!) -> Self!](./iobluetoothrfcommchannel/withrfcommchannelref%28_%29.md)
  Method call to convert an IOBluetoothRFCOMMChannelRef into an IOBluetoothRFCOMMChannel *.
### Instance Variables
- [delegate](./iobluetoothrfcommchannel/delegate-c.ivar.md)
- [mChannelID](./iobluetoothrfcommchannel/mchannelid.md)
- [mChannelIsOpen](./iobluetoothrfcommchannel/mchannelisopen.md)
- [mDataAvailablePort](./iobluetoothrfcommchannel/mdataavailableport.md)
- [mDevice](./iobluetoothrfcommchannel/mdevice.md)
- [mEventDataListener](./iobluetoothrfcommchannel/meventdatalistener.md)
- [mEventDataListenerRefCon](./iobluetoothrfcommchannel/meventdatalistenerrefcon.md)
- [mIncomingDataListener](./iobluetoothrfcommchannel/mincomingdatalistener.md)
- [mIncomingDataListenerRefCon](./iobluetoothrfcommchannel/mincomingdatalistenerrefcon.md)
- [mIncomingDataQueue](./iobluetoothrfcommchannel/mincomingdataqueue.md)
- [mIsIncoming](./iobluetoothrfcommchannel/misincoming.md)
- [mL2Channel](./iobluetoothrfcommchannel/ml2channel.md)
- [mMTU](./iobluetoothrfcommchannel/mmtu.md)
- [mObjectID](./iobluetoothrfcommchannel/mobjectid.md)

## Relationships

### Inherits From
- [IOBluetoothObject](./iobluetoothobject.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [PortDelegate](../Foundation/portdelegate.md)
- [StreamDelegate](../Foundation/streamdelegate.md)

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
- [class IOBluetoothRFCOMMChannelRef](./iobluetoothrfcommchannelref.md)
- [class IOBluetoothSDPDataElement](./iobluetoothsdpdataelement.md)
  An instance of this class represents a single SDP data element as defined by the Bluetooth SDP spec.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothrfcommchannel)*