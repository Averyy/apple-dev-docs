# MTLHeapType.automatic

**Framework**: Metal  
**Kind**: case  
**Role**: Case

A heap that automatically places new resource allocations.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
case automatic
```

```c
MTLHeapTypeAutomatic
```

#### Discussion

In an automatic heap, Metal automatically determines the locations of resources allocated by the heap, with a layout specific to the GPU. Automatic heaps may perform better than manually placing resources in the heap ([`MTLHeapType.placement`](./placement.md)).

Use automatic heaps when the heap primarily contains temporary resources that you write to often.

## See Also

### Specifying the heap type
- [MTLHeapType.placement](./placement.md)
  The app controls placement of resources on the heap.
- [MTLHeapType.sparse](./sparse.md)
  The heap contains sparse texture tiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheaptype/automatic)*