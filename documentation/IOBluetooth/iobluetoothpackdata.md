# IOBluetoothPackData

**Framework**: IOBluetooth  
**Kind**: func  
**Role**: Function

Packs a variable amount of parameters into a buffer according to a printf-style format string.

**Availability**:
- macOS

## Declaration

```c
extern long IOBluetoothPackData(void *ioBuffer, const char *inFormat, ...);
```

#### Return Value

Number of bytes packed or -1 if an error occurred.

#### Discussion

Pass the parameters to send data as the remaining arguments after the format string.

Supported format characters:

```objc
 
   	'b' 1 byte of data ('b'yte)
   	'h' 2 bytes of data ('h'alf-word)
   	'H' 2 bytes of data ('h'alf-word) to byte reverse.
   	't' 3 bytes of data ('t'riple byte, least significant 24-bits).
   	'T' 3 bytes of data ('t'riple byte, least significant 24-bits) to byte reverse.
   	'w' 4 bytes of data ('w'ord).
   	'W' 4 bytes of data ('w'ord) to byte reverse.
   	'1'	Ptr to 1 byte of data.
   	'2' Ptr to 2 bytes of data.
   	'@'	(shift-2) Ptr to 2 bytes of data to byte reverse.
   	'3' Ptr to 3 bytes of data.
   	'#'	(shift-3) Ptr to 3 bytes of data to byte reverse.
   	'4' Ptr to 4 bytes of data.
   	'$'	(shift-4) Ptr to 4 bytes of data to byte reverse.
   	'5' Ptr to 5 bytes of data.
   	'%'	(shift-5) Ptr to 5 bytes of data to byte reverse.
   	'6' Ptr to 6 bytes of data.
   	'^'	(shift-6) Ptr to 6 bytes of data to byte reverse.
   	'7' Ptr to 6 bytes of data.
   	'&'	(shift-7) Ptr to 7 bytes of data to byte reverse.
   	'8' Ptr to 6 bytes of data.
   	'*'	(shift-8) Ptr to 8 bytes of data to byte reverse.
   	'9' Ptr to 6 bytes of data.
   	'('	(shift-9) Ptr to 9 bytes of data to byte reverse.
   	'n' Ptr to n bytes of data (first param is size, second is ptr).
   	'N' Ptr to n bytes of data to byte reverse (first param is size, second is ptr).
   	's' Ptr to C-string (includes null terminator)
   	'p' Ptr to Pascal-string (includes length byte).
 
```

Example usage:

```objc
 
   	bytesPacked = PackData( buffer, "bts", 'U', 'XYZ', "This is a C-style string" );
 
```

**Warning:** *Raw values packed with ‘b’, ‘h’, ‘t’, and ‘w’ have their bytes packed into the buffer from left to right even on little-endian systems. For example, the value 0x12345678 would be sent out as 0x12 0x34 0x56 0x78. This needs to be taken into consideration if the value is expected to be in little-endian format in the buffer. This case requires you byte swap the value on all systems before sending it to this routine.*

## Parameters

- `ioBuffer`: Ptr to buffer to receive packed data.
- `inFormat`: Printf-Style format string controlling how the data is packed.

## See Also

### Miscellaneous
- [func IOBluetoothFindNumberOfRegistryEntriesOfClassName(UnsafePointer<CChar>!) -> Int](./iobluetoothfindnumberofregistryentriesofclassname%28_%29.md)
  The number of registry entries with a device classname.
- [func IOBluetoothGetUniqueFileNameAndPath(String!, String!) -> String!](./iobluetoothgetuniquefilenameandpath%28_,_%29.md)
- [func IOBluetoothIsFileAppleDesignatedPIMData(String!) -> Bool](./iobluetoothisfileappledesignatedpimdata%28_%29.md)
  Apple designated PIM data is classified as: .vcard, .vcal, .vcf, .vnote, .vmsg, .vcs
- [func IOBluetoothNSStringFromDeviceAddress(UnsafePointer<BluetoothDeviceAddress>!) -> String!](./iobluetoothnsstringfromdeviceaddress%28_%29.md)
  Convenience routine to take a device address structure and create an NSString.
- [func IOBluetoothNSStringToDeviceAddress(String!, UnsafeMutablePointer<BluetoothDeviceAddress>!) -> IOReturn](./iobluetoothnsstringtodeviceaddress%28_,_%29.md)
  Convenience routine to take an NSString and turn it into a BluetoothDeviceAddress structure.
- [func IOBluetoothNumberOfAvailableHIDDevices() -> Int](./iobluetoothnumberofavailablehiddevices%28%29.md)
  Returns total number of HID devices on the system (Bluetooth + USB)
- [func IOBluetoothNumberOfKeyboardHIDDevices() -> Int](./iobluetoothnumberofkeyboardhiddevices%28%29.md)
  Returns number of keyboard HID devices on the system (Bluetooth + USB)
- [func IOBluetoothNumberOfPointingHIDDevices() -> Int](./iobluetoothnumberofpointinghiddevices%28%29.md)
  Returns number of “pointing” HID devices on the system (Bluetooth + USB)
- [func IOBluetoothNumberOfTabletHIDDevices() -> Int](./iobluetoothnumberoftablethiddevices%28%29.md)
  Returns number of “Tablet” HID devices on the system (Bluetooth + USB)
- [IOBluetoothUnpackData](./iobluetoothunpackdata.md)
  Unpacks a variable amount of data from a buffer into a variable number of parameters according to a printf-style format string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothpackdata)*