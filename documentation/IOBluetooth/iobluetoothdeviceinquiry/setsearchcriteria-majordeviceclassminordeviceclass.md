# setSearchCriteria(_:majorDeviceClass:minorDeviceClass:)

**Framework**: IOBluetooth  
**Kind**: method

Use this method to set the criteria for the device search.

**Availability**:
- macOS ?+

## Declaration

```swift
func setSearchCriteria(_ inServiceClassMajor: BluetoothServiceClassMajor, majorDeviceClass inMajorDeviceClass: BluetoothDeviceClassMajor, minorDeviceClass inMinorDeviceClass: BluetoothDeviceClassMinor)
```

#### Discussion

The default inquiry object will search for all types of devices. If you wish to find only keyboards, for example, you might use this method like this:

[myInquiryObject setSearchCriteria:kBluetoothServiceClassMajorAny majorDeviceClass:kBluetoothDeviceClassMajorPeripheral minorDeviceClass:kBluetoothDeviceClassMinorPeripheral1Keyboard];

However, we recommend only using this if you are certain of the device class you are looking for, as some devices may report a different/unexpected device class, and the search may miss the device you are interested in.

## Parameters

- `inServiceClassMajor`: Set the major service class for found devices. Set to kBluetoothServiceClassMajorAny for all devices. See BluetoothAssignedNumbers.h for possible values.
- `inMajorDeviceClass`: Set the major device class for found devices. Set to kBluetoothDeviceClassMajorAny for all devices. See BluetoothAssignedNumbers.h for possible values.
- `inMinorDeviceClass`: Set the minor device class for found devices. Set to kBluetoothDeviceClassMinorAny for all devices. See BluetoothAssignedNumbers.h for possible values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdeviceinquiry/setsearchcriteria(_:majordeviceclass:minordeviceclass:))*