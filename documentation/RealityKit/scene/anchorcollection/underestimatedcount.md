# underestimatedCount

**Framework**: Realitykit  
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

## See Also

- [func makeIterator() -> Scene.AnchorCollection.Iterator](scene/anchorcollection/makeiterator.md)
  Returns an iterator over the elements of the collection.
- [Scene.AnchorCollection.Iterator](scene/anchorcollection/iterator.md)
  An iterator that presents the elements of the collection.
- [Scene.AnchorCollection.Element](scene/anchorcollection/element.md)
  The type of element traversed by the iterator.
- [func forEach((Self.Element) throws -> Void) rethrows](scene/anchorcollection/foreach(_:).md)
  Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [func enumerated() -> EnumeratedSequence<Self>](scene/anchorcollection/enumerated.md)
  Returns a sequence of pairs (, ), where  represents a consecutive integer starting at zero and  represents an element of the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/anchorcollection/underestimatedcount)*