# count

**Framework**: RealityKit  
**Kind**: property

The number of elements in the collection.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
var count: Int { get }
```

#### Discussion

To check whether a collection is empty, use its `isEmpty` property instead of comparing `count` to zero. Unless the collection guarantees random-access performance, calculating `count` can be an O() operation.

> **Note**: O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the length of the collection.

O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the length of the collection.

## See Also

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
- [var underestimatedCount: Int](jointtransforms/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/jointtransforms/count)*