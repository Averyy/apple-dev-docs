# IOBluetoothOBEXSession

**Framework**: IOBluetooth  
**Kind**: class

An OBEX Session with a Bluetooth RFCOMM channel as the transport.

**Availability**:
- macOS ?+

## Declaration

```swift
class IOBluetoothOBEXSession
```

## Topics

### Initializers
- [init!(device: IOBluetoothDevice!, channelID: BluetoothRFCOMMChannelID)](iobluetoothobexsession/init(device:channelid:).md)
  Initializes a Bluetooth-based OBEX Session using a Bluetooth device.
- [init!(incomingRFCOMMChannel: IOBluetoothRFCOMMChannel!, eventSelector: Selector!, selectorTarget: Any!, refCon: UnsafeMutableRawPointer!)](iobluetoothobexsession/init(incomingrfcommchannel:eventselector:selectortarget:refcon:).md)
  Initializes a Bluetooth-based OBEX Session using an incoming RFCOMM channel.
- [init!(sdpServiceRecord: IOBluetoothSDPServiceRecord!)](iobluetoothobexsession/init(sdpservicerecord:).md)
  Initializes a Bluetooth-based OBEX Session using an SDP service record.
### Instance Methods
- [func closeTransportConnection() -> OBEXError](iobluetoothobexsession/closetransportconnection.md)
  An OBEXSession override. When this is called by the session baseclass, we will close the transport connection if it is opened. In our case, it will be the RFCOMM channel that needs closing.
- [func getDevice() -> IOBluetoothDevice!](iobluetoothobexsession/getdevice.md)
  Get the Bluetooth Device being used by the session object.
- [func getRFCOMMChannel() -> IOBluetoothRFCOMMChannel!](iobluetoothobexsession/getrfcommchannel.md)
  Get the Bluetooth RFCOMM channel being used by the session object.
- [func hasOpenTransportConnection() -> Bool](iobluetoothobexsession/hasopentransportconnection.md)
  An OBEXSession override. When this is called by the session baseclass, we will return whether or not we have a transport connection established to another OBEX server/client. In our case we will tell whether or not the RFCOMM channel to a remote device is still open.
- [func isSessionTargetAMac() -> Bool](iobluetoothobexsession/issessiontargetamac.md)
  Tells whether the target device is a Mac by checking its service record.
- [func openTransportConnection(Selector!, selectorTarget: Any!, refCon: UnsafeMutableRawPointer!) -> OBEXError](iobluetoothobexsession/opentransportconnection(_:selectortarget:refcon:).md)
  An OBEXSession override. When this is called by the session baseclass, we will attempt to open the transport connection. In our case, this would be an RFCOMM channel to another Bluetooth device.
- [func restartTransmission()](iobluetoothobexsession/restarttransmission.md)
  If the transmission was stopped due to the lack of buffers this call restarts it.
- [func sendBufferTroughChannel() -> IOReturn](iobluetoothobexsession/sendbuffertroughchannel.md)
  Sends the next block of data through the rfcomm channel.
- [func sendData(toTransport: UnsafeMutableRawPointer!, dataLength: Int) -> OBEXError](iobluetoothobexsession/senddata(totransport:datalength:).md)
  An OBEXSession override. When this is called by the session baseclass, we will send the data we are given over our transport connection. If none is open, we could try to open it, or just return an error. In our case, it will be sent over the RFCOMM channel.
- [func setOBEXSessionOpenConnectionCallback(IOBluetoothOBEXSessionOpenConnectionCallback!, refCon: UnsafeMutableRawPointer!)](iobluetoothobexsession/setobexsessionopenconnectioncallback(_:refcon:).md)
  For C API support. Allows you to set the callback to be invoked when the OBEX connection is actually opened.
- [func setOpenTransportConnectionAsyncSelector(Selector!, target: Any!, refCon: UnsafeMutableRawPointer!)](iobluetoothobexsession/setopentransportconnectionasyncselector(_:target:refcon:).md)
  Allows you to set the selector to be used when a transport connection is opened, or fails to open.
### Type Methods
- [class func withDevice(IOBluetoothDevice!, channelID: BluetoothRFCOMMChannelID) -> Self!](iobluetoothobexsession/withdevice(_:channelid:).md)
  Creates a Bluetooth-based OBEX Session using a Bluetooth device and a Bluetooth RFCOMM channel ID.
- [class func withIncomingRFCOMMChannel(IOBluetoothRFCOMMChannel!, eventSelector: Selector!, selectorTarget: Any!, refCon: UnsafeMutableRawPointer!) -> Self!](iobluetoothobexsession/withincomingrfcommchannel(_:eventselector:selectortarget:refcon:).md)
  Creates a Bluetooth-based OBEX Session using an incoming RFCOMM channel.
- [class func withSDPServiceRecord(IOBluetoothSDPServiceRecord!) -> Self!](iobluetoothobexsession/withsdpservicerecord(_:).md)
  Creates a Bluetooth-based OBEX Session using an SDP service record, typically obtained from a device/service browser window controller.

## Relationships

### Inherits From
- [OBEXSession](obexsession.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [IOBluetoothRFCOMMChannelDelegate](iobluetoothrfcommchanneldelegate.md)
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
- [class IOBluetoothHostController](iobluetoothhostcontroller.md)
  This class is a representation of a Bluetooth Host Controller Interface that is present on the local computer (either plugged in externally or available internally).
- [class IOBluetoothL2CAPChannel](iobluetoothl2capchannel.md)
  An instance of IOBluetoothL2CAPChannel represents a single open L2CAP channel.
- [class IOBluetoothL2CAPChannelRef](iobluetoothl2capchannelref.md)
- [class IOBluetoothObject](iobluetoothobject.md)
- [class IOBluetoothObjectRef](iobluetoothobjectref.md)
- [class IOBluetoothRFCOMMChannel](iobluetoothrfcommchannel.md)
  An instance of this class represents an RFCOMM channel as defined by the Bluetooth SDP spec..
- [class IOBluetoothRFCOMMChannelRef](iobluetoothrfcommchannelref.md)
- [class IOBluetoothSDPDataElement](iobluetoothsdpdataelement.md)
  An instance of this class represents a single SDP data element as defined by the Bluetooth SDP spec.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothobexsession)*