# AnyBidirectionalCollection

**Framework**: Swift  
**Kind**: struct

A type-erased wrapper over any collection with indices that support bidirectional traversal.

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
struct AnyBidirectionalCollection<Element>
```

#### Overview

An `AnyBidirectionalCollection` instance forwards its operations to a base collection having the same `Element` type, hiding the specifics of the underlying collection.

## Topics

### Initializers
- [init?(AnyCollection<Element>)](anybidirectionalcollection/init(_:)-1hwm5.md)
  Creates an `AnyBidirectionalCollection` having the same underlying collection as `other`.
- [init<C>(C)](anybidirectionalcollection/init(_:)-2kvez.md)
  Creates a type-erased collection that wraps the given collection.
- [init(AnyRandomAccessCollection<Element>)](anybidirectionalcollection/init(_:)-4hewp.md)
  Creates an `AnyBidirectionalCollection` having the same underlying collection as `other`.
- [init<C>(C)](anybidirectionalcollection/init(_:)-5lybd.md)
  Creates a type-erased collection that wraps the given collection.
- [init(AnyBidirectionalCollection<Element>)](anybidirectionalcollection/init(_:)-61joz.md)
  Creates an `AnyBidirectionalCollection` having the same underlying collection as `other`.
### Instance Methods
- [func drop(while: (Element) throws -> Bool) rethrows -> AnyBidirectionalCollection<Element>](anybidirectionalcollection/drop(while:).md)
- [func dropFirst(Int) -> AnyBidirectionalCollection<Element>](anybidirectionalcollection/dropfirst(_:).md)
- [func dropLast(Int) -> AnyBidirectionalCollection<Element>](anybidirectionalcollection/droplast(_:).md)
- [func filter((Element) throws -> Bool) rethrows -> [Element]](anybidirectionalcollection/filter(_:).md)
- [func forEach((Element) throws -> Void) rethrows](anybidirectionalcollection/foreach(_:).md)
- [func formIndex(inout AnyBidirectionalCollection<Element>.Index, offsetBy: Int)](anybidirectionalcollection/formindex(_:offsetby:).md)
- [func formIndex(inout AnyBidirectionalCollection<Element>.Index, offsetBy: Int, limitedBy: AnyBidirectionalCollection<Element>.Index) -> Bool](anybidirectionalcollection/formindex(_:offsetby:limitedby:).md)
- [func map<T, E>((Element) throws(E) -> T) throws(E) -> [T]](anybidirectionalcollection/map(_:).md)
- [func prefix(Int) -> AnyBidirectionalCollection<Element>](anybidirectionalcollection/prefix(_:).md)
- [func prefix(while: (Element) throws -> Bool) rethrows -> AnyBidirectionalCollection<Element>](anybidirectionalcollection/prefix(while:).md)
- [func suffix(Int) -> AnyBidirectionalCollection<Element>](anybidirectionalcollection/suffix(_:).md)
### Default Implementations
- [BidirectionalCollection Implementations](anybidirectionalcollection/bidirectionalcollection-implementations.md)
- [Collection Implementations](anybidirectionalcollection/collection-implementations.md)
- [Sequence Implementations](anybidirectionalcollection/sequence-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](bidirectionalcollection.md)
- [Collection](collection.md)
- [Copyable](copyable.md)
- [Sequence](sequence.md)

## See Also

- [struct AnySequence](anysequence.md)
  A type-erased sequence.
- [struct AnyCollection](anycollection.md)
  A type-erased wrapper over any collection with indices that support forward traversal.
- [struct AnyRandomAccessCollection](anyrandomaccesscollection.md)
  A type-erased wrapper over any collection with indices that support random access traversal.
- [struct AnyIterator](anyiterator.md)
  A type-erased iterator of `Element`.
- [struct AnyIndex](anyindex.md)
  A wrapper over an underlying index that hides the specific underlying type.
- [struct AnyHashable](anyhashable.md)
  A type-erased hashable value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/anybidirectionalcollection)*