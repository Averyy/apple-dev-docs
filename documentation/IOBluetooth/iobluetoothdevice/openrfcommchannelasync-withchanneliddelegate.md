# openRFCOMMChannelAsync(_:withChannelID:delegate:)

**Framework**: IOBluetooth  
**Kind**: method

Opens a new RFCOMM channel to the target device. Returns immediately.

**Availability**:
- macOS ?+

## Declaration

```swift
func openRFCOMMChannelAsync(_ rfcommChannel: AutoreleasingUnsafeMutablePointer<IOBluetoothRFCOMMChannel?>!, withChannelID channelID: BluetoothRFCOMMChannelID, delegate channelDelegate: Any!) -> IOReturn
```

#### Return Value

Returns kIOReturnSuccess if the open process was successfully started (or if an existing RFCOMM channel was found). The channel must be released when the caller is done with it.

#### Discussion

This method will begin the process of opening a new RFCOMM channel to the target device. The baseband connection to the device will be opened if it is not open already. The RFCOMM channel open process will not complete until the client has registered an incoming data listener on the new channel. The RFCOMM channel object is already retained when this function returns success; the channel must be released when the caller is done with it.

You should verify that the channel you wish to open exists on the remote device before attempting to open it, by performing an SDP query. This is recommended because the service might have been removed from the, remote device or the channel assignments for the service could have changed (this is rare, but it does happen frequently on some devices). This also works around a bug that existed in early Leopard versions in certain situations where the method would return an error; in these instances, the desired RFCOMM channel could not be opened again until the calling app was restarted.

NOTE: This method is only available in macOS 10.2.5 (Bluetooth v1.2) or later.

## Parameters

- `rfcommChannel`: A pointer to an IOBluetoothRFCOMMChannel object to receive the RFCOMM channel requested to be opened. The rfcommChannel pointer will only be set if kIOReturnSuccess is returned.
- `channelID`: The RFCOMM channel ID for the new channel.
- `channelDelegate`: The object that will play the role of delegate for the channel. A channel delegate is the object the rfcomm uses as target for data and events. The developer will implement only the the methods he/she is interested in. A list of the possible methods is at the end of the file “IOBluetoothRFCOMMChannel.h” in the definition of the protocol IOBluetoothRFCOMMChannelDelegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/openrfcommchannelasync(_:withchannelid:delegate:))*