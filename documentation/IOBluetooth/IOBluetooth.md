# IOBluetooth

**Framework**: IOBluetooth  
**Kind**: module

Gain user-space access to Bluetooth devices.

**Availability**:
- macOS 10.2+

#### Overview

The Bluetooth framework supports user-space access to Bluetooth devices, including both C and Objective-C APIs.

## Topics

### Classes
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
- [class IOBluetoothSDPDataElement](iobluetoothsdpdataelement.md)
  An instance of this class represents a single SDP data element as defined by the Bluetooth SDP spec.
- [class IOBluetoothSDPDataElementRef](iobluetoothsdpdataelementref.md)
- [class IOBluetoothSDPServiceAttribute](iobluetoothsdpserviceattribute.md)
  IOBluetoothSDPServiceAttribute represents a single SDP service attribute.
- [class IOBluetoothSDPServiceRecord](iobluetoothsdpservicerecord.md)
  An instance of this class represents a single SDP service record.
- [class IOBluetoothSDPServiceRecordRef](iobluetoothsdpservicerecordref.md)
- [class IOBluetoothSDPUUID](iobluetoothsdpuuid.md)
  An NSData subclass that represents a UUID as defined in the Bluetooth SDP spec.
- [class IOBluetoothSDPUUIDRef](iobluetoothsdpuuidref.md)
- [class IOBluetoothUserNotification](iobluetoothusernotification.md)
  Represents a registered notification.
- [class IOBluetoothUserNotificationRef](iobluetoothusernotificationref.md)
- [class OBEXFileTransferServices](obexfiletransferservices.md)
  Implements advanced OBEX operations in addition to simple PUT and GET.
- [class OBEXSession](obexsession.md)
  Object representing an OBEX connection to a remote target.
### Protocols
- [protocol IOBluetoothDeviceAsyncCallbacks](iobluetoothdeviceasynccallbacks.md)
- [protocol IOBluetoothDeviceInquiryDelegate](iobluetoothdeviceinquirydelegate.md)
  This category on NSObject describes the delegate methods for the IOBluetoothDeviceInquiry object. All methods are optional, but it is highly recommended you implement them all. Do NOT invoke remote name requests on found IOBluetoothDevice objects unless the inquiry object has been stopped. Doing so may deadlock your process.
- [protocol IOBluetoothDevicePairDelegate](iobluetoothdevicepairdelegate.md)
- [protocol IOBluetoothHandsFreeAudioGatewayDelegate](iobluetoothhandsfreeaudiogatewaydelegate.md)
  A set of optional methods for receiving information about status changes for a connected Bluetooth hands-free phone or headset.
- [protocol IOBluetoothHandsFreeDelegate](iobluetoothhandsfreedelegate.md)
- [protocol IOBluetoothHandsFreeDeviceDelegate](iobluetoothhandsfreedevicedelegate.md)
  A set of optional methods for receiving status change updates and information about a connected Bluetooth hands-free phone or headset.
- [protocol IOBluetoothL2CAPChannelDelegate](iobluetoothl2capchanneldelegate.md)
- [protocol IOBluetoothRFCOMMChannelDelegate](iobluetoothrfcommchanneldelegate.md)
### Reference
- [Bluetooth.h User-Space](bluetooth-h-user-space.md)
  Bluetooth wireless technology
- [IOBluetoothUserLib.h](iobluetoothuserlib-h.md)
  Public Interfaces for Apple’s implementation of Bluetooth technology.
- [IOBluetoothUtilities.h](iobluetoothutilities-h.md)
  See the Overview section above for header-level documentation.
- [OBEX.h](obex-h.md)
  Public OBEX technology interfaces.
- [OBEXBluetooth.h](obexbluetooth-h.md)
  Object Exchange over Bluetooth.
- [OBEXFileTransferServices.h](obexfiletransferservices-h.md)
- [IOBluetooth Structures](iobluetooth-structures.md)
- [IOBluetooth Enumerations](iobluetooth-enumerations.md)
- [IOBluetooth Constants](iobluetooth-constants.md)
- [IOBluetooth Functions](iobluetooth-functions.md)
- [IOBluetooth Data Types](iobluetooth-data-types.md)

## See Also

- [Bluetooth Device Access Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/Bluetooth/BT_Intro/BT_Intro.html#//apple_ref/doc/uid/TP30000997)


---

*[View on Apple Developer](https://developer.apple.com/documentation/IOBluetooth)*