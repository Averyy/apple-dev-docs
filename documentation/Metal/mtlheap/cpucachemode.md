# cpuCacheMode

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The heap’s CPU cache mode.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var cpuCacheMode: MTLCPUCacheMode { get }
```

#### Discussion

Any resources you allocate on the heap have this CPU cache mode.

## See Also

- [var device: any MTLDevice](mtlheap/device.md)
  The device object that created the heap.
- [var type: MTLHeapType](mtlheap/type.md)
  The heap’s type.
- [var storageMode: MTLStorageMode](mtlheap/storagemode.md)
  The heap’s storage mode.
- [var hazardTrackingMode: MTLHazardTrackingMode](mtlheap/hazardtrackingmode.md)
  The heap’s hazard tracking mode.
- [var resourceOptions: MTLResourceOptions](mtlheap/resourceoptions.md)
  The options for resources created by the heap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheap/cpucachemode)*