# IOBluetoothDeviceSearchTypesBits

**Framework**: IOBluetooth  
**Kind**: struct

Bits to determine what Bluetooth devices to search for

**Availability**:
- macOS ?+

## Declaration

```swift
struct IOBluetoothDeviceSearchTypesBits
```

#### Overview

You can search for general device classes and service classes, or you can search for a specific device address or name. If you pass NULL as the attribute structure, you will get ALL devices in the vicinity found during a search. Note that passing a zeroed out block of attributes is NOT equivalent to passing in NULL!

## Topics

### Constants
- [var kIOBluetoothDeviceSearchClassic: IOBluetoothDeviceSearchTypesBits](kiobluetoothdevicesearchclassic.md)
- [var kIOBluetoothDeviceSearchLE: IOBluetoothDeviceSearchTypesBits](kiobluetoothdevicesearchle.md)
### Initializers
- [init(UInt32)](iobluetoothdevicesearchtypesbits/init(_:).md)
- [init(rawValue: UInt32)](iobluetoothdevicesearchtypesbits/init(rawvalue:).md)
### Instance Properties
- [var rawValue: UInt32](iobluetoothdevicesearchtypesbits/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [typealias BluetoothAFHMode](bluetoothafhmode.md)
- [typealias BluetoothAirMode](bluetoothairmode.md)
- [typealias BluetoothAllowRoleSwitch](bluetoothallowroleswitch.md)
- [typealias BluetoothAuthenticationRequirements](bluetoothauthenticationrequirements.md)
- [struct BluetoothAuthenticationRequirementsValues](bluetoothauthenticationrequirementsvalues.md)
- [typealias BluetoothClassOfDevice](bluetoothclassofdevice.md)
- [typealias BluetoothClockOffset](bluetoothclockoffset.md)
- [struct BluetoothCompanyIdentifers](bluetoothcompanyidentifers.md)
- [typealias BluetoothConnectionHandle](bluetoothconnectionhandle.md)
- [typealias BluetoothDeviceClassMajor](bluetoothdeviceclassmajor.md)
- [typealias BluetoothDeviceClassMinor](bluetoothdeviceclassminor.md)
- [typealias BluetoothDeviceName](bluetoothdevicename.md)
- [typealias BluetoothEncryptionEnable](bluetoothencryptionenable.md)
- [struct BluetoothFeatureBits](bluetoothfeaturebits.md)
- [typealias BluetoothHCIACLDataByteCount](bluetoothhciacldatabytecount.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevicesearchtypesbits)*