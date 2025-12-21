# storageMode

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The heap’s storage mode.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var storageMode: MTLStorageMode { get }
```

#### Discussion

Any resources you allocate on the heap have this storage mode.

## See Also

- [var device: any MTLDevice](mtlheap/device.md)
  The device object that created the heap.
- [var type: MTLHeapType](mtlheap/type.md)
  The heap’s type.
- [var cpuCacheMode: MTLCPUCacheMode](mtlheap/cpucachemode.md)
  The heap’s CPU cache mode.
- [var hazardTrackingMode: MTLHazardTrackingMode](mtlheap/hazardtrackingmode.md)
  The heap’s hazard tracking mode.
- [var resourceOptions: MTLResourceOptions](mtlheap/resourceoptions.md)
  The options for resources created by the heap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheap/storagemode)*