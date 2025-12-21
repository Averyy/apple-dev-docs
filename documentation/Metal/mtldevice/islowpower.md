# isLowPower

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

A Boolean value that indicates whether the GPU lowers its performance to conserve energy.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.11+

## Declaration

```swift
var isLowPower: Bool { get }
```

## Mentions

- [Finding multiple GPUs on an Intel-based Mac](finding-multiple-gpus-on-an-intel-based-mac.md)

#### Discussion

Some systems contain multiple GPUs that run with different performance and energy characteristics. At runtime, choose a GPU that best matches your performance needs while considering the current state of the system. For example, your app may choose a lower-power GPU if it doesn’t need the best possible performance on a MacBook Pro that’s running on battery power. For more information on discovering and selecting GPUs at runtime, see [`Multi-GPU systems`](multi-gpu-systems.md).

> **Note**:  Systems with Apple silicon only have one GPU, which removes the need to choose a GPU.

The property is typically [`true`](https://developer.apple.com/documentation/Swift/true) for integrated GPUs and [`false`](https://developer.apple.com/documentation/Swift/false) for discrete GPUs. However, an Apple silicon GPU on a Mac sets the property to [`false`](https://developer.apple.com/documentation/Swift/false) because it doesn’t need to lower its performance to conserve energy.

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

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/islowpower)*