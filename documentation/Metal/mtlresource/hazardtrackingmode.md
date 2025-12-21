# hazardTrackingMode

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

A mode that determines whether Metal tracks and synchronizes resource access.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var hazardTrackingMode: MTLHazardTrackingMode { get }
```

#### Discussion

This value can be either [`MTLHazardTrackingMode.untracked`](mtlhazardtrackingmode/untracked.md) or [`MTLHazardTrackingMode.tracked`](mtlhazardtrackingmode/tracked.md).

## See Also

- [var cpuCacheMode: MTLCPUCacheMode](mtlresource/cpucachemode.md)
  The CPU cache mode that defines the CPU mapping of the resource.
- [var storageMode: MTLStorageMode](mtlresource/storagemode.md)
  The location and access permissions of the resource.
- [var resourceOptions: MTLResourceOptions](mtlresource/resourceoptions.md)
  The storage mode, CPU cache mode, and hazard tracking mode of the resource.
- [enum MTLCPUCacheMode](mtlcpucachemode.md)
  Options for the CPU cache mode that define the CPU mapping of the resource.
- [enum MTLStorageMode](mtlstoragemode.md)
  Options for the memory location and access permissions for a resource.
- [enum MTLHazardTrackingMode](mtlhazardtrackingmode.md)
  Options that control whether Metal automatically tracks and prevents memory hazards for resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresource/hazardtrackingmode)*