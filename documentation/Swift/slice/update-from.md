# update(from:)

**Framework**: Swift  
**Kind**: method

Updates the buffer slice’s initialized memory with the given elements.

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
func update<S>(from source: S) -> (unwritten: S.Iterator, index: Slice<Base>.Index) where Base == UnsafeMutableBufferPointer<S.Element>, S : Sequence
```

#### Return Value

An iterator to any elements of `source` that didn’t fit in the buffer slice, and the index one past the last updated element.

#### Discussion

The buffer slice’s memory must be initialized or its `Element` type must be a trivial type.

## Parameters

- `source`: A sequence of elements to be used to update   the contents of the buffer slice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/slice/update(from:))*