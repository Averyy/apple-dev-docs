# CollectionOfOne

**Framework**: Swift  
**Kind**: struct

A collection containing a single element.

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
struct CollectionOfOne<Element>
```

#### Overview

You can use a `CollectionOfOne` instance when you need to efficiently represent a single value as a collection. For example, you can add a single element to an array by using a `CollectionOfOne` instance with the concatenation operator (`+`):

```swift
let a = [1, 2, 3, 4]
let toAdd = 100
let b = a + CollectionOfOne(toAdd)
// b == [1, 2, 3, 4, 100]
```

## Topics

### Initializers
- [init(Element)](collectionofone/init(_:).md)
  Creates an instance containing just the given element.
### Default Implementations
- [BidirectionalCollection Implementations](collectionofone/bidirectionalcollection-implementations.md)
- [Collection Implementations](collectionofone/collection-implementations.md)
- [CustomDebugStringConvertible Implementations](collectionofone/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](collectionofone/customreflectable-implementations.md)
- [MutableCollection Implementations](collectionofone/mutablecollection-implementations.md)
- [RandomAccessCollection Implementations](collectionofone/randomaccesscollection-implementations.md)
- [Sequence Implementations](collectionofone/sequence-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](bidirectionalcollection.md)
- [Collection](collection.md)
- [ContiguousBytes](../Foundation/ContiguousBytes.md)
- [Copyable](copyable.md)
- [CustomDebugStringConvertible](customdebugstringconvertible.md)
- [CustomReflectable](customreflectable.md)
- [MutableCollection](mutablecollection.md)
- [RandomAccessCollection](randomaccesscollection.md)
- [Sendable](sendable.md)
- [Sequence](sequence.md)

## See Also

- [func repeatElement<T>(T, count: Int) -> Repeated<T>](repeatelement(_:count:).md)
  Creates a collection containing the specified number of the given element.
- [struct EmptyCollection](emptycollection.md)
  A collection whose element type is `Element` but that is always empty.
- [struct KeyValuePairs](keyvaluepairs.md)
  A lightweight collection of key-value pairs.
- [typealias DictionaryLiteral](dictionaryliteral.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/collectionofone)*