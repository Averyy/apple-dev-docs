# IOBluetoothDeviceInquiry

**Framework**: IOBluetooth  
**Kind**: class  
**Role**: Class

Object representing a device inquiry that finds Bluetooth devices in-range of the computer, and (optionally) retrieves name information for them.

**Availability**:
- macOS

## Declaration

```swift
class IOBluetoothDeviceInquiry
```

```objc
@interface IOBluetoothDeviceInquiry : NSObject
```

#### Overview

You should only use this object if your application needs to know about in-range devices and cannot use the GUI provided by the IOBluetoothUI framework. It will not let you perform unlimited back-to-back inquiries, but will instead throttle the number of attempted inquiries if too many are attempted within a small window of time. Important Note: DO NOT perform remote name requests on devices from delegate methods or while this object is in use. If you wish to do your own remote name requests on devices, do them after you have stopped this object. If you do not heed this warning, you could potentially deadlock your process.

## Topics

### Initializers
- [init!(delegate: Any!)](./iobluetoothdeviceinquiry/init%28delegate%29.md)
  Initializes an alloc’d inquiry object, and sets the delegate object, as if -setDelegate: were called on it.
### Instance Properties
- [var delegate: AnyObject?](./iobluetoothdeviceinquiry/delegate.md)
- [var inquiryLength: UInt8](./iobluetoothdeviceinquiry/inquirylength.md)
  Set the length of the inquiry that is performed each time -start is used on an inquiry object.
- [var searchType: IOBluetoothDeviceSearchTypes](./iobluetoothdeviceinquiry/searchtype.md)
  Set the devices that are found.
- [var updateNewDeviceNames: Bool](./iobluetoothdeviceinquiry/updatenewdevicenames.md)
  Sets whether or not the inquiry object will retrieve the names of devices found during the search.
### Instance Methods
- [func clearFoundDevices()](./iobluetoothdeviceinquiry/clearfounddevices%28%29.md)
  Removes all found devices from the inquiry object.
- [func foundDevices() -> [Any]!](./iobluetoothdeviceinquiry/founddevices%28%29.md)
  Returns found IOBluetoothDevice objects as an array.
- [func setSearchCriteria(BluetoothServiceClassMajor, majorDeviceClass: BluetoothDeviceClassMajor, minorDeviceClass: BluetoothDeviceClassMinor)](./iobluetoothdeviceinquiry/setsearchcriteria%28_,majordeviceclass,minordeviceclass%29.md)
  Use this method to set the criteria for the device search.
- [func start() -> IOReturn](./iobluetoothdeviceinquiry/start%28%29.md)
  Tells inquiry object to begin the inquiry and name updating process, if specified.
- [func stop() -> IOReturn](./iobluetoothdeviceinquiry/stop%28%29.md)
  Halts the inquiry object. Could either stop the search for new devices, or the updating of found device names.

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

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdeviceinquiry)*