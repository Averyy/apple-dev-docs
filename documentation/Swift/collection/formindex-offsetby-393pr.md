# formIndex(_:offsetBy:)

**Framework**: Swift  
**Kind**: method

Offsets the given index by the specified distance.

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
func formIndex(_ i: inout Self.Index, offsetBy distance: Int)
```

#### Discussion

The value passed as `distance` must not offset `i` beyond the bounds of the collection.

> **Note**: O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the absolute value of `distance`.

O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the absolute value of `distance`.

## Parameters

- `i`: A valid index of the collection.
- `distance`: The distance to offset  .   must not be negative   unless the collection conforms to the    protocol.

## See Also

- [var startIndex: Self.Index](collection/startindex.md)
  The position of the first element in a nonempty collection.
- [var endIndex: Self.Index](collection/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var indices: Self.Indices](collection/indices-9kkbf.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [func index(after: Self.Index) -> Self.Index](collection/index(after:).md)
  Returns the position immediately after the given index.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](collection/formindex(_:offsetby:limitedby:)-6jwra.md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/collection/formindex(_:offsetby:)-393pr)*