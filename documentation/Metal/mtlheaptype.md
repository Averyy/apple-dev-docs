# MTLHeapType

**Framework**: Metal  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum MTLHeapType : NSInteger;
```

## Topics

### Specifying the heap type
- [MTLHeapType.automatic](./mtlheaptype/automatic.md)
  A heap that automatically places new resource allocations.
- [MTLHeapType.placement](./mtlheaptype/placement.md)
  The app controls placement of resources on the heap.
- [MTLHeapType.sparse](./mtlheaptype/sparse.md)
  The heap contains sparse texture tiles.
### Initializers
- [init?(rawValue: Int)](./mtlheaptype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Resource memory allocation and management
- [Using argument buffers with resource heaps](./using-argument-buffers-with-resource-heaps.md)
  Reduce CPU overhead by using arrays inside argument buffers and combining them with resource heaps.
- [Implementing a multistage image filter using heaps and events](./implementing-a-multistage-image-filter-using-heaps-and-events.md)
  Use events to synchronize access to resources allocated on a heap.
- [Implementing a multistage image filter using heaps and fences](./implementing-a-multistage-image-filter-using-heaps-and-fences.md)
  Use fences to synchronize access to resources allocated on a heap.
- [protocol MTLHeap](./mtlheap.md)
  A memory pool from which you can suballocate resources.
- [class MTLHeapDescriptor](./mtlheapdescriptor.md)
  A configuration that customizes the behavior for a Metal memory heap.
- [struct MTLSizeAndAlign](./mtlsizeandalign.md)
  The size and alignment of a resource, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheaptype)*