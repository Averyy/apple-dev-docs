# hazardTrackingMode

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readwrite) MTLHazardTrackingMode hazardTrackingMode;
```

#### Discussion

This property’s default value is [`MTLHazardTrackingMode.default`](../mtlhazardtrackingmode/default.md), which is equivalent to [`MTLHazardTrackingMode.untracked`](../mtlhazardtrackingmode/untracked.md) for a heap.

The resources you allocate from a heap inherit that heap’s hazard tracking mode.

## See Also

### Configuring a heap
- [var type: MTLHeapType](./type.md)
  The memory placement strategy for any resources you allocate from the heaps you create with this descriptor.
- [var storageMode: MTLStorageMode](./storagemode.md)
  The storage mode for the heaps you create with this descriptor.
- [var cpuCacheMode: MTLCPUCacheMode](./cpucachemode.md)
  The CPU cache behavior for any resources you allocate from the heaps you create with this descriptor.
- [var resourceOptions: MTLResourceOptions](./resourceoptions.md)
  The combined behavior for any resources you allocate from the heaps you create with this descriptor.
- [var size: Int](./size.md)
  The total amount of memory, in bytes, for the heaps you create with this descriptor.
- [var sparsePageSize: MTLSparsePageSize](./sparsepagesize.md)
  The page size for any resources you allocate from the heaps you create with this descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheapdescriptor/hazardtrackingmode)*