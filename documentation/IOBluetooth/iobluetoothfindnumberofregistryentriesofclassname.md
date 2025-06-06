# IOBluetoothFindNumberOfRegistryEntriesOfClassName(_:)

**Framework**: IOBluetooth  
**Kind**: func

The number of registry entries with a device classname.

**Availability**:
- macOS ?+

## Declaration

```swift
func IOBluetoothFindNumberOfRegistryEntriesOfClassName(_ deviceType: UnsafePointer<CChar>!) -> Int
```

#### Return Value

Number of HID devices.

#### Overview

Returns total number of registry entries with the provided device classname. For example, [`IOHIPointing`](https://developer.apple.com/documentation/kernel/iohipointing).

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothfindnumberofregistryentriesofclassname(_:))*