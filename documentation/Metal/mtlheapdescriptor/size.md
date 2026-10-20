# size

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The total amount of memory, in bytes, for the heaps you create with this descriptor.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var size: Int { get set }
```

```objc
@property (nonatomic, readwrite) NSUInteger size;
```

#### Discussion

You can use various [`MTLDevice`](../mtldevice.md) methods to help you estimate an appropriate heap size, including the following:

- [`heapBufferSizeAndAlign(length:options:)`](../mtldevice/heapbuffersizeandalign%28length,options%29.md)
- [`heapTextureSizeAndAlign(descriptor:)`](../mtldevice/heaptexturesizeandalign%28descriptor%29.md)
- [`heapAccelerationStructureSizeAndAlign(size:)`](../mtldevice/heapaccelerationstructuresizeandalign%28size%29.md)
- [`heapAccelerationStructureSizeAndAlign(descriptor:)`](../mtldevice/heapaccelerationstructuresizeandalign%28descriptor%29.md)

> **Note**:  Metal may round a heap’s size to a page boundary.

This property’s default value is `0`.

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
- [var sparsePageSize: MTLSparsePageSize](./sparsepagesize.md)
  The page size for any resources you allocate from the heaps you create with this descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheapdescriptor/size)*