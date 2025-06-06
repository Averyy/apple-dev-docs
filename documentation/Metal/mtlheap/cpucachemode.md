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

- [var type: MTLHeapType](mtlheap/type.md)
  The heap’s type.
- [var storageMode: MTLStorageMode](mtlheap/storagemode.md)
  The heap’s storage mode.
- [var hazardTrackingMode: MTLHazardTrackingMode](mtlheap/hazardtrackingmode.md)
  The heap’s hazard tracking mode.
- [var resourceOptions: MTLResourceOptions](mtlheap/resourceoptions.md)
  The options for resources created by the heap.
- [var size: Int](mtlheap/size.md)
  The total size of the heap, in bytes.
- [var usedSize: Int](mtlheap/usedsize.md)
  The size of all resources currently in the heap, in bytes.
- [var currentAllocatedSize: Int](mtlheap/currentallocatedsize.md)
  The size, in bytes, of the current heap allocation.
- [func maxAvailableSize(alignment: Int) -> Int](mtlheap/maxavailablesize(alignment:).md)
  The maximum size of a resource, in bytes, that can be currently allocated from the heap.
- [enum MTLHeapType](mtlheaptype.md)
  The options you use to choose the heap type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheap/cpucachemode)*