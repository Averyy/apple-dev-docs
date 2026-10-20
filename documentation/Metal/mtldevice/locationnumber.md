# locationNumber

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A specific GPU position based on its general location.

**Availability**:
- macOS 10.15+ - Deprecated in 27.0

> **Deprecated**: Not applicable on Apple Silicon

## Declaration

```swift
var locationNumber: Int { get }
```

```objc
@property (readonly) NSUInteger locationNumber;
```

#### Discussion

The meaning of the location number depends on a device’s [`location`](./location.md) property:

- For [`MTLDeviceLocation.builtIn`](../mtldevicelocation/builtin.md), the location number is `0` for low-power GPUs (see [`isLowPower`](./islowpower.md)) and `1` for other GPUs.
- For [`MTLDeviceLocation.slot`](../mtldevicelocation/slot.md), the location number represents the slot.
- For [`MTLDeviceLocation.external`](../mtldevicelocation/external.md), the location number represents the Thunderbolt port.

> **Note**:  It’s possible for multiple devices to share the same location and number. For example, a card in a slot may have multiple GPUs, or a person may connect multiple eGPUs to the same Thunderbolt port.

## See Also

### Identifying a GPU device
- [var name: String](./name.md)
  The full name of the GPU device.
- [var architecture: MTLArchitecture](./architecture.md)
  The architectural details of the GPU device.
- [class MTLArchitecture](../mtlarchitecture.md)
  A class that contains the architectural details of a GPU device.
- [var registryID: UInt64](./registryid.md)
  The GPU device’s registry identifier.
- [var location: MTLDeviceLocation](./location.md)
  The physical location of the GPU relative to the system.
- [enum MTLDeviceLocation](../mtldevicelocation.md)
  Indicates the location of the GPU relative to the system it’s connect to.
- [var isLowPower: Bool](./islowpower.md)
  A Boolean value that indicates whether the GPU lowers its performance to conserve energy.
- [var isRemovable: Bool](./isremovable.md)
  A Boolean value that indicates whether the GPU is removable.
- [var isHeadless: Bool](./isheadless.md)
  A Boolean value that indicates whether a GPU device doesn’t have a connection to a display.
- [var peerGroupID: UInt64](./peergroupid.md)
  The peer group ID the GPU belongs to, if applicable.
- [var peerCount: UInt32](./peercount.md)
  The total number of GPUs in the peer group, if applicable.
- [var peerIndex: UInt32](./peerindex.md)
  The unique identifier for a GPU in a peer group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/locationnumber)*