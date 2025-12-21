# resourceOptions

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The options for resources created by the heap.

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

The value of this property aggregates the values of [`storageMode`](mtlheap/storagemode.md), [`cpuCacheMode`](mtlheap/cpucachemode.md), and [`hazardTrackingMode`](mtlheap/hazardtrackingmode.md).

## See Also

- [var device: any MTLDevice](mtlheap/device.md)
  The device object that created the heap.
- [var type: MTLHeapType](mtlheap/type.md)
  The heap’s type.
- [var storageMode: MTLStorageMode](mtlheap/storagemode.md)
  The heap’s storage mode.
- [var cpuCacheMode: MTLCPUCacheMode](mtlheap/cpucachemode.md)
  The heap’s CPU cache mode.
- [var hazardTrackingMode: MTLHazardTrackingMode](mtlheap/hazardtrackingmode.md)
  The heap’s hazard tracking mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheap/resourceoptions)*