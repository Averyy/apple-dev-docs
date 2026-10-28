# cpuCacheMode

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readwrite) MTLCPUCacheMode cpuCacheMode;
```

## Discussion

This property’s default value is [`MTLCPUCacheMode.defaultCache`](../mtlcpucachemode/defaultcache.md).

The resources you allocate from a heap inherit that heap’s CPU cache mode.

## See Also

### Configuring a heap
- [var type: MTLHeapType](./type.md)
  The memory placement strategy for any resources you allocate from the heaps you create with this descriptor.
- [var storageMode: MTLStorageMode](./storagemode.md)
  The storage mode for the heaps you create with this descriptor.
- [var hazardTrackingMode: MTLHazardTrackingMode](./hazardtrackingmode.md)
  The hazard tracking behavior for any resources you allocate from the heaps you create with this descriptor.
- [var resourceOptions: MTLResourceOptions](./resourceoptions.md)
  The combined behavior for any resources you allocate from the heaps you create with this descriptor.
- [var size: Int](./size.md)
  The total amount of memory, in bytes, for the heaps you create with this descriptor.
- [var sparsePageSize: MTLSparsePageSize](./sparsepagesize.md)
  The page size for any resources you allocate from the heaps you create with this descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheapdescriptor/cpucachemode)*