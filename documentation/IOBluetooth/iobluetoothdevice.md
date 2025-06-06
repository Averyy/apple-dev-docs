# IOBluetoothDevice

**Framework**: IOBluetooth  
**Kind**: class

An instance of IOBluetoothDevice represents a single remote Bluetooth device.

**Availability**:
- macOS ?+

## Declaration

```swift
class IOBluetoothDevice
```

#### Overview

An IOBluetoothDevice object may exist independent of the existence of a baseband connection with the target device. Using this object, a client can request creation and destruction of baseband connections, and request the opening of L2CAP and RFCOMM channels on the remote device. Many of the other APIs in the IOBluetooth framework will return this object, or it’s C counterpart (IOBluetoothDeviceRef).

## Topics

### Initializers
- [convenience init!(address: UnsafePointer<BluetoothDeviceAddress>!)](iobluetoothdevice/init(address:).md)
  Returns the IOBluetoothDevice object for the given BluetoothDeviceAddress
- [convenience init!(addressString: String!)](iobluetoothdevice/init(addressstring:).md)
  Returns the IOBluetoothDevice object for the given BluetoothDeviceAddress
### Instance Properties
- [var addressString: String!](iobluetoothdevice/addressstring.md)
  Get a string representation of the Bluetooth device address for the target device. The format of the string is the same as returned by IOBluetoothNSStringFromDeviceAddress().
- [var classOfDevice: BluetoothClassOfDevice](iobluetoothdevice/classofdevice.md)
  Gets the full class of device value for the remote device.
- [var connectionHandle: BluetoothConnectionHandle](iobluetoothdevice/connectionhandle.md)
  Get the connection handle for the baseband connection.
- [var deviceClassMajor: BluetoothDeviceClassMajor](iobluetoothdevice/deviceclassmajor.md)
  Get the major device class of the device.
- [var deviceClassMinor: BluetoothDeviceClassMinor](iobluetoothdevice/deviceclassminor.md)
  Get the minor service class of the device.
- [var isHandsFreeAudioGateway: Bool](iobluetoothdevice/ishandsfreeaudiogateway.md)
- [var isHandsFreeDevice: Bool](iobluetoothdevice/ishandsfreedevice.md)
- [var lastNameUpdate: Date!](iobluetoothdevice/lastnameupdate.md)
  Get the date/time of the last successful remote name request.
- [var name: String!](iobluetoothdevice/name.md)
  Get the human readable name of the remote device.
- [var nameOrAddress: String!](iobluetoothdevice/nameoraddress.md)
  Get the human readable name of the remote device. If the name is not present, it will return a string containing the device’s address.
- [var serviceClassMajor: BluetoothServiceClassMajor](iobluetoothdevice/serviceclassmajor.md)
  Get the major service class of the device.
- [var services: [Any]!](iobluetoothdevice/services.md)
  Gets an array of service records for the device.
### Instance Methods
- [func addToFavorites() -> IOReturn](iobluetoothdevice/addtofavorites.md)
  Adds the target device to the user’s favorite devices list.
- [func awakeAfter(using: NSCoder!) -> Any!](iobluetoothdevice/awakeafter(using:).md)
- [func closeConnection() -> IOReturn](iobluetoothdevice/closeconnection.md)
  Close down the baseband connection to the device.
- [func getAddress() -> UnsafePointer<BluetoothDeviceAddress>!](iobluetoothdevice/getaddress.md)
  Get the Bluetooth device address for the target device.
- [func getClockOffset() -> BluetoothClockOffset](iobluetoothdevice/getclockoffset.md)
  Get the clock offset value of the device.
- [func getEncryptionMode() -> BluetoothHCIEncryptionMode](iobluetoothdevice/getencryptionmode.md)
  Get the encryption mode for the baseband connection.
- [func getLastInquiryUpdate() -> Date!](iobluetoothdevice/getlastinquiryupdate.md)
  Get the date/time of the last time the device was returned during an inquiry.
- [func getLastServicesUpdate() -> Date!](iobluetoothdevice/getlastservicesupdate.md)
  Get the date/time of the last SDP query.
- [func getLinkType() -> BluetoothLinkType](iobluetoothdevice/getlinktype.md)
  Get the link type for the baseband connection.
- [func getPageScanMode() -> BluetoothPageScanMode](iobluetoothdevice/getpagescanmode.md)
  Get the page scan mode for the device.
- [func getPageScanPeriodMode() -> BluetoothPageScanPeriodMode](iobluetoothdevice/getpagescanperiodmode.md)
  Get the value of the page scan period mode for the device.
- [func getPageScanRepetitionMode() -> BluetoothPageScanRepetitionMode](iobluetoothdevice/getpagescanrepetitionmode.md)
  Get the value of the page scan repetition mode for the device.
- [func getServiceRecord(for: IOBluetoothSDPUUID!) -> IOBluetoothSDPServiceRecord!](iobluetoothdevice/getservicerecord(for:).md)
  Search for a service record containing the given UUID.
- [func handsFreeAudioGatewayServiceRecord() -> IOBluetoothSDPServiceRecord!](iobluetoothdevice/handsfreeaudiogatewayservicerecord.md)
- [func handsFreeDeviceServiceRecord() -> IOBluetoothSDPServiceRecord!](iobluetoothdevice/handsfreedeviceservicerecord.md)
- [func isConnected() -> Bool](iobluetoothdevice/isconnected.md)
  Indicates whether a baseband connection to the device exists.
- [func isFavorite() -> Bool](iobluetoothdevice/isfavorite.md)
  Reports whether the target device is a favorite for the user.
- [func isIncoming() -> Bool](iobluetoothdevice/isincoming.md)
  Returns TRUE if the device connection was generated by the remote host.
- [func isPaired() -> Bool](iobluetoothdevice/ispaired.md)
  Returns whether the target device is paired.
- [func openConnection() -> IOReturn](iobluetoothdevice/openconnection.md)
  Create a baseband connection to the device.
- [func openConnection(Any!) -> IOReturn](iobluetoothdevice/openconnection(_:).md)
  Create a baseband connection to the device.
- [func openConnection(Any!, withPageTimeout: BluetoothHCIPageTimeout, authenticationRequired: Bool) -> IOReturn](iobluetoothdevice/openconnection(_:withpagetimeout:authenticationrequired:).md)
  Create a baseband connection to the device.
- [func openL2CAPChannelAsync(AutoreleasingUnsafeMutablePointer<IOBluetoothL2CAPChannel?>!, withPSM: BluetoothL2CAPPSM, delegate: Any!) -> IOReturn](iobluetoothdevice/openl2capchannelasync(_:withpsm:delegate:).md)
  Opens a new L2CAP channel to the target device. Returns immediately after starting the opening process.
- [func openL2CAPChannelAsync(AutoreleasingUnsafeMutablePointer<IOBluetoothL2CAPChannel?>!, withPSM: BluetoothL2CAPPSM, withConfiguration: [AnyHashable : Any]!, delegate: Any!) -> IOReturn](iobluetoothdevice/openl2capchannelasync(_:withpsm:withconfiguration:delegate:).md)
  Opens a new L2CAP channel to the target device. Returns immediately after starting the opening process.
- [func openL2CAPChannelSync(AutoreleasingUnsafeMutablePointer<IOBluetoothL2CAPChannel?>!, withPSM: BluetoothL2CAPPSM, delegate: Any!) -> IOReturn](iobluetoothdevice/openl2capchannelsync(_:withpsm:delegate:).md)
  Opens a new L2CAP channel to the target device. Returns only after the channel is opened.
- [func openL2CAPChannelSync(AutoreleasingUnsafeMutablePointer<IOBluetoothL2CAPChannel?>!, withPSM: BluetoothL2CAPPSM, withConfiguration: [AnyHashable : Any]!, delegate: Any!) -> IOReturn](iobluetoothdevice/openl2capchannelsync(_:withpsm:withconfiguration:delegate:).md)
  Opens a new L2CAP channel to the target device. Returns only after the channel is opened.
- [func openRFCOMMChannelAsync(AutoreleasingUnsafeMutablePointer<IOBluetoothRFCOMMChannel?>!, withChannelID: BluetoothRFCOMMChannelID, delegate: Any!) -> IOReturn](iobluetoothdevice/openrfcommchannelasync(_:withchannelid:delegate:).md)
  Opens a new RFCOMM channel to the target device. Returns immediately.
- [func openRFCOMMChannelSync(AutoreleasingUnsafeMutablePointer<IOBluetoothRFCOMMChannel?>!, withChannelID: BluetoothRFCOMMChannelID, delegate: Any!) -> IOReturn](iobluetoothdevice/openrfcommchannelsync(_:withchannelid:delegate:).md)
  Opens a new RFCOMM channel to the target device. Returns only once the channel is open or failed to open.
- [func performSDPQuery(Any!) -> IOReturn](iobluetoothdevice/performsdpquery(_:).md)
  Performs an SDP query on the target device.
- [func performSDPQuery(Any!, uuids: [Any]!) -> IOReturn](iobluetoothdevice/performsdpquery(_:uuids:).md)
  Performs an SDP query on the target device with the specified service UUIDs.
- [func rawRSSI() -> BluetoothHCIRSSIValue](iobluetoothdevice/rawrssi.md)
  Get the raw RSSI device (if connected).
- [func recentAccessDate() -> Date!](iobluetoothdevice/recentaccessdate.md)
  Returns the date/time of the most recent access of the target device.
- [func register(forDisconnectNotification: Any!, selector: Selector!) -> IOBluetoothUserNotification!](iobluetoothdevice/register(fordisconnectnotification:selector:).md)
  Allows a client to register for device disconnect notification.
- [func remoteNameRequest(Any!) -> IOReturn](iobluetoothdevice/remotenamerequest(_:).md)
  Issues a remote name request to the target device.
- [func remoteNameRequest(Any!, withPageTimeout: BluetoothHCIPageTimeout) -> IOReturn](iobluetoothdevice/remotenamerequest(_:withpagetimeout:).md)
  Issues a remote name request to the target device.
- [func removeFromFavorites() -> IOReturn](iobluetoothdevice/removefromfavorites.md)
  Removes the target device from the user’s favorite devices list.
- [func requestAuthentication() -> IOReturn](iobluetoothdevice/requestauthentication.md)
  Requests that the existing baseband connection be authenticated.
- [func rssi() -> BluetoothHCIRSSIValue](iobluetoothdevice/rssi.md)
  Get the RSSI device (if connected), above or below the golden range. If the RSSI is within the golden range, a value of 0 is returned. For the actual RSSI value, use getRawRSSI. For more information, see the Bluetooth 4.0 Core Specification.
- [func sendL2CAPEchoRequest(UnsafeMutableRawPointer!, length: UInt16) -> IOReturn](iobluetoothdevice/sendl2capechorequest(_:length:).md)
  Send an echo request over the L2CAP connection to a remote device.
- [func setSupervisionTimeout(UInt16) -> IOReturn](iobluetoothdevice/setsupervisiontimeout(_:).md)
  Sets the connection supervision timeout.
### Type Methods
- [class func favoriteDevices() -> [Any]!](iobluetoothdevice/favoritedevices.md)
  Gets an array of the user’s favorite devices.
- [class func pairedDevices() -> [Any]!](iobluetoothdevice/paireddevices.md)
  Gets an array of all of the paired devices on the system.
- [class func recentDevices(UInt) -> [Any]!](iobluetoothdevice/recentdevices(_:).md)
  Gets an array of recently used Bluetooth devices.
- [class func register(forConnectNotifications: Any!, selector: Selector!) -> IOBluetoothUserNotification!](iobluetoothdevice/register(forconnectnotifications:selector:).md)
  Allows a client to register for device connect notifications for any connection.

## Relationships

### Inherits From
- [IOBluetoothObject](iobluetoothobject.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

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
- [class IOBluetoothSDPDataElement](iobluetoothsdpdataelement.md)
  An instance of this class represents a single SDP data element as defined by the Bluetooth SDP spec.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice)*