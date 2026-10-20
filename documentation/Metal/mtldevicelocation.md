# MTLDeviceLocation

**Framework**: Metal  
**Kind**: enum  
**Role**: Enumeration

Indicates the location of the GPU relative to the system it’s connect to.

**Availability**:
- macOS 10.15+ - Deprecated in 27.0

> **Deprecated**: Not applicable on Apple Silicon

## Declaration

```swift
enum MTLDeviceLocation
```

```c
enum MTLDeviceLocation : NSUInteger;
```

#### Overview

Check the location of a GPU by checking the [`location`](./mtldevice/location.md) property of its [`MTLDevice`](./mtldevice.md) instance.

## Topics

### Determining the GPU’s location
- [MTLDeviceLocation.builtIn](./mtldevicelocation/builtin.md)
  A location that indicates the GPU is permanently connected to the system internally.
- [MTLDeviceLocation.slot](./mtldevicelocation/slot.md)
  A GPU location that indicates a person connected the GPU to a system’s internal slot.
- [MTLDeviceLocation.external](./mtldevicelocation/external.md)
  A GPU location that indicates a person connected the GPU to the system with an external interface, such as Thunderbolt.
- [MTLDeviceLocation.unspecified](./mtldevicelocation/unspecified.md)
  A value that indicates the system can’t determine how the GPU connects to it.
### Initializers
- [init?(rawValue: UInt)](./mtldevicelocation/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Identifying a GPU device
- [var name: String](./mtldevice/name.md)
  The full name of the GPU device.
- [var architecture: MTLArchitecture](./mtldevice/architecture.md)
  The architectural details of the GPU device.
- [class MTLArchitecture](./mtlarchitecture.md)
  A class that contains the architectural details of a GPU device.
- [var registryID: UInt64](./mtldevice/registryid.md)
  The GPU device’s registry identifier.
- [var location: MTLDeviceLocation](./mtldevice/location.md)
  The physical location of the GPU relative to the system.
- [var locationNumber: Int](./mtldevice/locationnumber.md)
  A specific GPU position based on its general location.
- [var isLowPower: Bool](./mtldevice/islowpower.md)
  A Boolean value that indicates whether the GPU lowers its performance to conserve energy.
- [var isRemovable: Bool](./mtldevice/isremovable.md)
  A Boolean value that indicates whether the GPU is removable.
- [var isHeadless: Bool](./mtldevice/isheadless.md)
  A Boolean value that indicates whether a GPU device doesn’t have a connection to a display.
- [var peerGroupID: UInt64](./mtldevice/peergroupid.md)
  The peer group ID the GPU belongs to, if applicable.
- [var peerCount: UInt32](./mtldevice/peercount.md)
  The total number of GPUs in the peer group, if applicable.
- [var peerIndex: UInt32](./mtldevice/peerindex.md)
  The unique identifier for a GPU in a peer group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevicelocation)*