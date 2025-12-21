# currentAllocatedSize

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The size, in bytes, of the current heap allocation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var currentAllocatedSize: Int { get }
```

## See Also

- [func maxAvailableSize(alignment: Int) -> Int](mtlheap/maxavailablesize(alignment:).md)
  The maximum size of a resource, in bytes, that can be currently allocated from the heap.
- [var size: Int](mtlheap/size.md)
  The total size of the heap, in bytes.
- [var usedSize: Int](mtlheap/usedsize.md)
  The size of all resources currently in the heap, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheap/currentallocatedsize)*