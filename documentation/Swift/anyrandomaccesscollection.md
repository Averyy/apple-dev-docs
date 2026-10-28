# AnyRandomAccessCollection

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

A type-erased wrapper over any collection with indices that support random access traversal.

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
struct AnyRandomAccessCollection<Element>
```

## Overview

An `AnyRandomAccessCollection` instance forwards its operations to a base collection having the same `Element` type, hiding the specifics of the underlying collection.

## Topics

### Initializers
- [init<C>(C)](./anyrandomaccesscollection/init%28_%29-1qlza.md)
  Creates a type-erased collection that wraps the given collection.
- [init?(AnyBidirectionalCollection<Element>)](./anyrandomaccesscollection/init%28_%29-2j41k.md)
  Creates an `AnyRandomAccessCollection` having the same underlying collection as `other`.
- [init(AnyRandomAccessCollection<Element>)](./anyrandomaccesscollection/init%28_%29-60sab.md)
  Creates an `AnyRandomAccessCollection` having the same underlying collection as `other`.
- [init?(AnyCollection<Element>)](./anyrandomaccesscollection/init%28_%29-66pkb.md)
  Creates an `AnyRandomAccessCollection` having the same underlying collection as `other`.
### Instance Methods
- [func drop(while: (Element) throws -> Bool) rethrows -> AnyRandomAccessCollection<Element>](./anyrandomaccesscollection/drop%28while%29.md)
- [func dropFirst(Int) -> AnyRandomAccessCollection<Element>](./anyrandomaccesscollection/dropfirst%28_%29.md)
- [func dropLast(Int) -> AnyRandomAccessCollection<Element>](./anyrandomaccesscollection/droplast%28_%29.md)
- [func filter((Element) throws -> Bool) rethrows -> [Element]](./anyrandomaccesscollection/filter%28_%29.md)
- [func forEach((Element) throws -> Void) rethrows](./anyrandomaccesscollection/foreach%28_%29.md)
- [func formIndex(inout AnyRandomAccessCollection<Element>.Index, offsetBy: Int)](./anyrandomaccesscollection/formindex%28_,offsetby%29.md)
- [func formIndex(inout AnyRandomAccessCollection<Element>.Index, offsetBy: Int, limitedBy: AnyRandomAccessCollection<Element>.Index) -> Bool](./anyrandomaccesscollection/formindex%28_,offsetby,limitedby%29.md)
- [func map<T, E>((Element) throws(E) -> T) throws(E) -> [T]](./anyrandomaccesscollection/map%28_%29.md)
- [func prefix(Int) -> AnyRandomAccessCollection<Element>](./anyrandomaccesscollection/prefix%28_%29.md)
- [func prefix(while: (Element) throws -> Bool) rethrows -> AnyRandomAccessCollection<Element>](./anyrandomaccesscollection/prefix%28while%29.md)
- [func suffix(Int) -> AnyRandomAccessCollection<Element>](./anyrandomaccesscollection/suffix%28_%29.md)
### Default Implementations
- [BidirectionalCollection Implementations](./anyrandomaccesscollection/bidirectionalcollection-implementations.md)
- [Collection Implementations](./anyrandomaccesscollection/collection-implementations.md)
- [RandomAccessCollection Implementations](./anyrandomaccesscollection/randomaccesscollection-implementations.md)
- [Sequence Implementations](./anyrandomaccesscollection/sequence-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](./bidirectionalcollection.md)
- [Collection](./collection.md)
- [Copyable](./copyable.md)
- [Escapable](./escapable.md)
- [RandomAccessCollection](./randomaccesscollection.md)
- [Sequence](./sequence.md)

## See Also

### Type-Erasing Wrappers
- [struct AnySequence](./anysequence.md)
  A type-erased sequence.
- [struct AnyCollection](./anycollection.md)
  A type-erased wrapper over any collection with indices that support forward traversal.
- [struct AnyBidirectionalCollection](./anybidirectionalcollection.md)
  A type-erased wrapper over any collection with indices that support bidirectional traversal.
- [struct AnyIterator](./anyiterator.md)
  A type-erased iterator of `Element`.
- [struct AnyIndex](./anyindex.md)
  A wrapper over an underlying index that hides the specific underlying type.
- [struct AnyHashable](./anyhashable.md)
  A type-erased hashable value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/anyrandomaccesscollection)*