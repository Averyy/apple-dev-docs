# CMIOExtensionDeviceSource

**Framework**: Core Media I/O  
**Kind**: protocol  
**Role**: Protocol

A protocol for objects that act as device sources.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
protocol CMIOExtensionDeviceSource : NSObjectProtocol
```

```objc
@protocol CMIOExtensionDeviceSource <NSObject>
```

## Overview

Create a class that adopts this protocol to configure device properties.

## Topics

### Managing Properties
- [var availableProperties: Set<CMIOExtensionProperty>](./cmioextensiondevicesource/availableproperties.md)
  A set of available properties that a device provides.
- [func deviceProperties(forProperties: Set<CMIOExtensionProperty>) throws -> CMIOExtensionDeviceProperties](./cmioextensiondevicesource/deviceproperties%28forproperties%29.md)
  Retrieves the state of device properties.
- [func setDeviceProperties(CMIOExtensionDeviceProperties) throws](./cmioextensiondevicesource/setdeviceproperties%28_%29.md)
  Sets the state of device properties.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Devices
- [class CMIOExtensionDevice](./cmioextensiondevice.md)
  An object that represents a physical or virtual device.
- [class CMIOExtensionDeviceProperties](./cmioextensiondeviceproperties.md)
  An object that defines the properties of a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensiondevicesource)*