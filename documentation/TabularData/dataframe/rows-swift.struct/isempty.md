# isEmpty

**Framework**: Tabulardata  
**Kind**: property

A Boolean value indicating whether the collection is empty.

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

## See Also

- [var underestimatedCount: Int](dataframe/rows-swift.struct/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.
- [func makeIterator() -> IndexingIterator<Self>](dataframe/rows-swift.struct/makeiterator.md)
  Returns an iterator over the elements of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/rows-swift.struct/isempty)*