# IOUSBHostInterfacePropertyKey

**Framework**: IOUSBHost  
**Kind**: struct

Properties of a USB interface that describe its state.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
struct IOUSBHostInterfacePropertyKey
```

## Topics

### Properties
- [static let alternateSetting: IOUSBHostInterfacePropertyKey](iousbhostinterfacepropertykey/alternatesetting.md)
  The USB interface’s current alternative setting value.
### Initializing the Structure
- [init(rawValue: String)](iousbhostinterfacepropertykey/init(rawvalue:).md)
  Creates the structure.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct IOUSBHostDevicePropertyKey](iousbhostdevicepropertykey.md)
  Properties of a USB device that describe its state.
- [struct IOUSBHostMatchingPropertyKey](iousbhostmatchingpropertykey.md)
  Properties for implementing the matching service.
- [typealias IOUSBHostPropertyKey](iousbhostpropertykey.md)
  Properties that the USB host device and interface classes share.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostinterfacepropertykey)*