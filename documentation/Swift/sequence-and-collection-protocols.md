# Sequence and Collection Protocols

**Framework**: Swift

Write generic code that works with any collection, or build your own collection types.

## Topics

### First Steps
- [protocol Sequence](sequence.md)
  A type that provides sequential, iterated access to its elements.
- [protocol Collection](collection.md)
  A sequence whose elements can be traversed multiple times, nondestructively, and accessed by an indexed subscript.
### Collection Traversal
- [protocol BidirectionalCollection](bidirectionalcollection.md)
  A collection that supports backward as well as forward traversal.
- [protocol RandomAccessCollection](randomaccesscollection.md)
  A collection that supports efficient random-access index traversal.
### Collection Mutability
- [protocol MutableCollection](mutablecollection.md)
  A collection that supports subscript assignment.
- [protocol RangeReplaceableCollection](rangereplaceablecollection.md)
  A collection that supports replacement of an arbitrary subrange of elements with the elements of another collection.
### Manual Iteration
- [protocol IteratorProtocol](iteratorprotocol.md)
  A type that supplies the values of a sequence one at a time.
### Algebraic Sets
- [protocol SetAlgebra](setalgebra.md)
  A type that provides mathematical set operations.
### Lazy Collections
- [protocol LazySequenceProtocol](lazysequenceprotocol.md)
  A sequence on which normally-eager sequence operations are implemented lazily.
- [protocol LazyCollectionProtocol](lazycollectionprotocol.md)

## See Also

- [Supporting Types](supporting-types.md)
  Use wrappers, indices, and iterators in operations like slicing, flattening, and reversing a collection.
- [Managed Buffers](managed-buffers.md)
  Build your own buffer-backed collection types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/sequence-and-collection-protocols)*