# sparsePageSize

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The page size for any resources you allocate from the heaps you create with this descriptor.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var sparsePageSize: MTLSparsePageSize { get set }
```

```objc
@property (nonatomic, readwrite) MTLSparsePageSize sparsePageSize;
```

## Discussion

This property’s default value is 16 kilobytes ([`MTLSparsePageSize.size16`](../mtlsparsepagesize/size16.md)), which is a smaller page size option that can help reduce your app’s memory usage. However, you can reduce operational overhead for sparse textures with larger page sizes, such as [`MTLSparsePageSize.size64`](../mtlsparsepagesize/size64.md) and [`MTLSparsePageSize.size256`](../mtlsparsepagesize/size256.md). These operations include blit commands and the configuration of sparse texture mappings (see [Blit passes](../blit-passes.md) and [`MTLResourceStateCommandEncoder`](../mtlresourcestatecommandencoder.md), respectively).

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
- [var resourceOptions: MTLResourceOptions](./resourceoptions.md)
  The combined behavior for any resources you allocate from the heaps you create with this descriptor.
- [var size: Int](./size.md)
  The total amount of memory, in bytes, for the heaps you create with this descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheapdescriptor/sparsepagesize)*