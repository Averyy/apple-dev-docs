# storageMode

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The location and access permissions of the resource.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var storageMode: MTLStorageMode { get }
```

## Mentions

- [Setting resource storage modes](setting-resource-storage-modes.md)
- [Synchronizing a managed resource in macOS](synchronizing-a-managed-resource-in-macos.md)

#### Discussion

The storage mode is set when you create the resource and cannot be changed.

## See Also

- [var cpuCacheMode: MTLCPUCacheMode](mtlresource/cpucachemode.md)
  The CPU cache mode that defines the CPU mapping of the resource.
- [var hazardTrackingMode: MTLHazardTrackingMode](mtlresource/hazardtrackingmode.md)
  A mode that determines whether Metal tracks and synchronizes resource access.
- [var resourceOptions: MTLResourceOptions](mtlresource/resourceoptions.md)
  The storage mode, CPU cache mode, and hazard tracking mode of the resource.
- [enum MTLCPUCacheMode](mtlcpucachemode.md)
  Options for the CPU cache mode that define the CPU mapping of the resource.
- [enum MTLStorageMode](mtlstoragemode.md)
  Options for the memory location and access permissions for a resource.
- [enum MTLHazardTrackingMode](mtlhazardtrackingmode.md)
  Options that control whether Metal automatically tracks and prevents memory hazards for resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresource/storagemode)*