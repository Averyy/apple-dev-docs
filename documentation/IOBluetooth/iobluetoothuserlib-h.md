# IOBluetoothUserLib.h

**Framework**: IOBluetooth

Public Interfaces for Apple’s implementation of Bluetooth technology.

#### Overview

There is an accompanying header to this, “Bluetooth.h”, which contains all technology-specific typedefs and information. This header relies heavily on it.

##### Included Headers

- <IOKit/IOKitLib.h>
- <CoreFoundation/CFMachPort.h>
- <IOBluetooth/Bluetooth.h>
- <Foundation/Foundation.h>

## Topics

### Miscellaneous
- [func IOBluetoothIgnoreHIDDevice(IOBluetoothDeviceRef!)](iobluetoothignorehiddevice(_:).md)
  Hints that the macOS Bluetooth software should ignore a HID device that connects up.
- [func IOBluetoothL2CAPChannelRegisterForChannelCloseNotification(IOBluetoothL2CAPChannelRef!, IOBluetoothUserNotificationCallback!, UnsafeMutableRawPointer!) -> Unmanaged<IOBluetoothUserNotificationRef>!](iobluetoothl2capchannelregisterforchannelclosenotification(_:_:_:).md)
  Allows a client to register for a channel close notification.
- [func IOBluetoothRemoveIgnoredHIDDevice(IOBluetoothDeviceRef!)](iobluetoothremoveignoredhiddevice(_:).md)
  The counterpart to the above IOBluetoothIgnoreHIDDevice() API.
- [func IOBluetoothUserNotificationUnregister(IOBluetoothUserNotificationRef!)](iobluetoothusernotificationunregister(_:).md)
  Unregisters the target notification.
### Callbacks
- [typealias IOBluetoothUserNotificationCallback](iobluetoothusernotificationcallback.md)
  Callback function definition for user notifications.
### Data Types
- [typealias IOBluetoothDeviceSearchOptions](iobluetoothdevicesearchoptions.md)
- [struct IOBluetoothDeviceSearchAttributes](iobluetoothdevicesearchattributes.md)
  Structure used to search for particular devices.
- [struct IOBluetoothDeviceSearchDeviceAttributes](iobluetoothdevicesearchdeviceattributes.md)
  Structure used to search for particular devices.
### Constants
- [struct IOBluetoothDeviceSearchDeviceAttributes](iobluetoothdevicesearchdeviceattributes.md)
  Structure used to search for particular devices.
- [struct IOBluetoothDeviceSearchTypesBits](iobluetoothdevicesearchtypesbits.md)
  Bits to determine what Bluetooth devices to search for

## See Also

- [Bluetooth.h User-Space](bluetooth-h-user-space.md)
  Bluetooth wireless technology
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothuserlib-h)*