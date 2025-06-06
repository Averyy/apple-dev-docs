# isEmpty

**Framework**: RealityKit  
**Kind**: property

A Boolean value indicating whether the collection is empty.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
var isEmpty: Bool { get }
```

#### Discussion

When you need to check whether your collection is empty, use the `isEmpty` property instead of checking that the `count` property is equal to zero. For collections that don’t conform to `RandomAccessCollection`, accessing the `count` property iterates through the elements of the collection.

```None
let horseName = "Silver"
if horseName.isEmpty {
    print("My horse has no name.")
} else {
    print("Hi ho, \(horseName)!")
}
// Prints "Hi ho, Silver!")
```

> **Note**: O(1)

O(1)

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
- [var last: Self.Element?](jointtransforms/last.md)
  The last element of the collection.
- [var lazy: LazySequence<Self>](jointtransforms/lazy.md)
  A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.
- [var publisher: Publishers.Sequence<Self, Never>](jointtransforms/publisher.md)
- [var underestimatedCount: Int](jointtransforms/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/jointtransforms/isempty)*