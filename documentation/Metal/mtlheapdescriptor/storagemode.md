# storageMode

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The storage mode for the heaps you create with this descriptor.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var storageMode: MTLStorageMode { get set }
```

```objc
@property (nonatomic, readwrite) MTLStorageMode storageMode;
```

## Discussion

For devices with Apple silicon, you can create a heap with either the [`MTLStorageMode.private`](../mtlstoragemode/private.md) or the [`MTLStorageMode.shared`](../mtlstoragemode/shared.md) storage mode. However, you can only create heaps with private storage on macOS devices without Apple silicon.

The resources you allocate from a heap inherit that heap’s storage mode. This property’s default value is [`MTLStorageMode.private`](../mtlstoragemode/private.md).

## See Also

### Configuring a heap
- [var type: MTLHeapType](./type.md)
  The memory placement strategy for any resources you allocate from the heaps you create with this descriptor.
- [var cpuCacheMode: MTLCPUCacheMode](./cpucachemode.md)
  The CPU cache behavior for any resources you allocate from the heaps you create with this descriptor.
- [var hazardTrackingMode: MTLHazardTrackingMode](./hazardtrackingmode.md)
  The hazard tracking behavior for any resources you allocate from the heaps you create with this descriptor.
- [var resourceOptions: MTLResourceOptions](./resourceoptions.md)
  The combined behavior for any resources you allocate from the heaps you create with this descriptor.
- [var size: Int](./size.md)
  The total amount of memory, in bytes, for the heaps you create with this descriptor.
- [var sparsePageSize: MTLSparsePageSize](./sparsepagesize.md)
  The page size for any resources you allocate from the heaps you create with this descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheapdescriptor/storagemode)*