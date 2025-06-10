# formIndex(_:offsetBy:)

**Framework**: TabularData  
**Kind**: method

Offsets the given index by the specified distance.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func formIndex(_ i: inout Self.Index, offsetBy distance: Int)
```

#### Discussion

The value passed as `distance` must not offset `i` beyond the bounds of the collection.

> **Note**: O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the absolute value of `distance`.

## Parameters

- `i`: A valid index of the collection.
- `distance`: The distance to offset  .   must not be negative   unless the collection conforms to the    protocol.

## See Also

- [var indices: DefaultIndices<Self>](filledcolumn/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [func firstIndex(of: Self.Element) -> Self.Index?](filledcolumn/firstindex(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](filledcolumn/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func index(Self.Index, offsetBy: Int) -> Self.Index](filledcolumn/index(_:offsetby:).md)
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](filledcolumn/index(_:offsetby:limitedby:).md)
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](filledcolumn/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func index(of: Self.Element) -> Self.Index?](filledcolumn/index(of:).md)
  Returns the first index where the specified value appears in the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/filledcolumn/formindex(_:offsetby:))*