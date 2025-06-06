# update(fromContentsOf:)

**Framework**: Swift  
**Kind**: method

Updates the buffer’s initialized memory with every element of the source.

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
func update(fromContentsOf source: some Collection<Element>) -> UnsafeMutableBufferPointer<Element>.Index
```

#### Return Value

An index one past the index of the last element updated.

#### Discussion

Prior to calling the `update(fromContentsOf:)` method on a buffer, the first `source.count` elements of the buffer’s memory must be initialized, or the buffer’s `Element` type must be a trivial type. The buffer must reference enough initialized memory to accommodate `source.count` elements.

The returned index is one past the index of the last element updated. If `source` contains no elements, the returned index is equal to the buffer’s `startIndex`. If `source` contains as many elements as the buffer can hold, the returned index is equal to the buffer’s `endIndex`.

> **Note**: The memory regions referenced by `source` and this buffer may overlap.

The memory regions referenced by `source` and this buffer may overlap.

> **Note**: `self.count` >= `source.count`

`self.count` >= `source.count`

## Parameters

- `source`: A collection of elements to be used to update   the buffer’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablebufferpointer/update(fromcontentsof:))*