# resourceOptions

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
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

```objc
@property (readonly) MTLResourceOptions resourceOptions;
```

#### Discussion

The value of this property aggregates the values of [`storageMode`](./storagemode.md), [`cpuCacheMode`](./cpucachemode.md), and [`hazardTrackingMode`](./hazardtrackingmode.md).

## See Also

### Reading memory and storage properties
- [var cpuCacheMode: MTLCPUCacheMode](./cpucachemode.md)
  The CPU cache mode that defines the CPU mapping of the resource.
- [var storageMode: MTLStorageMode](./storagemode.md)
  The location and access permissions of the resource.
- [var hazardTrackingMode: MTLHazardTrackingMode](./hazardtrackingmode.md)
  A mode that determines whether Metal tracks and synchronizes resource access.
- [enum MTLCPUCacheMode](../mtlcpucachemode.md)
  Options for the CPU cache mode that define the CPU mapping of the resource.
- [enum MTLStorageMode](../mtlstoragemode.md)
  Options for the memory location and access permissions for a resource.
- [enum MTLHazardTrackingMode](../mtlhazardtrackingmode.md)
  Options that control whether Metal automatically tracks and prevents memory hazards for resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresource/resourceoptions)*