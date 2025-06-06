# OBEXSession

**Framework**: IOBluetooth  
**Kind**: class

Object representing an OBEX connection to a remote target.

**Availability**:
- macOS ?+

## Declaration

```swift
class OBEXSession
```

#### Overview

You will have no need for a obtaining/using a raw OBEXSession, since it requires an underlying transport to do anything useful. However, once you have an object that is a subclass of this class, you can use the functions herein to manipulate that OBEXSession. First off, you will want to use OBEXConnect (if you are a client session) to actually cause the transport to open a connection to a remote target and establish an OBEX connection over it. From there you can issue more commands based on the responses from a server.

If you are a server session, the first thing you should receive is an OBEXConnect command packet, and you will want to issue an OBEXConnectResponse packet, with your reesponse to that command (success, denied, bad request, etc.).

You can use the session accessors to access certain information, such as the negotiated max packet length.

If you wish to implement your own OBEXSession over a transport such as ethernet, you will need to see the end of the file to determine which functions to override, and what to pass to those functions.

No timeout mechanism has been implemented so far for an OBEXSessions. If you need timeouts, you will need to implement them yourself. This is being explored for a future revision. However, be aware that the OBEX Specification does not explicitly require timeouts, so be sure you allow ample time for commands to complete, as some devices may be slow when sending large amounts of data.

## Topics

### DataTypes
- [struct OBEXTransportEvent](obextransportevent.md)
- [typealias OBEXTransportEventType](obextransporteventtype.md)
### Instance Methods
- [func clientHandleIncomingData(UnsafeMutablePointer<OBEXTransportEvent>!)](obexsession/clienthandleincomingdata(_:).md)
  Tranport subclasses need to invoke this from their own data-receive handlers. For example, when data is received over a Bluetooth RFCOMM channel in the IOBluetoothOBEXSession, it in turn calls this to dispatch the data. If you do not handle this case, your server session will not work, guaranteed.
- [func closeTransportConnection() -> OBEXError](obexsession/closetransportconnection.md)
  You must override this - it will be called when the transport connection should be shutdown.
- [func getAvailableCommandPayloadLength(OBEXOpCode) -> OBEXMaxPacketLength](obexsession/getavailablecommandpayloadlength(_:).md)
  Determine the maximum amount of data you can send in a particular command as an OBEX client session.
- [func getAvailableCommandResponsePayloadLength(OBEXOpCode) -> OBEXMaxPacketLength](obexsession/getavailablecommandresponsepayloadlength(_:).md)
  Determine the maximum amount of data you can send in a particular command response as an OBEX server session.
- [func getMaxPacketLength() -> OBEXMaxPacketLength](obexsession/getmaxpacketlength.md)
  Gets current max packet length.
- [func hasOpenOBEXConnection() -> Bool](obexsession/hasopenobexconnection.md)
  Has a successful connect packet been sent and received? This API tells you so.
- [func hasOpenTransportConnection() -> Bool](obexsession/hasopentransportconnection.md)
  You must override this - it will be called periodically to determine if a transport connection is open or not.
- [func obexAbort(UnsafeMutableRawPointer!, optionalHeadersLength: Int, eventSelector: Selector!, selectorTarget: Any!, refCon: UnsafeMutableRawPointer!) -> OBEXError](obexsession/obexabort(_:optionalheaderslength:eventselector:selectortarget:refcon:).md)
  Send an OBEX Abort command to the session’s target.
- [func obexAbortResponse(OBEXOpCode, optionalHeaders: UnsafeMutableRawPointer!, optionalHeadersLength: Int, eventSelector: Selector!, selectorTarget: Any!, refCon: UnsafeMutableRawPointer!) -> OBEXError](obexsession/obexabortresponse(_:optionalheaders:optionalheaderslength:eventselector:selectortarget:refcon:).md)
  Send an abort response to a session’s target.
- [func obexConnect(OBEXFlags, maxPacketLength: OBEXMaxPacketLength, optionalHeaders: UnsafeMutableRawPointer!, optionalHeadersLength: Int, eventSelector: Selector!, selectorTarget: Any!, refCon: UnsafeMutableRawPointer!) -> OBEXError](obexsession/obexconnect(_:maxpacketlength:optionalheaders:optionalheaderslength:eventselector:selectortarget:refcon:).md)
  Initiate an OBEX connection to a device. Causes underlying transport (Bluetooth, et al) to attempt to connect to a remote device. After success, an OBEX connect packet is sent to establish the OBEX Connection.
- [func obexConnectResponse(OBEXOpCode, flags: OBEXFlags, maxPacketLength: OBEXMaxPacketLength, optionalHeaders: UnsafeMutableRawPointer!, optionalHeadersLength: Int, eventSelector: Selector!, selectorTarget: Any!, refCon: UnsafeMutableRawPointer!) -> OBEXError](obexsession/obexconnectresponse(_:flags:maxpacketlength:optionalheaders:optionalheaderslength:eventselector:selectortarget:refcon:).md)
  Send a connect response to a session’s target.
- [func obexDisconnect(UnsafeMutableRawPointer!, optionalHeadersLength: Int, eventSelector: Selector!, selectorTarget: Any!, refCon: UnsafeMutableRawPointer!) -> OBEXError](obexsession/obexdisconnect(_:optionalheaderslength:eventselector:selectortarget:refcon:).md)
  Send an OBEX Disconnect command to the session’s target. THIS DOES NOT necessarily close the underlying transport connection. Deleting the session will ensure that closure.
- [func obexDisconnectResponse(OBEXOpCode, optionalHeaders: UnsafeMutableRawPointer!, optionalHeadersLength: Int, eventSelector: Selector!, selectorTarget: Any!, refCon: UnsafeMutableRawPointer!) -> OBEXError](obexsession/obexdisconnectresponse(_:optionalheaders:optionalheaderslength:eventselector:selectortarget:refcon:).md)
  Send a disconnect response to a session’s target.
- [func obexGet(Bool, headers: UnsafeMutableRawPointer!, headersLength: Int, eventSelector: Selector!, selectorTarget: Any!, refCon: UnsafeMutableRawPointer!) -> OBEXError](obexsession/obexget(_:headers:headerslength:eventselector:selectortarget:refcon:).md)
  Send an OBEX Get command to the session’s target.
- [func obexGetResponse(OBEXOpCode, optionalHeaders: UnsafeMutableRawPointer!, optionalHeadersLength: Int, eventSelector: Selector!, selectorTarget: Any!, refCon: UnsafeMutableRawPointer!) -> OBEXError](obexsession/obexgetresponse(_:optionalheaders:optionalheaderslength:eventselector:selectortarget:refcon:).md)
  Send a get response to a session’s target.
- [func obexPut(Bool, headersData: UnsafeMutableRawPointer!, headersDataLength: Int, bodyData: UnsafeMutableRawPointer!, bodyDataLength: Int, eventSelector: Selector!, selectorTarget: Any!, refCon: UnsafeMutableRawPointer!) -> OBEXError](obexsession/obexput(_:headersdata:headersdatalength:bodydata:bodydatalength:eventselector:selectortarget:refcon:).md)
  Send an OBEX Put command to the session’s target.
- [func obexPutResponse(OBEXOpCode, optionalHeaders: UnsafeMutableRawPointer!, optionalHeadersLength: Int, eventSelector: Selector!, selectorTarget: Any!, refCon: UnsafeMutableRawPointer!) -> OBEXError](obexsession/obexputresponse(_:optionalheaders:optionalheaderslength:eventselector:selectortarget:refcon:).md)
  Send a put response to a session’s target.
- [func obexSetPath(OBEXFlags, constants: OBEXConstants, optionalHeaders: UnsafeMutableRawPointer!, optionalHeadersLength: Int, eventSelector: Selector!, selectorTarget: Any!, refCon: UnsafeMutableRawPointer!) -> OBEXError](obexsession/obexsetpath(_:constants:optionalheaders:optionalheaderslength:eventselector:selectortarget:refcon:).md)
  Send an OBEX SetPath command to the session’s target.
- [func obexSetPathResponse(OBEXOpCode, optionalHeaders: UnsafeMutableRawPointer!, optionalHeadersLength: Int, eventSelector: Selector!, selectorTarget: Any!, refCon: UnsafeMutableRawPointer!) -> OBEXError](obexsession/obexsetpathresponse(_:optionalheaders:optionalheaderslength:eventselector:selectortarget:refcon:).md)
  Send a set path response to a session’s target.
- [func openTransportConnection(Selector!, selectorTarget: Any!, refCon: UnsafeMutableRawPointer!) -> OBEXError](obexsession/opentransportconnection(_:selectortarget:refcon:).md)
  Opens a transport connection to a device. A Bluetooth connection is one example of a transport.
- [func sendData(toTransport: UnsafeMutableRawPointer!, dataLength: Int) -> OBEXError](obexsession/senddata(totransport:datalength:).md)
  You must override this to send data over your transport. This does nothing by default, it will return a kOBEXUnsupportedError.
- [func serverHandleIncomingData(UnsafeMutablePointer<OBEXTransportEvent>!)](obexsession/serverhandleincomingdata(_:).md)
  Tranport subclasses need to invoke this from their own data-receive handlers. For example, when data is received over a Bluetooth RFCOMM channel in the IOBluetoothOBEXSession, it in turn calls this to dispatch the data. If you do not handle this case, your server session will not work, guaranteed.
- [func setEventCallback(OBEXSessionEventCallback!)](obexsession/seteventcallback(_:).md)
  Sets the C-API callback used when the session recieves data.
- [func setEventRefCon(UnsafeMutableRawPointer!)](obexsession/seteventrefcon(_:).md)
  Sets the C-API callback refCon used when the session recieves data.
- [func setEventSelector(Selector!, target: Any!, refCon: UnsafeMutableRawPointer!)](obexsession/seteventselector(_:target:refcon:).md)
  Allow you to set a selector to be called when events occur on the OBEX session.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [IOBluetoothOBEXSession](iobluetoothobexsession.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexsession)*