# resourceOptions

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readwrite) MTLResourceOptions resourceOptions;
```

#### Discussion

This property aggregates the values of [`storageMode`](./storagemode.md), [`cpuCacheMode`](./cpucachemode.md), and [`hazardTrackingMode`](./hazardtrackingmode.md). Any modifications you make to this property affect the other properties, and vice versa.

## See Also

### Configuring a heap
- [var type: MTLHeapType](./type.md)
  The memory placement strategy for any resources you allocate from the heaps you create with this descriptor.
- [var storageMode: MTLStorageMode](./storagemode.md)
  The storage mode for the heaps you create with this descriptor.
- [var cpuCacheMode: MTLCPUCacheMode](./cpucachemode.md)
  The CPU cache behavior for any resources you allocate from the heaps you create with this descriptor.
- [var hazardTrackingMode: MTLHazardTrackingMode](./hazardtrackingmode.md)
  The hazard tracking behavior for any resources you allocate from the heaps you create with this descriptor.
- [var size: Int](./size.md)
  The total amount of memory, in bytes, for the heaps you create with this descriptor.
- [var sparsePageSize: MTLSparsePageSize](./sparsepagesize.md)
  The page size for any resources you allocate from the heaps you create with this descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheapdescriptor/resourceoptions)*