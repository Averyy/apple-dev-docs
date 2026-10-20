# containerID

**Framework**: IOUSBHost  
**Kind**: property  
**Role**: Type Property

The device’s container ID.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
static let containerID: IOUSBHostDevicePropertyKey
```

```c
extern IOUSBHostDevicePropertyKey IOUSBHostDevicePropertyKeyContainerID;
```

#### Discussion

See USB 3.2, 9.6.2.3 for more information.

## See Also

### Properties
- [static let currentConfiguration: IOUSBHostDevicePropertyKey](./currentconfiguration.md)
  The device’s current configuration value.
- [static let serialNumberString: IOUSBHostDevicePropertyKey](./serialnumberstring.md)
  The device’s serial number as a string.
- [static let vendorString: IOUSBHostDevicePropertyKey](./vendorstring.md)
  The device’s vendor name.
- [typealias IOUSBHostPropertyKey](../iousbhostpropertykey.md)
  Properties that the USB host device and interface classes share.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostdevicepropertykey/containerid)*