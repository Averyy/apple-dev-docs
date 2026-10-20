# AnyCollection

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

A type-erased wrapper over any collection with indices that support forward traversal.

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
struct AnyCollection<Element>
```

#### Overview

An `AnyCollection` instance forwards its operations to a base collection having the same `Element` type, hiding the specifics of the underlying collection.

## Topics

### Initializers
- [init(AnyCollection<Element>)](./anycollection/init%28_%29-1jdmb.md)
  Creates an `AnyCollection` having the same underlying collection as `other`.
- [init<C>(C)](./anycollection/init%28_%29-33dcu.md)
  Creates a type-erased collection that wraps the given collection.
- [init(AnyBidirectionalCollection<Element>)](./anycollection/init%28_%29-598x3.md)
  Creates an `AnyCollection` having the same underlying collection as `other`.
- [init<C>(C)](./anycollection/init%28_%29-8k2a5.md)
  Creates a type-erased collection that wraps the given collection.
- [init(AnyRandomAccessCollection<Element>)](./anycollection/init%28_%29-91xl3.md)
  Creates an `AnyCollection` having the same underlying collection as `other`.
- [init<C>(C)](./anycollection/init%28_%29-9mgej.md)
  Creates a type-erased collection that wraps the given collection.
### Instance Methods
- [func drop(while: (Element) throws -> Bool) rethrows -> AnyCollection<Element>](./anycollection/drop%28while%29.md)
- [func dropFirst(Int) -> AnyCollection<Element>](./anycollection/dropfirst%28_%29.md)
- [func dropLast(Int) -> AnyCollection<Element>](./anycollection/droplast%28_%29.md)
- [func filter((Element) throws -> Bool) rethrows -> [Element]](./anycollection/filter%28_%29.md)
- [func forEach((Element) throws -> Void) rethrows](./anycollection/foreach%28_%29.md)
- [func formIndex(inout AnyCollection<Element>.Index, offsetBy: Int)](./anycollection/formindex%28_,offsetby%29.md)
- [func formIndex(inout AnyCollection<Element>.Index, offsetBy: Int, limitedBy: AnyCollection<Element>.Index) -> Bool](./anycollection/formindex%28_,offsetby,limitedby%29.md)
- [func map<T, E>((Element) throws(E) -> T) throws(E) -> [T]](./anycollection/map%28_%29.md)
- [func prefix(Int) -> AnyCollection<Element>](./anycollection/prefix%28_%29.md)
- [func prefix(while: (Element) throws -> Bool) rethrows -> AnyCollection<Element>](./anycollection/prefix%28while%29.md)
- [func suffix(Int) -> AnyCollection<Element>](./anycollection/suffix%28_%29.md)
### Default Implementations
- [Collection Implementations](./anycollection/collection-implementations.md)
- [Sequence Implementations](./anycollection/sequence-implementations.md)

## Relationships

### Conforms To
- [Collection](./collection.md)
- [Copyable](./copyable.md)
- [Escapable](./escapable.md)
- [Sequence](./sequence.md)

## See Also

### Type-Erasing Wrappers
- [struct AnySequence](./anysequence.md)
  A type-erased sequence.
- [struct AnyBidirectionalCollection](./anybidirectionalcollection.md)
  A type-erased wrapper over any collection with indices that support bidirectional traversal.
- [struct AnyRandomAccessCollection](./anyrandomaccesscollection.md)
  A type-erased wrapper over any collection with indices that support random access traversal.
- [struct AnyIterator](./anyiterator.md)
  A type-erased iterator of `Element`.
- [struct AnyIndex](./anyindex.md)
  A wrapper over an underlying index that hides the specific underlying type.
- [struct AnyHashable](./anyhashable.md)
  A type-erased hashable value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/anycollection)*