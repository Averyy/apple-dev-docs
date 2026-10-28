# IOBluetoothNSStringToDeviceAddress(_:_:)

**Framework**: IOBluetooth  
**Kind**: func  
**Role**: Function

Convenience routine to take an NSString and turn it into a BluetoothDeviceAddress structure.

**Availability**:
- macOS

## Declaration

```swift
func IOBluetoothNSStringToDeviceAddress(_ inNameString: String!, _ outDeviceAddress: UnsafeMutablePointer<BluetoothDeviceAddress>!) -> IOReturn
```

```c
extern IOReturn IOBluetoothNSStringToDeviceAddress(NSString *inNameString, BluetoothDeviceAddress *outDeviceAddress);
```

## Return Value

Returns success (0) or failure code.

## Discussion

Pass in most types of strings, such as “001122334455” or “00-11-22-33-44-55” and the conversion should be successful. Also, you should have 2 characters per byte for the conversion to work properly.

## Parameters

- `inNameString`: Ptr to an NSString that contains the data to turn into the device address.
- `outDeviceAddress`: Ptr to an address structure that will be returned.

## See Also

### Miscellaneous
- [func IOBluetoothFindNumberOfRegistryEntriesOfClassName(UnsafePointer<CChar>!) -> Int](./iobluetoothfindnumberofregistryentriesofclassname%28_%29.md)
  The number of registry entries with a device classname.
- [func IOBluetoothGetUniqueFileNameAndPath(String!, String!) -> String!](./iobluetoothgetuniquefilenameandpath%28_,_%29.md)
- [func IOBluetoothIsFileAppleDesignatedPIMData(String!) -> Bool](./iobluetoothisfileappledesignatedpimdata%28_%29.md)
  Apple designated PIM data is classified as: .vcard, .vcal, .vcf, .vnote, .vmsg, .vcs
- [func IOBluetoothNSStringFromDeviceAddress(UnsafePointer<BluetoothDeviceAddress>!) -> String!](./iobluetoothnsstringfromdeviceaddress%28_%29.md)
  Convenience routine to take a device address structure and create an NSString.
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

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothnsstringtodeviceaddress(_:_:))*