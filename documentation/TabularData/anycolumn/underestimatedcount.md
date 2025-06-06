# underestimatedCount

**Framework**: TabularData  
**Kind**: property

A value less than or equal to the number of elements in the collection.

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
var underestimatedCount: Int { get }
```

#### Discussion

> **Note**: O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the length of the collection.

O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the length of the collection.

## See Also

- [var isEmpty: Bool](anycolumn/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [func makeIterator() -> IndexingIterator<Self>](anycolumn/makeiterator.md)
  Returns an iterator over the elements of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/anycolumn/underestimatedcount)*