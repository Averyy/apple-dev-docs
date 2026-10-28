# AccessoryControlDevice.Capabilities

**Framework**: AudioAccessoryKit  
**Kind**: struct  
**Role**: Structure

A set of capabilities that an audio accessory supports.

**Availability**:
- iOS 26.4+

## Declaration

```swift
struct Capabilities
```

## Overview

The [`AccessoryControlDevice`](../accessorycontroldevice.md) class’s initializer takes an argument of this type. Use this structure to specify which features your accessory supports when initializing an audio accessory configuration.

## Topics

### Capability options
- [static let audioSwitching: AccessoryControlDevice.Capabilities](./capabilities/audioswitching.md)
  A capability indicating the device supports automatic audio switching.
- [static let placement: AccessoryControlDevice.Capabilities](./capabilities/placement.md)
  A capability indicating the device supports placement detection.
### Type Properties
- [static let audioSpatialization: AccessoryControlDevice.Capabilities](./capabilities/audiospatialization.md)
  Device supports audio spatialization
- [static let headTracking: AccessoryControlDevice.Capabilities](./capabilities/headtracking.md)
  Device supports head tracking for audio spatialization

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Device characteristics
- [AccessoryControlDevice.Placement](./placement.md)
  The physical placement of an audio accessory.
- [AccessoryControlDevice.Configuration](./configuration-swift.struct.md)
  The configuration for an accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audioaccessorykit/accessorycontroldevice/capabilities)*