# isHeadless

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value that indicates whether a GPU device doesn’t have a connection to a display.

**Availability**:
- Mac Catalyst 13.0+ - Deprecated in 27.0
- macOS 10.11+ - Deprecated in 27.0

> **Deprecated**: Not applicable on Apple Silicon

## Declaration

```swift
var isHeadless: Bool { get }
```

```objc
@property (readonly, getter=isHeadless) BOOL headless;
```

## Mentions

- [Finding multiple GPUs on an Intel-based Mac](../finding-multiple-gpus-on-an-intel-based-mac.md)

## Discussion

The value is [`true`](../../Swift/true.md) when the GPU is *headless*, which means it isn’t connected to any displays.

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
- [var locationNumber: Int](./locationnumber.md)
  A specific GPU position based on its general location.
- [var isLowPower: Bool](./islowpower.md)
  A Boolean value that indicates whether the GPU lowers its performance to conserve energy.
- [var isRemovable: Bool](./isremovable.md)
  A Boolean value that indicates whether the GPU is removable.
- [var peerGroupID: UInt64](./peergroupid.md)
  The peer group ID the GPU belongs to, if applicable.
- [var peerCount: UInt32](./peercount.md)
  The total number of GPUs in the peer group, if applicable.
- [var peerIndex: UInt32](./peerindex.md)
  The unique identifier for a GPU in a peer group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/isheadless)*