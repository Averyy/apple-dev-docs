# SRDevice

**Framework**: SensorKit  
**Kind**: class  
**Role**: Class

A representation of a device that provides sample data.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class SRDevice
```

```objc
@interface SRDevice : NSObject
```

#### Overview

This class supports iOS and watchOS devices.

## Topics

### Accessing Device Information
- [var model: String](./srdevice/model.md)
  The user-defined name of the device.
- [var name: String](./srdevice/name.md)
  The framework-defined name of the device.
- [var systemName: String](./srdevice/systemname.md)
  The device’s operating system.
- [var systemVersion: String](./srdevice/systemversion.md)
  The device’s operating system version.
- [var productType: String](./srdevice/producttype.md)
  A string that identifies the device used to save a sample.
### Accessing the Primary Device
- [class var current: SRDevice](./srdevice/current.md)
  The device that runs the app.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Selecting the Device
- [var device: SRDevice](./srfetchrequest/device.md)
  The device to query for sample data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srdevice)*