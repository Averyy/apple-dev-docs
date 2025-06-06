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

O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the absolute value of `distance`.

## Parameters

- `i`: A valid index of the collection.
- `distance`: The distance to offset  .   must not be negative   unless the collection conforms to the    protocol.

## See Also

- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](rowgrouping/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](rowgrouping/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](rowgrouping/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/rowgrouping/formindex(_:offsetby:))*