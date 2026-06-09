# AccessoryControlDevice.Capabilities

**Framework**: AudioAccessoryKit  
**Kind**: struct

A set of capabilities that an audio accessory supports.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
struct Capabilities
```

#### Overview

The [`AccessoryControlDevice`](accessorycontroldevice.md) class’s initializer takes an argument of this type. Use this structure to specify which features your accessory supports when initializing an audio accessory configuration.

## Topics

### Capability options
- [static let audioSwitching: AccessoryControlDevice.Capabilities](accessorycontroldevice/capabilities/audioswitching.md)
  A capability indicating the device supports automatic audio switching.
- [static let placement: AccessoryControlDevice.Capabilities](accessorycontroldevice/capabilities/placement.md)
  A capability indicating the device supports placement detection.
### Type Properties
- [static let audioSpatialization: AccessoryControlDevice.Capabilities](accessorycontroldevice/capabilities/audiospatialization.md)
  Device supports audio spatialization
- [static let headTracking: AccessoryControlDevice.Capabilities](accessorycontroldevice/capabilities/headtracking.md)
  Device supports head tracking for audio spatialization

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [AccessoryControlDevice.Placement](accessorycontroldevice/placement.md)
  The physical placement of an audio accessory.
- [AccessoryControlDevice.Configuration](accessorycontroldevice/configuration-swift.struct.md)
  The configuration for an accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audioaccessorykit/accessorycontroldevice/capabilities)*