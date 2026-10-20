# IOBluetoothNSStringFromDeviceAddress(_:)

**Framework**: IOBluetooth  
**Kind**: func

Convenience routine to take a device address structure and create an NSString.

**Availability**:
- macOS ?+

## Declaration

```swift
func IOBluetoothNSStringFromDeviceAddress(_ deviceAddress: UnsafePointer<BluetoothDeviceAddress>!) -> String!
```

#### Return Value

Returns the created address string.

#### Discussion

The resultant string will be in this format: “00-11-22-33-44-55”

## Parameters

- `deviceAddress`: A valid bluetooth device structure.

## See Also

- [func IOBluetoothFindNumberOfRegistryEntriesOfClassName(UnsafePointer<CChar>!) -> Int](iobluetoothfindnumberofregistryentriesofclassname(_:).md)
  The number of registry entries with a device classname.
- [func IOBluetoothGetUniqueFileNameAndPath(String!, String!) -> String!](iobluetoothgetuniquefilenameandpath(_:_:).md)
- [func IOBluetoothIsFileAppleDesignatedPIMData(String!) -> Bool](iobluetoothisfileappledesignatedpimdata(_:).md)
  Apple designated PIM data is classified as: .vcard, .vcal, .vcf, .vnote, .vmsg, .vcs
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

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothnsstringfromdeviceaddress(_:))*