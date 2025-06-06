# indices

**Framework**: RealityKit  
**Kind**: property

The indices that are valid for subscripting the collection, in ascending order.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
var indices: DefaultIndices<Self> { get }
```

#### Discussion

A collection’s `indices` property can hold a strong reference to the collection itself, causing the collection to be non-uniquely referenced. If you mutate the collection while iterating over its indices, a strong reference can cause an unexpected copy of the collection. To avoid the unexpected copy, use the `index(after:)` method starting with `startIndex` to produce indices instead.

```None
var c = MyFancyCollection([10, 20, 30, 40, 50])
var i = c.startIndex
while i != c.endIndex {
    c[i] /= 5
    i = c.index(after: i)
}
// c == MyFancyCollection([2, 4, 6, 8, 10])
```

## See Also

- [func distance(from: Self.Index, to: Self.Index) -> Int](entity/childcollection/distance(from:to:).md)
  Returns the distance between two indices.
- [var startIndex: Int](entity/childcollection/startindex.md)
  The position of the first element in a nonempty collection. (See `Collection.startIndex`.)
- [var endIndex: Int](entity/childcollection/endindex.md)
  TThe collection’s “past the end” position—that is, the position one greater than the last valid subscript argument. (See `Collection.endIndex`.)
- [func firstIndex(of: Self.Element) -> Self.Index?](entity/childcollection/firstindex(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](entity/childcollection/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func formIndex(inout Self.Index, offsetBy: Int)](entity/childcollection/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](entity/childcollection/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func formIndex(after: inout Self.Index)](entity/childcollection/formindex(after:).md)
  Replaces the given index with its successor.
- [func index(Self.Index, offsetBy: Int) -> Self.Index](entity/childcollection/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](entity/childcollection/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: Int) -> Int](entity/childcollection/index(after:).md)
  Returns the position immediately after the given index. (See `Collection.index`.)
- [func index(of: Self.Element) -> Self.Index?](entity/childcollection/index(of:).md)
  Returns the first index where the specified value appears in the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/childcollection/indices-swift.property)*