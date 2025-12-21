# maxAvailableSize(alignment:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

The maximum size of a resource, in bytes, that can be currently allocated from the heap.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func maxAvailableSize(alignment: Int) -> Int
```

#### Return Value

The maximum size for the resource, in bytes.

#### Discussion

This method measures fragmentation within the heap. You can use the [`heapBufferSizeAndAlign(length:options:)`](mtldevice/heapbuffersizeandalign(length:options:).md) and [`heapTextureSizeAndAlign(descriptor:)`](mtldevice/heaptexturesizeandalign(descriptor:).md) methods to help you determine the correct alignment for the resource.

## Parameters

- `alignment`: The alignment of the resource, in bytes. This value needs to be a power of two.

## See Also

- [var size: Int](mtlheap/size.md)
  The total size of the heap, in bytes.
- [var usedSize: Int](mtlheap/usedsize.md)
  The size of all resources currently in the heap, in bytes.
- [var currentAllocatedSize: Int](mtlheap/currentallocatedsize.md)
  The size, in bytes, of the current heap allocation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheap/maxavailablesize(alignment:))*