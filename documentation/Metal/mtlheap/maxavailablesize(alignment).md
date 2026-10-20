# maxAvailableSize(alignment:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (NSUInteger) maxAvailableSizeWithAlignment:(NSUInteger) alignment;
```

#### Return Value

The maximum size for the resource, in bytes.

#### Discussion

This method measures fragmentation within the heap. You can use the [`heapBufferSizeAndAlign(length:options:)`](../mtldevice/heapbuffersizeandalign%28length,options%29.md) and [`heapTextureSizeAndAlign(descriptor:)`](../mtldevice/heaptexturesizeandalign%28descriptor%29.md) methods to help you determine the correct alignment for the resource.

## Parameters

- `alignment`: The alignment of the resource, in bytes. This value needs to be a power of two.

## See Also

### Checking a heap’s size information
- [var size: Int](./size.md)
  The total size of the heap, in bytes.
- [var usedSize: Int](./usedsize.md)
  The size of all resources currently in the heap, in bytes.
- [var currentAllocatedSize: Int](./currentallocatedsize.md)
  The size, in bytes, of the current heap allocation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheap/maxavailablesize(alignment:))*