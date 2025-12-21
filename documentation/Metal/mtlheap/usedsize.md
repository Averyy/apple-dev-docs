# usedSize

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The size of all resources currently in the heap, in bytes.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var usedSize: Int { get }
```

## See Also

- [func maxAvailableSize(alignment: Int) -> Int](mtlheap/maxavailablesize(alignment:).md)
  The maximum size of a resource, in bytes, that can be currently allocated from the heap.
- [var size: Int](mtlheap/size.md)
  The total size of the heap, in bytes.
- [var currentAllocatedSize: Int](mtlheap/currentallocatedsize.md)
  The size, in bytes, of the current heap allocation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheap/usedsize)*