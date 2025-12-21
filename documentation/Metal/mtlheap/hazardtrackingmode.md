# hazardTrackingMode

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The heap’s hazard tracking mode.

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

Any resources you allocate on the heap have this hazard tracking mode.

## See Also

- [var device: any MTLDevice](mtlheap/device.md)
  The device object that created the heap.
- [var type: MTLHeapType](mtlheap/type.md)
  The heap’s type.
- [var storageMode: MTLStorageMode](mtlheap/storagemode.md)
  The heap’s storage mode.
- [var cpuCacheMode: MTLCPUCacheMode](mtlheap/cpucachemode.md)
  The heap’s CPU cache mode.
- [var resourceOptions: MTLResourceOptions](mtlheap/resourceoptions.md)
  The options for resources created by the heap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheap/hazardtrackingmode)*