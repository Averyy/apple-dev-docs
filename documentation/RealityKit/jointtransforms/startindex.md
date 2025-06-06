# startIndex

**Framework**: RealityKit  
**Kind**: property

An index to the first joint transform in the collection.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
var startIndex: JointTransforms.Index { get }
```

#### Discussion

For more on the sequence’s beginning index, see [`startIndex`](https://developer.apple.com/documentation/Swift/Array/startIndex).

## See Also

- [var count: Int](jointtransforms/count.md)
  The number of elements in the collection.
- [var first: Self.Element?](jointtransforms/first.md)
  The first element of the collection.
- [var indices: DefaultIndices<Self>](jointtransforms/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var endIndex: JointTransforms.Index](jointtransforms/endindex.md)
  An index to the last joint transform in the collection.
- [var isEmpty: Bool](jointtransforms/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var last: Self.Element?](jointtransforms/last.md)
  The last element of the collection.
- [var lazy: LazySequence<Self>](jointtransforms/lazy.md)
  A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.
- [var publisher: Publishers.Sequence<Self, Never>](jointtransforms/publisher.md)
- [var underestimatedCount: Int](jointtransforms/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/jointtransforms/startindex)*