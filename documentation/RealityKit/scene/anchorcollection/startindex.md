# startIndex

**Framework**: RealityKit  
**Kind**: property

The position of the first element in a nonempty collection.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var startIndex: Int { get }
```

#### Discussion

If the collection is empty, `startIndex` is equal to `endIndex`.

## See Also

- [Scene.AnchorCollection.Index](scene/anchorcollection/index.md)
  A type that represents a position in the collection.
- [Scene.AnchorCollection.Indices](scene/anchorcollection/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
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
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](scene/anchorcollection/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func formIndex(after: inout Self.Index)](scene/anchorcollection/formindex(after:).md)
  Replaces the given index with its successor.
- [func distance(from: Self.Index, to: Self.Index) -> Int](scene/anchorcollection/distance(from:to:).md)
  Returns the distance between two indices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/anchorcollection/startindex)*