# isRemovable

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

A Boolean value that indicates whether the GPU is removable.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
var isRemovable: Bool { get }
```

## Mentions

- [Finding Multiple GPUs on an Intel-based Mac](finding-multiple-gpus-on-an-intel-based-mac.md)

#### Discussion

You can respond to GPU removal notifications by registering with the [`MTLCopyAllDevicesWithObserver(handler:)`](mtlcopyalldeviceswithobserver(handler:).md) function in Swift, or the [`MTLCopyAllDevicesWithObserver`](mtlcopyalldeviceswithobserver.md) function in Objective-C, and responding to the [`removalRequested`](mtldevicenotificationname/removalrequested.md) and [`wasRemoved`](mtldevicenotificationname/wasremoved.md) device notification names.

> ❗ **Important**:  If a person removes a GPU without warning, [`MTLDevice`](mtldevice.md) APIs may fail even before your app receives a [`wasRemoved`](mtldevicenotificationname/wasremoved.md) notification.

 If a person removes a GPU without warning, [`MTLDevice`](mtldevice.md) APIs may fail even before your app receives a [`wasRemoved`](mtldevicenotificationname/wasremoved.md) notification.

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
- [var isHeadless: Bool](mtldevice/isheadless.md)
  A Boolean value that indicates whether a GPU device doesn’t have a connection to a display.
- [var peerGroupID: UInt64](mtldevice/peergroupid.md)
  The peer group ID the GPU belongs to, if applicable.
- [var peerCount: UInt32](mtldevice/peercount.md)
  The total number of GPUs in the peer group, if applicable.
- [var peerIndex: UInt32](mtldevice/peerindex.md)
  The unique identifier for a GPU in a peer group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/isremovable)*