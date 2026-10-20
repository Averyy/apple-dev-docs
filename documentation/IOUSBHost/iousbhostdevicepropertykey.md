# IOUSBHostDevicePropertyKey

**Framework**: IOUSBHost  
**Kind**: struct  
**Role**: Structure

Properties of a USB device that describe its state.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
struct IOUSBHostDevicePropertyKey
```

```c
typedef NSString * IOUSBHostDevicePropertyKey;
```

## Topics

### Properties
- [static let currentConfiguration: IOUSBHostDevicePropertyKey](./iousbhostdevicepropertykey/currentconfiguration.md)
  The device’s current configuration value.
- [static let containerID: IOUSBHostDevicePropertyKey](./iousbhostdevicepropertykey/containerid.md)
  The device’s container ID.
- [static let serialNumberString: IOUSBHostDevicePropertyKey](./iousbhostdevicepropertykey/serialnumberstring.md)
  The device’s serial number as a string.
- [static let vendorString: IOUSBHostDevicePropertyKey](./iousbhostdevicepropertykey/vendorstring.md)
  The device’s vendor name.
- [typealias IOUSBHostPropertyKey](./iousbhostpropertykey.md)
  Properties that the USB host device and interface classes share.
### Initializing the Properties
- [init(rawValue: String)](./iousbhostdevicepropertykey/init%28rawvalue%29.md)
  Creates the structure.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### IOServicePlane Properties
- [struct IOUSBHostInterfacePropertyKey](./iousbhostinterfacepropertykey.md)
  Properties of a USB interface that describe its state.
- [struct IOUSBHostMatchingPropertyKey](./iousbhostmatchingpropertykey.md)
  Properties for implementing the matching service.
- [typealias IOUSBHostPropertyKey](./iousbhostpropertykey.md)
  Properties that the USB host device and interface classes share.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostdevicepropertykey)*