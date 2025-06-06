# resourceOptions

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The storage mode, CPU cache mode, and hazard tracking mode of the resource.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var resourceOptions: MTLResourceOptions { get }
```

#### Discussion

The value of this property aggregates the values of [`storageMode`](mtlresource/storagemode.md), [`cpuCacheMode`](mtlresource/cpucachemode.md), and [`hazardTrackingMode`](mtlresource/hazardtrackingmode.md).

## See Also

- [var cpuCacheMode: MTLCPUCacheMode](mtlresource/cpucachemode.md)
  The CPU cache mode that defines the CPU mapping of the resource.
- [var storageMode: MTLStorageMode](mtlresource/storagemode.md)
  The location and access permissions of the resource.
- [var hazardTrackingMode: MTLHazardTrackingMode](mtlresource/hazardtrackingmode.md)
  A mode that determines whether Metal tracks and synchronizes resource access.
- [enum MTLCPUCacheMode](mtlcpucachemode.md)
  Options for the CPU cache mode that define the CPU mapping of the resource.
- [enum MTLStorageMode](mtlstoragemode.md)
  Options for the memory location and access permissions for a resource.
- [enum MTLHazardTrackingMode](mtlhazardtrackingmode.md)
  The options you use to specify the hazard tracking mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresource/resourceoptions)*