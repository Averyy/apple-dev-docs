# Scene.AnchorCollection.Iterator

**Framework**: RealityKit  
**Kind**: typealias

An iterator that presents the elements of the collection.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
typealias Iterator = Entity.ChildCollection.IndexingIterator<Scene.AnchorCollection>
```

## See Also

- [func makeIterator() -> Scene.AnchorCollection.Iterator](scene/anchorcollection/makeiterator.md)
  Returns an iterator over the elements of the collection.
- [Scene.AnchorCollection.Element](scene/anchorcollection/element.md)
  The type of element traversed by the iterator.
- [func forEach((Self.Element) throws -> Void) rethrows](scene/anchorcollection/foreach(_:).md)
  Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [func enumerated() -> EnumeratedSequence<Self>](scene/anchorcollection/enumerated.md)
  Returns a sequence of pairs (, ), where  represents a consecutive integer starting at zero and  represents an element of the sequence.
- [var underestimatedCount: Int](scene/anchorcollection/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/anchorcollection/iterator)*