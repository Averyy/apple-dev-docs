# resourceOptions

**Framework**: Metal  
**Kind**: property

The combined behavior for any resources you allocate from the heaps you create with this descriptor.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var resourceOptions: MTLResourceOptions { get set }
```

#### Discussion

This property aggregates the values of [`storageMode`](mtlheapdescriptor/storagemode.md), [`cpuCacheMode`](mtlheapdescriptor/cpucachemode.md), and [`hazardTrackingMode`](mtlheapdescriptor/hazardtrackingmode.md). Any modifications you make to this property affect the other properties, and vice versa.

## See Also

- [var type: MTLHeapType](mtlheapdescriptor/type.md)
  The memory placement strategy for any resources you allocate from the heaps you create with this descriptor.
- [var storageMode: MTLStorageMode](mtlheapdescriptor/storagemode.md)
  The storage mode for the heaps you create with this descriptor.
- [var cpuCacheMode: MTLCPUCacheMode](mtlheapdescriptor/cpucachemode.md)
  The CPU cache behavior for any resources you allocate from the heaps you create with this descriptor.
- [var hazardTrackingMode: MTLHazardTrackingMode](mtlheapdescriptor/hazardtrackingmode.md)
  The hazard tracking behavior for any resources you allocate from the heaps you create with this descriptor.
- [var size: Int](mtlheapdescriptor/size.md)
  The total amount of memory, in bytes, for the heaps you create with this descriptor.
- [var sparsePageSize: MTLSparsePageSize](mtlheapdescriptor/sparsepagesize.md)
  The page size for any resources you allocate from the heaps you create with this descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheapdescriptor/resourceoptions)*