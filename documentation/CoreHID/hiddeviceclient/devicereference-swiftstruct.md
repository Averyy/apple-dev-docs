# HIDDeviceClient.DeviceReference

**Framework**: Core HID  
**Kind**: struct

A reference to a HID device on the system.

**Availability**:
- macOS 15.0+

## Declaration

```swift
struct DeviceReference
```

#### Overview

A device reference exists for every discovered device. Use it to create an [`HIDDeviceClient`](hiddeviceclient.md), and maintain the reference until someone removes the device.

## Topics

### Operators
- [static func == (HIDDeviceClient.DeviceReference, HIDDeviceClient.DeviceReference) -> Bool](hiddeviceclient/devicereference-swift.struct/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [let deviceID: UInt64](hiddeviceclient/devicereference-swift.struct/deviceid.md)
  The unique ID for the associated HID device.
- [var hashValue: Int](hiddeviceclient/devicereference-swift.struct/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](hiddeviceclient/devicereference-swift.struct/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [CustomStringConvertible Implementations](hiddeviceclient/devicereference-swift.struct/customstringconvertible-implementations.md)
- [Equatable Implementations](hiddeviceclient/devicereference-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init?(deviceReference: HIDDeviceClient.DeviceReference)](hiddeviceclient/init(devicereference:).md)
  Creates a client for a HID device.
- [let deviceReference: HIDDeviceClient.DeviceReference](hiddeviceclient/devicereference-swift.property.md)
  The reference to the HID device used to create the  HID client device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddeviceclient/devicereference-swift.struct)*