# MTLHeapType

**Framework**: Metal  
**Kind**: enum

The options you use to choose the heap type.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
enum MTLHeapType
```

## Topics

### Specifying the Heap Type
- [MTLHeapType.automatic](mtlheaptype/automatic.md)
  A heap that automatically places new resource allocations.
- [MTLHeapType.placement](mtlheaptype/placement.md)
  The app controls placement of resources on the heap.
- [MTLHeapType.sparse](mtlheaptype/sparse.md)
  The heap contains sparse texture tiles.
### Initializers
- [init?(rawValue: Int)](mtlheaptype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Using Argument Buffers with Resource Heaps](using-argument-buffers-with-resource-heaps.md)
  Reduce CPU overhead by using arrays inside argument buffers and combining them with resource heaps.
- [Implementing a Multistage Image Filter Using Heaps and Events](implementing-a-multistage-image-filter-using-heaps-and-events.md)
  Use events to synchronize access to resources allocated on a heap.
- [Implementing a Multistage Image Filter Using Heaps and Fences](implementing-a-multistage-image-filter-using-heaps-and-fences.md)
  Use fences to synchronize access to resources allocated on a heap.
- [protocol MTLHeap](mtlheap.md)
  A memory pool from which you can suballocate resources.
- [class MTLHeapDescriptor](mtlheapdescriptor.md)
  A configuration that customizes the behavior for a Metal memory heap.
- [struct MTLSizeAndAlign](mtlsizeandalign.md)
  The size and alignment of a resource, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheaptype)*