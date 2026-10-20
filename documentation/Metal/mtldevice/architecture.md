# architecture

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The architectural details of the GPU device.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var architecture: MTLArchitecture { get }
```

```objc
@property (readonly, nonnull) MTLArchitecture * architecture;
```

## See Also

### Identifying a GPU device
- [var name: String](./name.md)
  The full name of the GPU device.
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
- [var isHeadless: Bool](./isheadless.md)
  A Boolean value that indicates whether a GPU device doesn’t have a connection to a display.
- [var peerGroupID: UInt64](./peergroupid.md)
  The peer group ID the GPU belongs to, if applicable.
- [var peerCount: UInt32](./peercount.md)
  The total number of GPUs in the peer group, if applicable.
- [var peerIndex: UInt32](./peerindex.md)
  The unique identifier for a GPU in a peer group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/architecture)*