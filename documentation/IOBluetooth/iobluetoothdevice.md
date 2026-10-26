# IOBluetoothDevice

**Framework**: IOBluetooth  
**Kind**: class  
**Role**: Class

An instance of IOBluetoothDevice represents a single remote Bluetooth device.

**Availability**:
- macOS

## Declaration

```swift
class IOBluetoothDevice
```

```objc
@interface IOBluetoothDevice : IOBluetoothObject
```

#### Overview

An IOBluetoothDevice object may exist independent of the existence of a baseband connection with the target device. Using this object, a client can request creation and destruction of baseband connections, and request the opening of L2CAP and RFCOMM channels on the remote device. Many of the other APIs in the IOBluetooth framework will return this object, or it’s C counterpart (IOBluetoothDeviceRef).

## Topics

### Initializers
- [convenience init!(address: UnsafePointer<BluetoothDeviceAddress>!)](./iobluetoothdevice/init%28address%29.md)
  Returns the IOBluetoothDevice object for the given BluetoothDeviceAddress
- [convenience init!(addressString: String!)](./iobluetoothdevice/init%28addressstring%29.md)
  Returns the IOBluetoothDevice object for the given BluetoothDeviceAddress
- [init?(coder: NSCoder)](./iobluetoothdevice/init%28coder%29.md)
### Instance Properties
- [var addressString: String!](./iobluetoothdevice/addressstring.md)
  Get a string representation of the Bluetooth device address for the target device. The format of the string is the same as returned by IOBluetoothNSStringFromDeviceAddress().
- [var classOfDevice: BluetoothClassOfDevice](./iobluetoothdevice/classofdevice.md)
  Gets the full class of device value for the remote device.
- [var connectionHandle: BluetoothConnectionHandle](./iobluetoothdevice/connectionhandle.md)
  Get the connection handle for the baseband connection.
- [var deviceClassMajor: BluetoothDeviceClassMajor](./iobluetoothdevice/deviceclassmajor.md)
  Get the major device class of the device.
- [var deviceClassMinor: BluetoothDeviceClassMinor](./iobluetoothdevice/deviceclassminor.md)
  Get the minor service class of the device.
- [var isHandsFreeAudioGateway: Bool](./iobluetoothdevice/ishandsfreeaudiogateway.md)
- [var isHandsFreeDevice: Bool](./iobluetoothdevice/ishandsfreedevice.md)
- [var lastNameUpdate: Date!](./iobluetoothdevice/lastnameupdate.md)
  Get the date/time of the last successful remote name request.
- [var name: String!](./iobluetoothdevice/name.md)
  Get the human readable name of the remote device.
- [var nameOrAddress: String!](./iobluetoothdevice/nameoraddress.md)
  Get the human readable name of the remote device. If the name is not present, it will return a string containing the device’s address.
- [var serviceClassMajor: BluetoothServiceClassMajor](./iobluetoothdevice/serviceclassmajor.md)
  Get the major service class of the device.
- [var services: [Any]!](./iobluetoothdevice/services.md)
  Gets an array of service records for the device.
### Instance Methods
- [func addToFavorites() -> IOReturn](./iobluetoothdevice/addtofavorites%28%29.md)
  Adds the target device to the user’s favorite devices list.
- [func awakeAfter(using: NSCoder!) -> Any!](./iobluetoothdevice/awakeafter%28using%29.md)
- [func closeConnection() -> IOReturn](./iobluetoothdevice/closeconnection%28%29.md)
  Close down the baseband connection to the device.
- [func getAddress() -> UnsafePointer<BluetoothDeviceAddress>!](./iobluetoothdevice/getaddress%28%29.md)
  Get the Bluetooth device address for the target device.
- [func getClockOffset() -> BluetoothClockOffset](./iobluetoothdevice/getclockoffset%28%29.md)
  Get the clock offset value of the device.
- [func getEncryptionMode() -> BluetoothHCIEncryptionMode](./iobluetoothdevice/getencryptionmode%28%29.md)
  Get the encryption mode for the baseband connection.
- [func getLastInquiryUpdate() -> Date!](./iobluetoothdevice/getlastinquiryupdate%28%29.md)
  Get the date/time of the last time the device was returned during an inquiry.
- [func getLastServicesUpdate() -> Date!](./iobluetoothdevice/getlastservicesupdate%28%29.md)
  Get the date/time of the last SDP query.
- [func getLinkType() -> BluetoothLinkType](./iobluetoothdevice/getlinktype%28%29.md)
  Get the link type for the baseband connection.
- [func getPageScanMode() -> BluetoothPageScanMode](./iobluetoothdevice/getpagescanmode%28%29.md)
  Get the page scan mode for the device.
- [func getPageScanPeriodMode() -> BluetoothPageScanPeriodMode](./iobluetoothdevice/getpagescanperiodmode%28%29.md)
  Get the value of the page scan period mode for the device.
- [func getPageScanRepetitionMode() -> BluetoothPageScanRepetitionMode](./iobluetoothdevice/getpagescanrepetitionmode%28%29.md)
  Get the value of the page scan repetition mode for the device.
- [func getServiceRecord(for: IOBluetoothSDPUUID!) -> IOBluetoothSDPServiceRecord!](./iobluetoothdevice/getservicerecord%28for%29.md)
  Search for a service record containing the given UUID.
- [func handsFreeAudioGatewayServiceRecord() -> IOBluetoothSDPServiceRecord!](./iobluetoothdevice/handsfreeaudiogatewayservicerecord%28%29.md)
- [func handsFreeDeviceServiceRecord() -> IOBluetoothSDPServiceRecord!](./iobluetoothdevice/handsfreedeviceservicerecord%28%29.md)
- [func isConnected() -> Bool](./iobluetoothdevice/isconnected%28%29.md)
  Indicates whether a baseband connection to the device exists.
- [func isFavorite() -> Bool](./iobluetoothdevice/isfavorite%28%29.md)
  Reports whether the target device is a favorite for the user.
- [func isIncoming() -> Bool](./iobluetoothdevice/isincoming%28%29.md)
  Returns TRUE if the device connection was generated by the remote host.
- [func isPaired() -> Bool](./iobluetoothdevice/ispaired%28%29.md)
  Returns whether the target device is paired.
- [func openConnection() -> IOReturn](./iobluetoothdevice/openconnection%28%29.md)
  Create a baseband connection to the device.
- [func openConnection(Any!) -> IOReturn](./iobluetoothdevice/openconnection%28_%29.md)
  Create a baseband connection to the device.
- [func openConnection(Any!, withPageTimeout: BluetoothHCIPageTimeout, authenticationRequired: Bool) -> IOReturn](./iobluetoothdevice/openconnection%28_,withpagetimeout,authenticationrequired%29.md)
  Create a baseband connection to the device.
- [func openL2CAPChannelAsync(AutoreleasingUnsafeMutablePointer<IOBluetoothL2CAPChannel?>!, withPSM: BluetoothL2CAPPSM, delegate: Any!) -> IOReturn](./iobluetoothdevice/openl2capchannelasync%28_,withpsm,delegate%29.md)
  Opens a new L2CAP channel to the target device. Returns immediately after starting the opening process.
- [func openL2CAPChannelAsync(AutoreleasingUnsafeMutablePointer<IOBluetoothL2CAPChannel?>!, withPSM: BluetoothL2CAPPSM, withConfiguration: [AnyHashable : Any]!, delegate: Any!) -> IOReturn](./iobluetoothdevice/openl2capchannelasync%28_,withpsm,withconfiguration,delegate%29.md)
  Opens a new L2CAP channel to the target device. Returns immediately after starting the opening process.
- [func openL2CAPChannelSync(AutoreleasingUnsafeMutablePointer<IOBluetoothL2CAPChannel?>!, withPSM: BluetoothL2CAPPSM, delegate: Any!) -> IOReturn](./iobluetoothdevice/openl2capchannelsync%28_,withpsm,delegate%29.md)
  Opens a new L2CAP channel to the target device. Returns only after the channel is opened.
- [func openL2CAPChannelSync(AutoreleasingUnsafeMutablePointer<IOBluetoothL2CAPChannel?>!, withPSM: BluetoothL2CAPPSM, withConfiguration: [AnyHashable : Any]!, delegate: Any!) -> IOReturn](./iobluetoothdevice/openl2capchannelsync%28_,withpsm,withconfiguration,delegate%29.md)
  Opens a new L2CAP channel to the target device. Returns only after the channel is opened.
- [func openRFCOMMChannelAsync(AutoreleasingUnsafeMutablePointer<IOBluetoothRFCOMMChannel?>!, withChannelID: BluetoothRFCOMMChannelID, delegate: Any!) -> IOReturn](./iobluetoothdevice/openrfcommchannelasync%28_,withchannelid,delegate%29.md)
  Opens a new RFCOMM channel to the target device. Returns immediately.
- [func openRFCOMMChannelSync(AutoreleasingUnsafeMutablePointer<IOBluetoothRFCOMMChannel?>!, withChannelID: BluetoothRFCOMMChannelID, delegate: Any!) -> IOReturn](./iobluetoothdevice/openrfcommchannelsync%28_,withchannelid,delegate%29.md)
  Opens a new RFCOMM channel to the target device. Returns only once the channel is open or failed to open.
- [func performSDPQuery(Any!) -> IOReturn](./iobluetoothdevice/performsdpquery%28_%29.md)
  Performs an SDP query on the target device.
- [func performSDPQuery(Any!, uuids: [Any]!) -> IOReturn](./iobluetoothdevice/performsdpquery%28_,uuids%29.md)
  Performs an SDP query on the target device with the specified service UUIDs.
- [func rawRSSI() -> BluetoothHCIRSSIValue](./iobluetoothdevice/rawrssi%28%29.md)
  Get the raw RSSI device (if connected).
- [func recentAccessDate() -> Date!](./iobluetoothdevice/recentaccessdate%28%29.md)
  Returns the date/time of the most recent access of the target device.
- [func register(forDisconnectNotification: Any!, selector: Selector!) -> IOBluetoothUserNotification!](./iobluetoothdevice/register%28fordisconnectnotification,selector%29.md)
  Allows a client to register for device disconnect notification.
- [func remoteNameRequest(Any!) -> IOReturn](./iobluetoothdevice/remotenamerequest%28_%29.md)
  Issues a remote name request to the target device.
- [func remoteNameRequest(Any!, withPageTimeout: BluetoothHCIPageTimeout) -> IOReturn](./iobluetoothdevice/remotenamerequest%28_,withpagetimeout%29.md)
  Issues a remote name request to the target device.
- [func removeFromFavorites() -> IOReturn](./iobluetoothdevice/removefromfavorites%28%29.md)
  Removes the target device from the user’s favorite devices list.
- [func requestAuthentication() -> IOReturn](./iobluetoothdevice/requestauthentication%28%29.md)
  Requests that the existing baseband connection be authenticated.
- [func rssi() -> BluetoothHCIRSSIValue](./iobluetoothdevice/rssi%28%29.md)
  Get the RSSI device (if connected), above or below the golden range. If the RSSI is within the golden range, a value of 0 is returned. For the actual RSSI value, use getRawRSSI. For more information, see the Bluetooth 4.0 Core Specification.
- [func sendL2CAPEchoRequest(UnsafeMutableRawPointer!, length: UInt16) -> IOReturn](./iobluetoothdevice/sendl2capechorequest%28_,length%29.md)
  Send an echo request over the L2CAP connection to a remote device.
- [func setSupervisionTimeout(UInt16) -> IOReturn](./iobluetoothdevice/setsupervisiontimeout%28_%29.md)
  Sets the connection supervision timeout.
- [- getAddressString](./iobluetoothdevice/getaddressstring.md)
  Get a string representation of the Bluetooth device address for the target device. The format of the string is the same as returned by IOBluetoothNSStringFromDeviceAddress().
- [- getClassOfDevice](./iobluetoothdevice/getclassofdevice.md)
  Gets the full class of device value for the remote device.
- [- getConnectionHandle](./iobluetoothdevice/getconnectionhandle.md)
  Get the connection handle for the baseband connection.
- [- getDeviceClassMajor](./iobluetoothdevice/getdeviceclassmajor.md)
  Get the major device class of the device.
- [- getDeviceClassMinor](./iobluetoothdevice/getdeviceclassminor.md)
  Get the minor service class of the device.
- [- getDeviceRef](./iobluetoothdevice/getdeviceref.md)
  Returns an IOBluetoothDeviceRef representation of the target IOBluetoothDevice object.
- [- getLastNameUpdate](./iobluetoothdevice/getlastnameupdate.md)
  Get the date/time of the last successful remote name request.
- [- getName](./iobluetoothdevice/getname.md)
  Get the human readable name of the remote device.
- [- getNameOrAddress](./iobluetoothdevice/getnameoraddress.md)
  Get the human readable name of the remote device. If the name is not present, it will return a string containing the device’s address.
- [- getServiceClassMajor](./iobluetoothdevice/getserviceclassmajor.md)
  Get the major service class of the device.
- [- getServices](./iobluetoothdevice/getservices.md)
- [- handsFreeAudioGatewayDriverID](./iobluetoothdevice/handsfreeaudiogatewaydriverid.md)
- [- handsFreeDeviceDriverID](./iobluetoothdevice/handsfreedevicedriverid.md)
- [- openL2CAPChannel:findExisting:newChannel:](./iobluetoothdevice/openl2capchannel_findexisting_newchannel_.md)
  Opens a new L2CAP channel to the target device. Returns immedialty after starting the opening process.
- [- openRFCOMMChannel:channel:](./iobluetoothdevice/openrfcommchannel_channel_.md)
  Opens a new RFCOMM channel to the target device. Returns only once the channel is open or failed to open.
### Type Methods
- [class func favoriteDevices() -> [Any]!](./iobluetoothdevice/favoritedevices%28%29.md)
  Gets an array of the user’s favorite devices.
- [class func pairedDevices() -> [Any]!](./iobluetoothdevice/paireddevices%28%29.md)
  Gets an array of all of the paired devices on the system.
- [class func recentDevices(UInt) -> [Any]!](./iobluetoothdevice/recentdevices%28_%29.md)
  Gets an array of recently used Bluetooth devices.
- [class func register(forConnectNotifications: Any!, selector: Selector!) -> IOBluetoothUserNotification!](./iobluetoothdevice/register%28forconnectnotifications,selector%29.md)
  Allows a client to register for device connect notifications for any connection.
- [+ withAddress:](./iobluetoothdevice/withaddress_.md)
- [+ withDeviceRef:](./iobluetoothdevice/withdeviceref_.md)
  Method call to convert an IOBluetoothDeviceRef into an IOBluetoothDevice *.
### Instance Variables
- [mAddress](./iobluetoothdevice/maddress.md)
- [mClassOfDevice](./iobluetoothdevice/mclassofdevice.md)
- [mClockOffset](./iobluetoothdevice/mclockoffset.md)
- [mConnectionHandle](./iobluetoothdevice/mconnectionhandle.md)
- [mDeviceConnectNotification](./iobluetoothdevice/mdeviceconnectnotification.md)
- [mEncryptionMode](./iobluetoothdevice/mencryptionmode.md)
- [mLastInquiryUpdate](./iobluetoothdevice/mlastinquiryupdate.md)
- [mLastNameUpdate](./iobluetoothdevice/mlastnameupdate.md)
- [mLastServicesUpdate](./iobluetoothdevice/mlastservicesupdate.md)
- [mLinkType](./iobluetoothdevice/mlinktype.md)
- [mName](./iobluetoothdevice/mname.md)
- [mPageScanMode](./iobluetoothdevice/mpagescanmode.md)
- [mPageScanPeriodMode](./iobluetoothdevice/mpagescanperiodmode.md)
- [mPageScanRepetitionMode](./iobluetoothdevice/mpagescanrepetitionmode.md)
- [mRFCOMMConnection](./iobluetoothdevice/mrfcommconnection.md)
- [mServerDevice](./iobluetoothdevice/mserverdevice.md)
- [mServiceArray](./iobluetoothdevice/mservicearray.md)

## Relationships

### Inherits From
- [IOBluetoothObject](./iobluetoothobject.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Classes
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
- [class IOBluetoothSDPDataElement](./iobluetoothsdpdataelement.md)
  An instance of this class represents a single SDP data element as defined by the Bluetooth SDP spec.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice)*