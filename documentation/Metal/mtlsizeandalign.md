# MTLSizeAndAlign

**Framework**: Metal  
**Kind**: struct

The size and alignment of a resource, in bytes.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct MTLSizeAndAlign
```

## Topics

### Accessing the Size and Alignment
- [var size: Int](mtlsizeandalign/size.md)
  The size of a resource, in bytes.
- [var align: Int](mtlsizeandalign/align.md)
  The alignment of a resource, in bytes.
### Creating Instances
- [init()](mtlsizeandalign/init.md)
  Creates a default instance.
- [init(size: Int, align: Int)](mtlsizeandalign/init(size:align:).md)
  Creates a new instance initialized to the given values.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

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
- [enum MTLHeapType](mtlheaptype.md)
  The options you use to choose the heap type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsizeandalign)*