# Entity.ChildCollection.IndexingIterator.Iterator

**Framework**: RealityKit  
**Kind**: typealias

A type that provides the sequence’s iteration interface and encapsulates its iteration state.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
typealias Iterator = Entity.ChildCollection.IndexingIterator<Elements>
```

## See Also

- [func enumerated() -> EnumeratedSequence<Self>](entity/childcollection/indexingiterator/enumerated.md)
  Returns a sequence of pairs (, ), where  represents a consecutive integer starting at zero and  represents an element of the sequence.
- [func next() -> Elements.Element?](entity/childcollection/indexingiterator/next.md)
  Advances to the next element and returns it, or `nil` if no next element exists.
- [func forEach((Self.Element) throws -> Void) rethrows](entity/childcollection/indexingiterator/foreach(_:).md)
  Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [func makeIterator() -> Self](entity/childcollection/indexingiterator/makeiterator.md)
  Returns an iterator over the elements of this sequence.
- [Entity.ChildCollection.IndexingIterator.Element](entity/childcollection/indexingiterator/element.md)
  The type of element traversed by the iterator.
- [var underestimatedCount: Int](entity/childcollection/indexingiterator/underestimatedcount.md)
  A value less than or equal to the number of elements in the sequence, calculated nondestructively.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/childcollection/indexingiterator/iterator)*