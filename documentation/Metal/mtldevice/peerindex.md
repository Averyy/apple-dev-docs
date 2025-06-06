# peerIndex

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The unique identifier for a GPU in a peer group.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var peerIndex: UInt32 { get }
```

#### Discussion

If the GPU is part of a peer group (see [`peerGroupID`](mtldevice/peergroupid.md) or [`peerCount`](mtldevice/peercount.md)) the peer index is the GPU’s unique value within the group in the range `[0, `[`peerCount`](mtldevice/peercount.md)`)`.

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
- [var locationNumber: Int](mtldevice/locationnumber.md)
  A specific GPU position based on its general location.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/peerindex)*