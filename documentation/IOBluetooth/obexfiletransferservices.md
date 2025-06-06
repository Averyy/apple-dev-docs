# OBEXFileTransferServices

**Framework**: IOBluetooth  
**Kind**: class

Implements advanced OBEX operations in addition to simple PUT and GET.

**Availability**:
- macOS ?+

## Declaration

```swift
class OBEXFileTransferServices
```

#### Overview

All operations are asynchronous and will callback over a respective delegate method if the initial return value is successful. The initial return value usually concerns the state of this object where as the delegate return value reflects the response of the remote device.

## Topics

### Initializers
- [init!(obexSession: IOBluetoothOBEXSession!)](obexfiletransferservices/init(obexsession:).md)
  Create a new OBEXFileTransferServices object
### Instance Properties
- [var delegate: AnyObject!](obexfiletransferservices/delegate.md)
### Instance Methods
- [func abort() -> OBEXError](obexfiletransferservices/abort.md)
  Abort the current operation
- [func changeCurrentFolderBackward() -> OBEXError](obexfiletransferservices/changecurrentfolderbackward.md)
  Change to the directory above the current level if not at the root
- [func changeCurrentFolderForward(toPath: String!) -> OBEXError](obexfiletransferservices/changecurrentfolderforward(topath:).md)
  Change the remote path
- [func changeCurrentFolderToRoot() -> OBEXError](obexfiletransferservices/changecurrentfoldertoroot.md)
  Asynchronously change to the remote root directory
- [func connectToFTPService() -> OBEXError](obexfiletransferservices/connecttoftpservice.md)
  Connect to a remote device for FTP operations
- [func connectToObjectPushService() -> OBEXError](obexfiletransferservices/connecttoobjectpushservice.md)
  Connect to a remote device for ObjectPush operations. Most of the FTP functionality of this object will be disabled.
- [func copyRemoteFile(String!, toLocalPath: String!) -> OBEXError](obexfiletransferservices/copyremotefile(_:tolocalpath:).md)
  Copy a remote file to a local path
- [func createFolder(String!) -> OBEXError](obexfiletransferservices/createfolder(_:).md)
  Create a folder on the remote target
- [func currentPath() -> String!](obexfiletransferservices/currentpath.md)
  Get the remote current directory path during an FTP session
- [func disconnect() -> OBEXError](obexfiletransferservices/disconnect.md)
  Disconnect from the remote device
- [func getDefaultVCard(String!) -> OBEXError](obexfiletransferservices/getdefaultvcard(_:).md)
  Get the remote default VCard, if it is supported
- [func isBusy() -> Bool](obexfiletransferservices/isbusy.md)
  Get the action state of the module
- [func isConnected() -> Bool](obexfiletransferservices/isconnected.md)
  Get the connected state of this module.
- [func removeItem(String!) -> OBEXError](obexfiletransferservices/removeitem(_:).md)
  Remove a remote item.
- [func retrieveFolderListing() -> OBEXError](obexfiletransferservices/retrievefolderlisting.md)
  Get a remote directory listing
- [func send(Data!, type: String!, name: String!) -> OBEXError](obexfiletransferservices/send(_:type:name:).md)
  Send data to a remote target
- [func sendFile(String!) -> OBEXError](obexfiletransferservices/sendfile(_:).md)
  Put a local file to the remote target
### Type Methods
- [class func withOBEXSession(IOBluetoothOBEXSession!) -> Self!](obexfiletransferservices/withobexsession(_:).md)
  Create a new OBEXFileTransferServices object

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices)*