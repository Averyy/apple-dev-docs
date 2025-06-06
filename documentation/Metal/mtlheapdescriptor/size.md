# size

**Framework**: Metal  
**Kind**: property

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

#### Discussion

You can use various [`MTLDevice`](mtldevice.md) methods to help you estimate an appropriate heap size, including the following:

- [`heapBufferSizeAndAlign(length:options:)`](mtldevice/heapbuffersizeandalign(length:options:).md)
- [`heapTextureSizeAndAlign(descriptor:)`](mtldevice/heaptexturesizeandalign(descriptor:).md)
- [`heapAccelerationStructureSizeAndAlign(size:)`](mtldevice/heapaccelerationstructuresizeandalign(size:).md)
- [`heapAccelerationStructureSizeAndAlign(descriptor:)`](mtldevice/heapaccelerationstructuresizeandalign(descriptor:).md)

> **Note**:  Metal may round a heap’s size to a page boundary.

 Metal may round a heap’s size to a page boundary.

This property’s default value is `0`.

## See Also

- [var type: MTLHeapType](mtlheapdescriptor/type.md)
  The memory placement strategy for any resources you allocate from the heaps you create with this descriptor.
- [var storageMode: MTLStorageMode](mtlheapdescriptor/storagemode.md)
  The storage mode for the heaps you create with this descriptor.
- [var cpuCacheMode: MTLCPUCacheMode](mtlheapdescriptor/cpucachemode.md)
  The CPU cache behavior for any resources you allocate from the heaps you create with this descriptor.
- [var hazardTrackingMode: MTLHazardTrackingMode](mtlheapdescriptor/hazardtrackingmode.md)
  The hazard tracking behavior for any resources you allocate from the heaps you create with this descriptor.
- [var resourceOptions: MTLResourceOptions](mtlheapdescriptor/resourceoptions.md)
  The combined behavior for any resources you allocate from the heaps you create with this descriptor.
- [var sparsePageSize: MTLSparsePageSize](mtlheapdescriptor/sparsepagesize.md)
  The page size for any resources you allocate from the heaps you create with this descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheapdescriptor/size)*