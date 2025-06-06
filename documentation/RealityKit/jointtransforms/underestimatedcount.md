# underestimatedCount

**Framework**: RealityKit  
**Kind**: property

A value less than or equal to the number of elements in the collection.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
var underestimatedCount: Int { get }
```

#### Discussion

> **Note**: O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the length of the collection.

O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the length of the collection.

## See Also

- [var count: Int](jointtransforms/count.md)
  The number of elements in the collection.
- [var first: Self.Element?](jointtransforms/first.md)
  The first element of the collection.
- [var indices: DefaultIndices<Self>](jointtransforms/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var startIndex: JointTransforms.Index](jointtransforms/startindex.md)
  An index to the first joint transform in the collection.
- [var endIndex: JointTransforms.Index](jointtransforms/endindex.md)
  An index to the last joint transform in the collection.
- [var isEmpty: Bool](jointtransforms/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var last: Self.Element?](jointtransforms/last.md)
  The last element of the collection.
- [var lazy: LazySequence<Self>](jointtransforms/lazy.md)
  A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.
- [var publisher: Publishers.Sequence<Self, Never>](jointtransforms/publisher.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/jointtransforms/underestimatedcount)*