# IOBluetoothGetUniqueFileNameAndPath(_:_:)

**Framework**: IOBluetooth  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS

## Declaration

```swift
func IOBluetoothGetUniqueFileNameAndPath(_ inName: String!, _ inPath: String!) -> String!
```

```c
extern NSString *IOBluetoothGetUniqueFileNameAndPath(NSString *inName, NSString *inPath);
```

#### Return Value

String with a unique name appended on it for the provided path.

#### Discussion

When passed a VALID filename and a VALID path, this routine will return you a the path with the name appended onto it. If it already exist, it will insert a #1, #2, etc. Example: If you pass @“TestFile.txt” and @”~/Documents”, you will get @“~Documents/TestFile.txt”. If one already exists, you will be returned: @“~Documents/TestFile #1.txt”.

## Parameters

- `inName`: Name of file that needs unique name in the specified path.
- `inPath`: Path you are trying to put file into.

## See Also

### Miscellaneous
- [func IOBluetoothFindNumberOfRegistryEntriesOfClassName(UnsafePointer<CChar>!) -> Int](./iobluetoothfindnumberofregistryentriesofclassname%28_%29.md)
  The number of registry entries with a device classname.
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
- [IOBluetoothPackData](./iobluetoothpackdata.md)
  Packs a variable amount of parameters into a buffer according to a printf-style format string.
- [IOBluetoothUnpackData](./iobluetoothunpackdata.md)
  Unpacks a variable amount of data from a buffer into a variable number of parameters according to a printf-style format string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothgetuniquefilenameandpath(_:_:))*