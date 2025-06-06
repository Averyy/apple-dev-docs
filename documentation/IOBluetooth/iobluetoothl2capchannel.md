# IOBluetoothL2CAPChannel

**Framework**: IOBluetooth  
**Kind**: class

An instance of IOBluetoothL2CAPChannel represents a single open L2CAP channel.

**Availability**:
- macOS ?+

## Declaration

```swift
class IOBluetoothL2CAPChannel
```

#### Overview

A client won’t create IOBluetoothL2CAPChannel objects directly. Instead, the IOBluetoothDevice’s L2CAP channel open API is responsible for opening a new L2CAP channel and returning an IOBluetoothL2CAPChannel instance representing that newly opened channel. Additionally, the IOBluetooth notification system will send notifications when new L2CAP channels are open (if requested).

After a new L2CAP channel is opened, the L2CAP configuration process will not be completed until an incoming data listener is registered with the IOBluetoothL2CAPChannel object. The reason for this is to due to the limited buffering done of incoming L2CAP data. This way, we avoid the situation where incoming data is received before the client is ready for it. Once a client is done with an IOBluetoothL2CAPChannel that it opened, it should call -closeChannel. Additionally, if the client does not intend to use the connection to the remote device any further, it should call -closeConnection on the IOBluetoothDevice object.

## Topics

### Instance Properties
- [var device: IOBluetoothDevice!](iobluetoothl2capchannel/device.md)
  Returns the IOBluetoothDevice to which the target L2CAP channel is open.
- [var incomingMTU: BluetoothL2CAPMTU](iobluetoothl2capchannel/incomingmtu.md)
  Returns the current incoming MTU for the L2CAP channel.
- [var localChannelID: BluetoothL2CAPChannelID](iobluetoothl2capchannel/localchannelid.md)
  Returns the local L2CAP channel ID for the target L2CAP channel.
- [var objectID: IOBluetoothObjectID](iobluetoothl2capchannel/objectid.md)
  Returns the IOBluetoothObjectID of the given IOBluetoothL2CAPChannel.
- [var outgoingMTU: BluetoothL2CAPMTU](iobluetoothl2capchannel/outgoingmtu.md)
  Returns the current outgoing MTU for the L2CAP channel.
- [var psm: BluetoothL2CAPPSM](iobluetoothl2capchannel/psm.md)
  Returns the PSM for the target L2CAP channel.
- [var remoteChannelID: BluetoothL2CAPChannelID](iobluetoothl2capchannel/remotechannelid.md)
  Returns the remote L2CAP channel ID for the target L2CAP channel.
### Instance Methods
- [func close() -> IOReturn](iobluetoothl2capchannel/close.md)
  Initiates the close process on an open L2CAP channel.
- [func delegate() -> Any!](iobluetoothl2capchannel/delegate.md)
  Returns the currently assigned delegate
- [func isIncoming() -> Bool](iobluetoothl2capchannel/isincoming.md)
  Returns TRUE if the channel is an incoming channel.
- [func register(forChannelCloseNotification: Any!, selector: Selector!) -> IOBluetoothUserNotification!](iobluetoothl2capchannel/register(forchannelclosenotification:selector:).md)
  Allows a client to register for a channel close notification.
- [func requestRemoteMTU(BluetoothL2CAPMTU) -> IOReturn](iobluetoothl2capchannel/requestremotemtu(_:).md)
  Initiates the process to reconfigure the L2CAP channel with a new outgoing MTU.
- [func setDelegate(Any!) -> IOReturn](iobluetoothl2capchannel/setdelegate(_:).md)
  Allows an object to register itself as client of the L2CAP channel.
- [func setDelegate(Any!, withConfiguration: [AnyHashable : Any]!) -> IOReturn](iobluetoothl2capchannel/setdelegate(_:withconfiguration:).md)
  Allows an object to register itself as client of the L2CAP channel.
- [func writeAsync(UnsafeMutableRawPointer!, length: UInt16, refcon: UnsafeMutableRawPointer!) -> IOReturn](iobluetoothl2capchannel/writeasync(_:length:refcon:).md)
  Writes the given data over the target L2CAP channel asynchronously to the remote device.
- [func writeAsyncTrap(UnsafeMutableRawPointer!, length: UInt16, refcon: UnsafeMutableRawPointer!) -> IOReturn](iobluetoothl2capchannel/writeasynctrap(_:length:refcon:).md)
- [func writeSync(UnsafeMutableRawPointer!, length: UInt16) -> IOReturn](iobluetoothl2capchannel/writesync(_:length:).md)
  Writes the given data synchronously over the target L2CAP channel to the remote device.
### Type Methods
- [class func register(forChannelOpenNotifications: Any!, selector: Selector!) -> IOBluetoothUserNotification!](iobluetoothl2capchannel/register(forchannelopennotifications:selector:).md)
  Allows a client to register for L2CAP channel open notifications for any L2CAP channel.
- [class func register(forChannelOpenNotifications: Any!, selector: Selector!, withPSM: BluetoothL2CAPPSM, direction: IOBluetoothUserNotificationChannelDirection) -> IOBluetoothUserNotification!](iobluetoothl2capchannel/register(forchannelopennotifications:selector:withpsm:direction:).md)
  Allows a client to register for L2CAP channel open notifications for certain types of L2CAP channels.
- [class func withObjectID(IOBluetoothObjectID) -> Self!](iobluetoothl2capchannel/withobjectid(_:).md)
  Returns the IObluetoothL2CAPChannel with the given IOBluetoothObjectID.

## Relationships

### Inherits From
- [IOBluetoothObject](iobluetoothobject.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [PortDelegate](../Foundation/PortDelegate.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannel)*