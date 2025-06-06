# formIndex(_:offsetBy:limitedBy:)

**Framework**: Realitykit  
**Kind**: method

Offsets the given index by the specified distance, or so that it equals the given limiting index.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
func formIndex(_ i: inout Self.Index, offsetBy distance: Int, limitedBy limit: Self.Index) -> Bool
```

#### Return Value

`true` if `i` has been offset by exactly `distance` steps without going beyond `limit`; otherwise, `false`. When the return value is `false`, the value of `i` is equal to `limit`.

#### Discussion

The value passed as `distance` must not offset `i` beyond the bounds of the collection, unless the index passed as `limit` prevents offsetting beyond those bounds.

> **Note**: O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the absolute value of `distance`.

## Parameters

- `i`: A valid index of the collection.
- `distance`: The distance to offset  .   must not be negative   unless the collection conforms to the    protocol.
- `limit`: A valid index of the collection to use as a limit. If   , a limit that is less than   has no effect.   Likewise, if  , a limit that is greater than   has no   effect.

## See Also

- [Scene.AnchorCollection.Index](scene/anchorcollection/index.md)
  A type that represents a position in the collection.
- [Scene.AnchorCollection.Indices](scene/anchorcollection/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [var startIndex: Int](scene/anchorcollection/startindex.md)
  The position of the first element in a nonempty collection.
- [var endIndex: Int](scene/anchorcollection/endindex.md)
  The position one greater than the last valid subscript argument.
- [var indices: DefaultIndices<Self>](scene/anchorcollection/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [func index(Self.Index, offsetBy: Int) -> Self.Index](scene/anchorcollection/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](scene/anchorcollection/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: Int) -> Int](scene/anchorcollection/index(after:).md)
  Returns the position immediately after the given index.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](scene/anchorcollection/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func formIndex(inout Self.Index, offsetBy: Int)](scene/anchorcollection/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(after: inout Self.Index)](scene/anchorcollection/formindex(after:).md)
  Replaces the given index with its successor.
- [func distance(from: Self.Index, to: Self.Index) -> Int](scene/anchorcollection/distance(from:to:).md)
  Returns the distance between two indices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/anchorcollection/formindex(_:offsetby:limitedby:))*