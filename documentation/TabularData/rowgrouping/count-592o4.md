# count

**Framework**: TabularData  
**Kind**: property

The number of elements in the collection.

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
var count: Int { get }
```

#### Discussion

To check whether a collection is empty, use its `isEmpty` property instead of comparing `count` to zero. Unless the collection guarantees random-access performance, calculating `count` can be an O() operation.

> **Note**: O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the length of the collection.

O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the length of the collection.

## See Also

- [var isEmpty: Bool](rowgrouping/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var underestimatedCount: Int](rowgrouping/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.
- [func makeIterator() -> IndexingIterator<Self>](rowgrouping/makeiterator.md)
  Returns an iterator over the elements of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/rowgrouping/count-592o4)*