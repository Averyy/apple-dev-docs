# locationNumber

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

A specific GPU position based on its general location.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var locationNumber: Int { get }
```

#### Discussion

The meaning of the location number depends on a device’s [`location`](mtldevice/location.md) property:

- For [`MTLDeviceLocation.builtIn`](mtldevicelocation/builtin.md), the location number is `0` for low-power GPUs (see [`isLowPower`](mtldevice/islowpower.md)) and `1` for other GPUs.
- For [`MTLDeviceLocation.slot`](mtldevicelocation/slot.md), the location number represents the slot.
- For [`MTLDeviceLocation.external`](mtldevicelocation/external.md), the location number represents the Thunderbolt port.

> **Note**:  It’s possible for multiple devices to share the same location and number. For example, a card in a slot may have multiple GPUs, or a person may connect multiple eGPUs to the same Thunderbolt port.

 It’s possible for multiple devices to share the same location and number. For example, a card in a slot may have multiple GPUs, or a person may connect multiple eGPUs to the same Thunderbolt port.

## See Also

- [var name: String](mtldevice/name.md)
  The full name of the GPU device.
- [var architecture: MTLArchitecture](mtldevice/architecture.md)
  The architectural details of the GPU device.
- [class MTLArchitecture](mtlarchitecture.md)
  A class that contains the architectural details of a GPU device.
- [var registryID: UInt64](mtldevice/registryid.md)
  The GPU device’s registry identifier.
- [var location: MTLDeviceLocation](mtldevice/location.md)
  The physical location of the GPU relative to the system.
- [enum MTLDeviceLocation](mtldevicelocation.md)
  Indicates the location of the GPU relative to the system it’s connect to.
- [var isLowPower: Bool](mtldevice/islowpower.md)
  A Boolean value that indicates whether the GPU lowers its performance to conserve energy.
- [var isRemovable: Bool](mtldevice/isremovable.md)
  A Boolean value that indicates whether the GPU is removable.
- [var isHeadless: Bool](mtldevice/isheadless.md)
  A Boolean value that indicates whether a GPU device doesn’t have a connection to a display.
- [var peerGroupID: UInt64](mtldevice/peergroupid.md)
  The peer group ID the GPU belongs to, if applicable.
- [var peerCount: UInt32](mtldevice/peercount.md)
  The total number of GPUs in the peer group, if applicable.
- [var peerIndex: UInt32](mtldevice/peerindex.md)
  The unique identifier for a GPU in a peer group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/locationnumber)*