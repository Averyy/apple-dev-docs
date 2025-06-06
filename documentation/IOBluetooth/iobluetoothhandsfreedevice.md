# IOBluetoothHandsFreeDevice

**Framework**: IOBluetooth  
**Kind**: class

An object you use to manage phone calls on a connected Bluetooth hands-free phone or headset.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class IOBluetoothHandsFreeDevice
```

## Topics

### Creating a Hands-Free Device Manager
- [init!(device: IOBluetoothDevice!, delegate: Any!)](iobluetoothhandsfreedevice/init(device:delegate:).md)
  Creates an object to manage phone calls on a hands-free Bluetooth device.
### Accepting Calls
- [func acceptCall()](iobluetoothhandsfreedevice/acceptcall.md)
  Accepts an incoming call.
- [func acceptCallOnPhone()](iobluetoothhandsfreedevice/acceptcallonphone.md)
  Accepts an incoming call and transfers the audio to the managed hands-free phone or headset.
- [func callTransfer()](iobluetoothhandsfreedevice/calltransfer.md)
  Ends all calls that are active or on hold, and accepts any waiting calls.
### Dialing Calls
- [func dialNumber(String!)](iobluetoothhandsfreedevice/dialnumber(_:).md)
  Calls the phone number on a hands-free phone or headset.
- [func memoryDial(Int32)](iobluetoothhandsfreedevice/memorydial(_:).md)
  Calls the phone number stored in a speed dial or memory slot of the hands-free phone or headset.
- [func redial()](iobluetoothhandsfreedevice/redial.md)
  Calls the number stored on the hands-free phone or headset again.
### Holding Calls
- [func holdCall()](iobluetoothhandsfreedevice/holdcall.md)
  Places all active calls on hold and accepts a held or waiting call.
- [func addHeldCall()](iobluetoothhandsfreedevice/addheldcall.md)
  Adds held calls to the current conversation.
- [func placeAllOthers(onHold: Int32)](iobluetoothhandsfreedevice/placeallothers(onhold:).md)
  Places all calls except the call with the specified index on hold.
### Ending Calls
- [func endCall()](iobluetoothhandsfreedevice/endcall.md)
  Ends the current call or refuses an incoming call.
- [func releaseCall(Int32)](iobluetoothhandsfreedevice/releasecall(_:).md)
  Ends the call with the specified index.
- [func releaseActiveCalls()](iobluetoothhandsfreedevice/releaseactivecalls.md)
  Ends all active calls and accepts a held or waiting call.
- [func releaseHeldCalls()](iobluetoothhandsfreedevice/releaseheldcalls.md)
  Ends all calls that are on hold or returns a busy signal for a waiting call.
### Sending Messages and Commands
- [func sendSMS(String!, message: String!)](iobluetoothhandsfreedevice/sendsms(_:message:).md)
  Sends a text message to a phone number.
- [func sendDTMF(String!)](iobluetoothhandsfreedevice/senddtmf(_:).md)
  Sends the tone associated with a phone key to the hands-free Bluetooth device.
- [func send(atCommand: String!)](iobluetoothhandsfreedevice/send(atcommand:).md)
  Sends an AT command to the Bluetooth audio gateway.
- [func send(atCommand: String!, timeout: Float, selector: Selector!, target: Any!)](iobluetoothhandsfreedevice/send(atcommand:timeout:selector:target:).md)
  Send an AT command to the Bluetooth audio gateway and performs a selector on completion or timeout.
### Requesting Status Information
- [func subscriberNumber()](iobluetoothhandsfreedevice/subscribernumber.md)
  Requests that the Bluetooth audio gateway send the subscriber number to the delegate.
- [func currentCallList()](iobluetoothhandsfreedevice/currentcalllist.md)
  Requests that the Bluetooth audio gateway send the delegate a list of calls that are active, on hold, or being set up.
### Transferring Audio
- [func transferAudioToComputer()](iobluetoothhandsfreedevice/transferaudiotocomputer.md)
  Moves the audio for current and future calls to a Mac.
- [func transferAudioToPhone()](iobluetoothhandsfreedevice/transferaudiotophone.md)
  Moves the audio for current or future calls to a phone.

## Relationships

### Inherits From
- [IOBluetoothHandsFree](iobluetoothhandsfree.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice)*