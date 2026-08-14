# SRDevice

**Framework**: SensorKit  
**Kind**: class

A representation of a device that provides sample data.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class SRDevice
```

#### Overview

This class supports iOS and watchOS devices.

## Topics

### Accessing Device Information
- [var model: String](srdevice/model.md)
  The user-defined name of the device.
- [var name: String](srdevice/name.md)
  The framework-defined name of the device.
- [var systemName: String](srdevice/systemname.md)
  The device’s operating system.
- [var systemVersion: String](srdevice/systemversion.md)
  The device’s operating system version.
- [var productType: String](srdevice/producttype.md)
  A string that identifies the device used to save a sample.
### Accessing the Primary Device
- [class var current: SRDevice](srdevice/current.md)
  The device that runs the app.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var device: SRDevice](srfetchrequest/device.md)
  The device to query for sample data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srdevice)*