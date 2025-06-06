# cpuCacheMode

**Framework**: Metal  
**Kind**: property

The CPU cache behavior for any resources you allocate from the heaps you create with this descriptor.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var cpuCacheMode: MTLCPUCacheMode { get set }
```

#### Discussion

This property’s default value is [`MTLCPUCacheMode.defaultCache`](mtlcpucachemode/defaultcache.md).

The resources you allocate from a heap inherit that heap’s CPU cache mode.

## See Also

- [var type: MTLHeapType](mtlheapdescriptor/type.md)
  The memory placement strategy for any resources you allocate from the heaps you create with this descriptor.
- [var storageMode: MTLStorageMode](mtlheapdescriptor/storagemode.md)
  The storage mode for the heaps you create with this descriptor.
- [var hazardTrackingMode: MTLHazardTrackingMode](mtlheapdescriptor/hazardtrackingmode.md)
  The hazard tracking behavior for any resources you allocate from the heaps you create with this descriptor.
- [var resourceOptions: MTLResourceOptions](mtlheapdescriptor/resourceoptions.md)
  The combined behavior for any resources you allocate from the heaps you create with this descriptor.
- [var size: Int](mtlheapdescriptor/size.md)
  The total amount of memory, in bytes, for the heaps you create with this descriptor.
- [var sparsePageSize: MTLSparsePageSize](mtlheapdescriptor/sparsepagesize.md)
  The page size for any resources you allocate from the heaps you create with this descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheapdescriptor/cpucachemode)*