# index(_:offsetBy:)

**Framework**: TabularData  
**Kind**: method

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
func index(_ i: Self.Index, offsetBy distance: Int) -> Self.Index
```

## See Also

- [var indices: DefaultIndices<Self>](filledcolumn/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [func firstIndex(of: Self.Element) -> Self.Index?](filledcolumn/firstindex(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](filledcolumn/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](filledcolumn/index(_:offsetby:limitedby:).md)
- [func formIndex(inout Self.Index, offsetBy: Int)](filledcolumn/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](filledcolumn/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func index(of: Self.Element) -> Self.Index?](filledcolumn/index(of:).md)
  Returns the first index where the specified value appears in the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/filledcolumn/index(_:offsetby:))*