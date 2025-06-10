# IndexingIterator

**Framework**: Swift  
**Kind**: struct

A type that iterates over a collection using its indices.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@frozen
struct IndexingIterator<Elements> where Elements : Collection
```

#### Overview

The `IndexingIterator` type is the default iterator for any collection that doesn’t declare its own. It acts as an iterator by using a collection’s indices to step over each value in the collection. Most collections in the standard library use `IndexingIterator` as their iterator.

By default, any custom collection type you create will inherit a `makeIterator()` method that returns an `IndexingIterator` instance, making it unnecessary to declare your own. When creating a custom collection type, add the minimal requirements of the `Collection` protocol: starting and ending indices and a subscript for accessing elements. With those elements defined, the inherited `makeIterator()` method satisfies the requirements of the `Sequence` protocol.

Here’s an example of a type that declares the minimal requirements for a collection. The `CollectionOfTwo` structure is a fixed-size collection that always holds two elements of a specific type.

```swift
struct CollectionOfTwo<Element>: Collection {
    let elements: (Element, Element)

    init(_ first: Element, _ second: Element) {
        self.elements = (first, second)
    }

    var startIndex: Int { return 0 }
    var endIndex: Int   { return 2 }

    subscript(index: Int) -> Element {
        switch index {
        case 0: return elements.0
        case 1: return elements.1
        default: fatalError("Index out of bounds.")
        }
    }
    
    func index(after i: Int) -> Int {
        precondition(i < endIndex, "Can't advance beyond endIndex")
        return i + 1
    }
}
```

Because `CollectionOfTwo` doesn’t define its own `makeIterator()` method or `Iterator` associated type, it uses the default iterator type, `IndexingIterator`. This example shows how a `CollectionOfTwo` instance can be created holding the values of a point, and then iterated over using a `for`-`in` loop.

```swift
let point = CollectionOfTwo(15.0, 20.0)
for element in point {
    print(element)
}
// Prints "15.0"
// Prints "20.0"
```

## Topics

### Type Aliases
- [IndexingIterator.SubSequence](indexingiterator/subsequence.md)
### Default Implementations
- [IteratorProtocol Implementations](indexingiterator/iteratorprotocol-implementations.md)
- [Sequence Implementations](indexingiterator/sequence-implementations.md)

## Relationships

### Conforms To
- [Copyable](copyable.md)
- [IteratorProtocol](iteratorprotocol.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)
- [Sequence](sequence.md)

## See Also

- [struct IteratorSequence](iteratorsequence.md)
  A sequence built around an iterator of type `Base`.
- [typealias EnumeratedIterator](enumeratediterator.md)
- [typealias SetIterator](setiterator.md)
- [struct StrideThroughIterator](stridethroughiterator.md)
  An iterator for a `StrideThrough` instance.
- [struct StrideToIterator](stridetoiterator.md)
  An iterator for a `StrideTo` instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/indexingiterator)*