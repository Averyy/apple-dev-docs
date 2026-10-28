# MTLHeapType.placement

**Framework**: Metal  
**Kind**: case  
**Role**: Case

The app controls placement of resources on the heap.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
case placement
```

```c
MTLHeapTypePlacement
```

## Discussion

Use placement heaps when you need direct control over memory use and heap fragmentation. Typically, you use placement heaps for resources you keep for long time periods and rarely change.

## See Also

### Specifying the heap type
- [MTLHeapType.automatic](./automatic.md)
  A heap that automatically places new resource allocations.
- [MTLHeapType.sparse](./sparse.md)
  The heap contains sparse texture tiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheaptype/placement)*