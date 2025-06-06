# next()

**Framework**: RealityKit  
**Kind**: method

Advances to the next element and returns it, or `nil` if no next element exists.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
mutating func next() -> Elements.Element?
```

#### Return Value

The next element in the underlying sequence, if a next element exists; otherwise, `nil`.

#### Discussion

Repeatedly calling this method returns, in order, all the elements of the underlying sequence. As soon as the sequence has run out of elements, all subsequent calls return `nil`.

You must not call this method if any other copy of this iterator has been advanced with a call to its `next()` method.

The following example shows how an iterator can be used explicitly to emulate a `for`-`in` loop. First, retrieve a sequence’s iterator, and then call the iterator’s `next()` method until it returns `nil`.

```None
let numbers = [2, 3, 5, 7]
var numbersIterator = numbers.makeIterator()

while let num = numbersIterator.next() {
    print(num)
}
// Prints "2"
// Prints "3"
// Prints "5"
// Prints "7"
```

## See Also

- [func enumerated() -> EnumeratedSequence<Self>](entity/childcollection/indexingiterator/enumerated.md)
  Returns a sequence of pairs (, ), where  represents a consecutive integer starting at zero and  represents an element of the sequence.
- [func forEach((Self.Element) throws -> Void) rethrows](entity/childcollection/indexingiterator/foreach(_:).md)
  Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [func makeIterator() -> Self](entity/childcollection/indexingiterator/makeiterator.md)
  Returns an iterator over the elements of this sequence.
- [Entity.ChildCollection.IndexingIterator.Iterator](entity/childcollection/indexingiterator/iterator.md)
  A type that provides the sequence’s iteration interface and encapsulates its iteration state.
- [Entity.ChildCollection.IndexingIterator.Element](entity/childcollection/indexingiterator/element.md)
  The type of element traversed by the iterator.
- [var underestimatedCount: Int](entity/childcollection/indexingiterator/underestimatedcount.md)
  A value less than or equal to the number of elements in the sequence, calculated nondestructively.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/childcollection/indexingiterator/next())*