# IOBluetoothNSStringFromDeviceAddress(_:)

**Framework**: IOBluetooth  
**Kind**: func  
**Role**: Function

Convenience routine to take a device address structure and create an NSString.

**Availability**:
- macOS

## Declaration

```swift
func IOBluetoothNSStringFromDeviceAddress(_ deviceAddress: UnsafePointer<BluetoothDeviceAddress>!) -> String!
```

```c
extern NSString *IOBluetoothNSStringFromDeviceAddress(const BluetoothDeviceAddress *deviceAddress);
```

## Return Value

Returns the created address string.

## Discussion

The resultant string will be in this format: “00-11-22-33-44-55”

## Parameters

- `deviceAddress`: A valid bluetooth device structure.

## See Also

### Miscellaneous
- [func IOBluetoothFindNumberOfRegistryEntriesOfClassName(UnsafePointer<CChar>!) -> Int](./iobluetoothfindnumberofregistryentriesofclassname%28_%29.md)
  The number of registry entries with a device classname.
- [func IOBluetoothGetUniqueFileNameAndPath(String!, String!) -> String!](./iobluetoothgetuniquefilenameandpath%28_,_%29.md)
- [func IOBluetoothIsFileAppleDesignatedPIMData(String!) -> Bool](./iobluetoothisfileappledesignatedpimdata%28_%29.md)
  Apple designated PIM data is classified as: .vcard, .vcal, .vcf, .vnote, .vmsg, .vcs
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

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothnsstringfromdeviceaddress(_:))*