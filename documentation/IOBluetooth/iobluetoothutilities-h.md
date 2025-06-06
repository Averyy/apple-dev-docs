# IOBluetoothUtilities.h

**Framework**: IOBluetooth

See the Overview section above for header-level documentation.

###### Included Headers

- <stdio.h>
- <stdlib.h>
- <string.h>
- <sysexits.h>
- <sys/errno.h>
- <unistd.h>
- <IOBluetooth/Bluetooth.h>
- <IOKit/IOReturn.h>
- <IOBluetooth/IOBluetoothUserLib.h>

## Topics

### Miscellaneous
- [func IOBluetoothFindNumberOfRegistryEntriesOfClassName(UnsafePointer<CChar>!) -> Int](iobluetoothfindnumberofregistryentriesofclassname(_:).md)
  The number of registry entries with a device classname.
- [func IOBluetoothGetUniqueFileNameAndPath(String!, String!) -> String!](iobluetoothgetuniquefilenameandpath(_:_:).md)
- [func IOBluetoothIsFileAppleDesignatedPIMData(String!) -> Bool](iobluetoothisfileappledesignatedpimdata(_:).md)
  Apple designated PIM data is classified as: .vcard, .vcal, .vcf, .vnote, .vmsg, .vcs
- [func IOBluetoothNSStringFromDeviceAddress(UnsafePointer<BluetoothDeviceAddress>!) -> String!](iobluetoothnsstringfromdeviceaddress(_:).md)
  Convenience routine to take a device address structure and create an NSString.
- [func IOBluetoothNSStringToDeviceAddress(String!, UnsafeMutablePointer<BluetoothDeviceAddress>!) -> IOReturn](iobluetoothnsstringtodeviceaddress(_:_:).md)
  Convenience routine to take an NSString and turn it into a BluetoothDeviceAddress structure.
- [func IOBluetoothNumberOfAvailableHIDDevices() -> Int](iobluetoothnumberofavailablehiddevices().md)
  Returns total number of HID devices on the system (Bluetooth + USB)
- [func IOBluetoothNumberOfKeyboardHIDDevices() -> Int](iobluetoothnumberofkeyboardhiddevices().md)
  Returns number of keyboard HID devices on the system (Bluetooth + USB)
- [func IOBluetoothNumberOfPointingHIDDevices() -> Int](iobluetoothnumberofpointinghiddevices().md)
  Returns number of “pointing” HID devices on the system (Bluetooth + USB)
- [func IOBluetoothNumberOfTabletHIDDevices() -> Int](iobluetoothnumberoftablethiddevices().md)
  Returns number of “Tablet” HID devices on the system (Bluetooth + USB)

## See Also

- [Bluetooth.h User-Space](bluetooth-h-user-space.md)
  Bluetooth wireless technology
- [IOBluetoothUserLib.h](iobluetoothuserlib-h.md)
  Public Interfaces for Apple’s implementation of Bluetooth technology.
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

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothutilities-h)*