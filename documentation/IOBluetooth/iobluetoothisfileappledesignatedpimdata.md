# IOBluetoothIsFileAppleDesignatedPIMData(_:)

**Framework**: IOBluetooth  
**Kind**: func

Apple designated PIM data is classified as: .vcard, .vcal, .vcf, .vnote, .vmsg, .vcs

**Availability**:
- macOS ?+

## Declaration

```swift
func IOBluetoothIsFileAppleDesignatedPIMData(_ inFileName: String!) -> Bool
```

#### Return Value

Yes or no, is it Apple-designated PIM data?

#### Discussion

Not much to talk about.

## Parameters

- `inFileName`: Name of file - should include extension!

## See Also

- [func IOBluetoothFindNumberOfRegistryEntriesOfClassName(UnsafePointer<CChar>!) -> Int](iobluetoothfindnumberofregistryentriesofclassname(_:).md)
  The number of registry entries with a device classname.
- [func IOBluetoothGetUniqueFileNameAndPath(String!, String!) -> String!](iobluetoothgetuniquefilenameandpath(_:_:).md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothisfileappledesignatedpimdata(_:))*