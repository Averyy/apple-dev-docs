# moveUpdate(fromContentsOf:)

**Framework**: Swift  
**Kind**: method

Updates this buffer’s initialized memory by moving every element from the source buffer, leaving the source memory uninitialized.

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
func moveUpdate(fromContentsOf source: UnsafeMutableBufferPointer<Element>) -> UnsafeMutableBufferPointer<Element>.Index
```

#### Return Value

An index one past the index of the last element updated.

#### Discussion

Prior to calling the `moveUpdate(fromContentsOf:)` method on a buffer, the first `source.count` elements of the buffer’s memory must be initialized, or the buffer’s `Element` type must be a trivial type. The memory referenced by `source` is uninitialized after the function returns. The buffer must reference enough initialized memory to accommodate `source.count` elements.

The returned index is one past the index of the last element updated. If `source` contains no elements, the returned index is equal to the buffer’s `startIndex`. If `source` contains as many elements as the buffer can hold, the returned index is equal to the buffer’s `endIndex`.

> **Note**: The memory regions referenced by `source` and this buffer must not overlap.

> **Note**: `self.count` >= `source.count`

## Parameters

- `source`: A buffer containing the values to move.   The memory region underlying   must be initialized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablebufferpointer/moveupdate(fromcontentsof:)-522y2)*