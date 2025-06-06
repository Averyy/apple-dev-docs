# IOUSBHostMatchingPropertyKey

**Framework**: IOUSBHost  
**Kind**: struct

Properties for implementing the matching service.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
struct IOUSBHostMatchingPropertyKey
```

## Topics

### Device Properties
- [static let vendorID: IOUSBHostMatchingPropertyKey](iousbhostmatchingpropertykey/vendorid.md)
  The matching property for the device’s vendor ID.
- [static let productID: IOUSBHostMatchingPropertyKey](iousbhostmatchingpropertykey/productid.md)
  The matching property for the device’s product ID.
- [static let deviceReleaseNumber: IOUSBHostMatchingPropertyKey](iousbhostmatchingpropertykey/devicereleasenumber.md)
  The matching property for the device’s release number.
- [static let configurationValue: IOUSBHostMatchingPropertyKey](iousbhostmatchingpropertykey/configurationvalue.md)
  The matching property for the device’s current configuration value.
- [static let speed: IOUSBHostMatchingPropertyKey](iousbhostmatchingpropertykey/speed.md)
  The matching property for the device’s enumeration speed.
- [static let productIDArray: IOUSBHostMatchingPropertyKey](iousbhostmatchingpropertykey/productidarray.md)
  The matching property on a list of product IDs.
- [static let productIDMask: IOUSBHostMatchingPropertyKey](iousbhostmatchingpropertykey/productidmask.md)
  The matching property on a mask of product IDs.
### Interface Properties
- [static let interfaceNumber: IOUSBHostMatchingPropertyKey](iousbhostmatchingpropertykey/interfacenumber.md)
  The matching property for the device’s interface number.
- [static let interfaceClass: IOUSBHostMatchingPropertyKey](iousbhostmatchingpropertykey/interfaceclass.md)
  The matching property for the interface’s class ID.
- [static let interfaceSubClass: IOUSBHostMatchingPropertyKey](iousbhostmatchingpropertykey/interfacesubclass.md)
  The matching property for the interface’s subclass ID.
- [static let interfaceProtocol: IOUSBHostMatchingPropertyKey](iousbhostmatchingpropertykey/interfaceprotocol.md)
  The matching property for the interface’s protocol.
### Protocol and Class Properties
- [static let deviceProtocol: IOUSBHostMatchingPropertyKey](iousbhostmatchingpropertykey/deviceprotocol.md)
  The matching property for the device’s protocol.
- [static let deviceClass: IOUSBHostMatchingPropertyKey](iousbhostmatchingpropertykey/deviceclass.md)
  The matching property for the device’s class.
- [static let deviceSubClass: IOUSBHostMatchingPropertyKey](iousbhostmatchingpropertykey/devicesubclass.md)
  The matching property for the device’s subclass.
### Initializing the Structure
- [init(rawValue: String)](iousbhostmatchingpropertykey/init(rawvalue:).md)
  Creates the structure.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct IOUSBHostInterfacePropertyKey](iousbhostinterfacepropertykey.md)
  Properties of a USB interface that describe its state.
- [struct IOUSBHostDevicePropertyKey](iousbhostdevicepropertykey.md)
  Properties of a USB device that describe its state.
- [typealias IOUSBHostPropertyKey](iousbhostpropertykey.md)
  Properties that the USB host device and interface classes share.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostmatchingpropertykey)*