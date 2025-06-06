# MTLHeapType.automatic

**Framework**: Metal  
**Kind**: case

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

#### Discussion

In an automatic heap, Metal automatically determines the locations of resources allocated by the heap, with a layout specific to the GPU. Automatic heaps may perform better than manually placing resources in the heap ([`MTLHeapType.placement`](mtlheaptype/placement.md)).

Use automatic heaps when the heap primarily contains temporary resources that you write to often.

## See Also

- [MTLHeapType.placement](mtlheaptype/placement.md)
  The app controls placement of resources on the heap.
- [MTLHeapType.sparse](mtlheaptype/sparse.md)
  The heap contains sparse texture tiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheaptype/automatic)*