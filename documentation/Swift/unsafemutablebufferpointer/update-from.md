# update(from:)

**Framework**: Swift  
**Kind**: method

Updates the buffer’s initialized memory with the given elements.

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
func update<S>(from source: S) -> (unwritten: S.Iterator, index: UnsafeMutableBufferPointer<Element>.Index) where Element == S.Element, S : Sequence
```

#### Return Value

An iterator to any elements of `source` that didn’t fit in the buffer, and the index one past the last updated element in the buffer.

#### Discussion

The buffer’s memory must be initialized or its `Element` type must be a trivial type.

## Parameters

- `source`: A sequence of elements to be used to update   the buffer’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablebufferpointer/update(from:))*