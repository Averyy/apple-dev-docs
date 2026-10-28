# OBEXFileTransferServices

**Framework**: IOBluetooth  
**Kind**: class  
**Role**: Class

Implements advanced OBEX operations in addition to simple PUT and GET.

**Availability**:
- macOS

## Declaration

```swift
class OBEXFileTransferServices
```

```objc
@interface OBEXFileTransferServices : NSObject
```

## Overview

All operations are asynchronous and will callback over a respective delegate method if the initial return value is successful. The initial return value usually concerns the state of this object where as the delegate return value reflects the response of the remote device.

## Topics

### Initializers
- [init!(obexSession: IOBluetoothOBEXSession!)](./obexfiletransferservices/init%28obexsession%29-8xm7d.md)
  Create a new OBEXFileTransferServices object
- [init!(OBEXSession: IOBluetoothOBEXSession!)](./obexfiletransferservices/init%28obexsession%29-8au7l.md)
### Instance Properties
- [var delegate: AnyObject!](./obexfiletransferservices/delegate.md)
### Instance Methods
- [func abort() -> OBEXError](./obexfiletransferservices/abort%28%29.md)
  Abort the current operation
- [func changeCurrentFolderBackward() -> OBEXError](./obexfiletransferservices/changecurrentfolderbackward%28%29.md)
  Change to the directory above the current level if not at the root
- [func changeCurrentFolderForward(toPath: String!) -> OBEXError](./obexfiletransferservices/changecurrentfolderforward%28topath%29.md)
  Change the remote path
- [func changeCurrentFolderToRoot() -> OBEXError](./obexfiletransferservices/changecurrentfoldertoroot%28%29.md)
  Asynchronously change to the remote root directory
- [func connectToFTPService() -> OBEXError](./obexfiletransferservices/connecttoftpservice%28%29.md)
  Connect to a remote device for FTP operations
- [func connectToObjectPushService() -> OBEXError](./obexfiletransferservices/connecttoobjectpushservice%28%29.md)
  Connect to a remote device for ObjectPush operations. Most of the FTP functionality of this object will be disabled.
- [func copyRemoteFile(String!, toLocalPath: String!) -> OBEXError](./obexfiletransferservices/copyremotefile%28_,tolocalpath%29.md)
  Copy a remote file to a local path
- [func createFolder(String!) -> OBEXError](./obexfiletransferservices/createfolder%28_%29.md)
  Create a folder on the remote target
- [func currentPath() -> String!](./obexfiletransferservices/currentpath%28%29.md)
  Get the remote current directory path during an FTP session
- [func disconnect() -> OBEXError](./obexfiletransferservices/disconnect%28%29.md)
  Disconnect from the remote device
- [func getDefaultVCard(String!) -> OBEXError](./obexfiletransferservices/getdefaultvcard%28_%29.md)
  Get the remote default VCard, if it is supported
- [func isBusy() -> Bool](./obexfiletransferservices/isbusy%28%29.md)
  Get the action state of the module
- [func isConnected() -> Bool](./obexfiletransferservices/isconnected%28%29.md)
  Get the connected state of this module.
- [func removeItem(String!) -> OBEXError](./obexfiletransferservices/removeitem%28_%29.md)
  Remove a remote item.
- [func retrieveFolderListing() -> OBEXError](./obexfiletransferservices/retrievefolderlisting%28%29.md)
  Get a remote directory listing
- [func send(Data!, type: String!, name: String!) -> OBEXError](./obexfiletransferservices/send%28_,type,name%29.md)
  Send data to a remote target
- [func sendFile(String!) -> OBEXError](./obexfiletransferservices/sendfile%28_%29.md)
  Put a local file to the remote target
### Type Methods
- [class func withOBEXSession(IOBluetoothOBEXSession!) -> Self!](./obexfiletransferservices/withobexsession%28_%29.md)
  Create a new OBEXFileTransferServices object
### Instance Variables
- [mAbortedByOwner](./obexfiletransferservices/mabortedbyowner.md)
- [mActionArgument1](./obexfiletransferservices/mactionargument1.md)
- [mActionArgument2](./obexfiletransferservices/mactionargument2.md)
- [mActionArgument3](./obexfiletransferservices/mactionargument3.md)
- [mActionCommand](./obexfiletransferservices/mactioncommand.md)
- [mActionInProgress](./obexfiletransferservices/mactioninprogress.md)
- [mConnectionID](./obexfiletransferservices/mconnectionid.md)
- [mCurrentRemoteDirectory](./obexfiletransferservices/mcurrentremotedirectory.md)
- [mDelegate](./obexfiletransferservices/mdelegate.md)
- [mFolderListingFileRef](./obexfiletransferservices/mfolderlistingfileref.md)
- [mGETProgress](./obexfiletransferservices/mgetprogress.md)
- [mHasTargetHeader](./obexfiletransferservices/mhastargetheader.md)
- [mInactivityTimer](./obexfiletransferservices/minactivitytimer.md)
- [mMaxPacketLength](./obexfiletransferservices/mmaxpacketlength.md)
- [mOBEXFileGet](./obexfiletransferservices/mobexfileget.md)
- [mOBEXFilePut](./obexfiletransferservices/mobexfileput.md)
- [mOBEXSession](./obexfiletransferservices/mobexsession.md)
- [mPUTProgress](./obexfiletransferservices/mputprogress.md)
- [mReserved1](./obexfiletransferservices/mreserved1.md)
- [mReserved2](./obexfiletransferservices/mreserved2.md)
- [mSavedCommand](./obexfiletransferservices/msavedcommand.md)
- [mWeAreAborting](./obexfiletransferservices/mweareaborting.md)
- [mWeOpenedTheOBEXConnection](./obexfiletransferservices/mweopenedtheobexconnection.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices)*