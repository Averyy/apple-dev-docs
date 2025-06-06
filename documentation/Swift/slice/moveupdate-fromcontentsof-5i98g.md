# moveUpdate(fromContentsOf:)

**Framework**: Swift  
**Kind**: method

Updates this buffer slice’s initialized memory initialized memory by moving every element from the source buffer, leaving the source memory uninitialized.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func moveUpdate<Element>(fromContentsOf source: UnsafeMutableBufferPointer<Element>) -> Slice<Base>.Index where Base == UnsafeMutableBufferPointer<Element>
```

#### Return Value

An index one past the index of the last element updated.

#### Discussion

The region of memory starting at the beginning of this buffer slice and covering `source.count` instances of its `Element` type  must be initialized, or its `Element` type must be a trivial type. After calling `moveUpdate(fromContentsOf:)`, the region of memory underlying `source` is uninitialized. The buffer slice must reference enough initialized memory to accommodate `source.count` elements.

The returned index is one past the index of the last element updated. If `source` contains no elements, the returned index is equal to the buffer’s `startIndex`. If `source` contains as many elements as the buffer slice can hold, the returned index is equal to the slice’s `endIndex`.

> **Note**: The memory regions referenced by `source` and this buffer slice must not overlap.

> **Note**: `self.count` >= `source.count`

## Parameters

- `source`: A buffer containing the values to move.   The memory region underlying   must be initialized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/slice/moveupdate(fromcontentsof:)-5i98g)*