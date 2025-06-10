# EmptyCollection

**Framework**: Swift  
**Kind**: struct

A collection whose element type is `Element` but that is always empty.

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
struct EmptyCollection<Element>
```

## Topics

### Initializers
- [init()](emptycollection/init.md)
  Creates an instance.
### Default Implementations
- [BidirectionalCollection Implementations](emptycollection/bidirectionalcollection-implementations.md)
- [Collection Implementations](emptycollection/collection-implementations.md)
- [Equatable Implementations](emptycollection/equatable-implementations.md)
- [MutableCollection Implementations](emptycollection/mutablecollection-implementations.md)
- [RandomAccessCollection Implementations](emptycollection/randomaccesscollection-implementations.md)
- [Sequence Implementations](emptycollection/sequence-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](bidirectionalcollection.md)
- [BitwiseCopyable](bitwisecopyable.md)
- [Collection](collection.md)
- [ContiguousBytes](../Foundation/ContiguousBytes.md)
- [Copyable](copyable.md)
- [DataProtocol](../Foundation/DataProtocol.md)
- [Equatable](equatable.md)
- [MutableCollection](mutablecollection.md)
- [RandomAccessCollection](randomaccesscollection.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)
- [Sequence](sequence.md)

## See Also

- [func repeatElement<T>(T, count: Int) -> Repeated<T>](repeatelement(_:count:).md)
  Creates a collection containing the specified number of the given element.
- [struct CollectionOfOne](collectionofone.md)
  A collection containing a single element.
- [struct KeyValuePairs](keyvaluepairs.md)
  A lightweight collection of key-value pairs.
- [typealias DictionaryLiteral](dictionaryliteral.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/emptycollection)*