# hazardTrackingMode

**Framework**: Metal  
**Kind**: property

The hazard tracking behavior for any resources you allocate from the heaps you create with this descriptor.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var hazardTrackingMode: MTLHazardTrackingMode { get set }
```

#### Discussion

This property’s default value is [`MTLHazardTrackingMode.default`](mtlhazardtrackingmode/default.md), which is equivalent to [`MTLHazardTrackingMode.untracked`](mtlhazardtrackingmode/untracked.md) for a heap.

The resources you allocate from a heap inherit that heap’s hazard tracking mode.

## See Also

- [var type: MTLHeapType](mtlheapdescriptor/type.md)
  The memory placement strategy for any resources you allocate from the heaps you create with this descriptor.
- [var storageMode: MTLStorageMode](mtlheapdescriptor/storagemode.md)
  The storage mode for the heaps you create with this descriptor.
- [var cpuCacheMode: MTLCPUCacheMode](mtlheapdescriptor/cpucachemode.md)
  The CPU cache behavior for any resources you allocate from the heaps you create with this descriptor.
- [var resourceOptions: MTLResourceOptions](mtlheapdescriptor/resourceoptions.md)
  The combined behavior for any resources you allocate from the heaps you create with this descriptor.
- [var size: Int](mtlheapdescriptor/size.md)
  The total amount of memory, in bytes, for the heaps you create with this descriptor.
- [var sparsePageSize: MTLSparsePageSize](mtlheapdescriptor/sparsepagesize.md)
  The page size for any resources you allocate from the heaps you create with this descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheapdescriptor/hazardtrackingmode)*