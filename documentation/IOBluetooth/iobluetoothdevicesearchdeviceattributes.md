# IOBluetoothDeviceSearchDeviceAttributes

**Framework**: IOBluetooth  
**Kind**: struct

Structure used to search for particular devices.

**Availability**:
- macOS ?+

## Declaration

```swift
struct IOBluetoothDeviceSearchDeviceAttributes
```

#### Overview

You can search for general device classes and service classes, or you can search for a specific device address or name. If you pass NULL as the attribute structure, you will get ALL devices in the vicinity found during a search. Note that passing a zeroed out block of attributes is NOT equivalent to passing in NULL!

## Topics

### Initializers
- [init()](iobluetoothdevicesearchdeviceattributes/init.md)
- [init(address: BluetoothDeviceAddress, name: BluetoothDeviceName, serviceClassMajor: BluetoothServiceClassMajor, deviceClassMajor: BluetoothDeviceClassMajor, deviceClassMinor: BluetoothDeviceClassMinor)](iobluetoothdevicesearchdeviceattributes/init(address:name:serviceclassmajor:deviceclassmajor:deviceclassminor:).md)
### Instance Properties
- [var address: BluetoothDeviceAddress](iobluetoothdevicesearchdeviceattributes/address.md)
- [var deviceClassMajor: BluetoothDeviceClassMajor](iobluetoothdevicesearchdeviceattributes/deviceclassmajor.md)
- [var deviceClassMinor: BluetoothDeviceClassMinor](iobluetoothdevicesearchdeviceattributes/deviceclassminor.md)
- [var name: BluetoothDeviceName](iobluetoothdevicesearchdeviceattributes/name.md)
- [var serviceClassMajor: BluetoothServiceClassMajor](iobluetoothdevicesearchdeviceattributes/serviceclassmajor.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct IOBluetoothDeviceSearchAttributes](iobluetoothdevicesearchattributes.md)
  Structure used to search for particular devices.
- [typealias IOBluetoothDeviceSearchTypes](iobluetoothdevicesearchtypes.md)
- [struct IOBluetoothDeviceSearchTypesBits](iobluetoothdevicesearchtypesbits.md)
  Bits to determine what Bluetooth devices to search for
- [struct IOBluetoothDeviceSearchDeviceAttributes](iobluetoothdevicesearchdeviceattributes.md)
  Structure used to search for particular devices.
- [typealias IOBluetoothDeviceSearchOptions](iobluetoothdevicesearchoptions.md)
- [struct IOBluetoothDeviceSearchAttributes](iobluetoothdevicesearchattributes.md)
  Structure used to search for particular devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevicesearchdeviceattributes)*