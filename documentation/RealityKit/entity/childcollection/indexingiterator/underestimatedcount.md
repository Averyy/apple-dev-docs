# underestimatedCount

**Framework**: RealityKit  
**Kind**: property

A value less than or equal to the number of elements in the sequence, calculated nondestructively.

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

The default implementation returns 0. If you provide your own implementation, make sure to compute the value nondestructively.

> **Note**: O(1), except if the sequence also conforms to `Collection`. In this case, see the documentation of `Collection.underestimatedCount`.

O(1), except if the sequence also conforms to `Collection`. In this case, see the documentation of `Collection.underestimatedCount`.

## See Also

- [func enumerated() -> EnumeratedSequence<Self>](entity/childcollection/indexingiterator/enumerated.md)
  Returns a sequence of pairs (, ), where  represents a consecutive integer starting at zero and  represents an element of the sequence.
- [func next() -> Elements.Element?](entity/childcollection/indexingiterator/next.md)
  Advances to the next element and returns it, or `nil` if no next element exists.
- [func forEach((Self.Element) throws -> Void) rethrows](entity/childcollection/indexingiterator/foreach(_:).md)
  Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [func makeIterator() -> Self](entity/childcollection/indexingiterator/makeiterator.md)
  Returns an iterator over the elements of this sequence.
- [Entity.ChildCollection.IndexingIterator.Iterator](entity/childcollection/indexingiterator/iterator.md)
  A type that provides the sequence’s iteration interface and encapsulates its iteration state.
- [Entity.ChildCollection.IndexingIterator.Element](entity/childcollection/indexingiterator/element.md)
  The type of element traversed by the iterator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/childcollection/indexingiterator/underestimatedcount)*