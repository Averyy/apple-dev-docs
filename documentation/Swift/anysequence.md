# AnySequence

**Framework**: Swift  
**Kind**: struct

A type-erased sequence.

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
struct AnySequence<Element>
```

#### Overview

An instance of `AnySequence` forwards its operations to an underlying base sequence having the same `Element` type, hiding the specifics of the underlying sequence.

## Topics

### Initializers
- [init<I>(() -> I)](anysequence/init(_:)-25934.md)
  Creates a sequence whose `makeIterator()` method forwards to `makeUnderlyingIterator`.
- [init<S>(S)](anysequence/init(_:)-307a9.md)
  Creates a new sequence that wraps and forwards operations to `base`.
### Instance Methods
- [func drop(while: (Element) throws -> Bool) rethrows -> AnySequence<Element>](anysequence/drop(while:).md)
- [func dropFirst(Int) -> AnySequence<Element>](anysequence/dropfirst(_:).md)
- [func dropLast(Int) -> [Element]](anysequence/droplast(_:).md)
- [func filter((Element) throws -> Bool) rethrows -> [Element]](anysequence/filter(_:).md)
- [func forEach((Element) throws -> Void) rethrows](anysequence/foreach(_:).md)
- [func map<T, E>((Element) throws(E) -> T) throws(E) -> [T]](anysequence/map(_:).md)
- [func prefix(Int) -> AnySequence<Element>](anysequence/prefix(_:).md)
- [func prefix(while: (Element) throws -> Bool) rethrows -> [Element]](anysequence/prefix(while:).md)
- [func suffix(Int) -> [Element]](anysequence/suffix(_:).md)
### Default Implementations
- [Sequence Implementations](anysequence/sequence-implementations.md)

## Relationships

### Conforms To
- [Copyable](copyable.md)
- [Sequence](sequence.md)

## See Also

- [struct AnyCollection](anycollection.md)
  A type-erased wrapper over any collection with indices that support forward traversal.
- [struct AnyBidirectionalCollection](anybidirectionalcollection.md)
  A type-erased wrapper over any collection with indices that support bidirectional traversal.
- [struct AnyRandomAccessCollection](anyrandomaccesscollection.md)
  A type-erased wrapper over any collection with indices that support random access traversal.
- [struct AnyIterator](anyiterator.md)
  A type-erased iterator of `Element`.
- [struct AnyIndex](anyindex.md)
  A wrapper over an underlying index that hides the specific underlying type.
- [struct AnyHashable](anyhashable.md)
  A type-erased hashable value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/anysequence)*